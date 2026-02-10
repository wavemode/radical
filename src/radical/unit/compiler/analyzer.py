from pathlib import Path
from typing import NoReturn
from radical.data.compiler.analysis_result import AnalysisResult
from radical.data.compiler.errors import CompileError
from radical.data.interp.builtin_lookup import BuiltinLookup
from radical.data.parser.ast import (
    BinaryOperationNode,
    FloatLiteralNode,
    IntegerLiteralNode,
    ModuleNode,
    RegexLiteralNode,
    StringLiteralNode,
    SymbolNode,
)
from radical.data.parser.node import Node
from radical.data.parser.operator import Operator
from radical.data.sema.expression import (
    AddExpr,
    ExpressionType,
    LiteralExpr,
    SuspendedExpr,
)
from radical.data.sema.type import Type
from radical.data.sema.value import Value
from radical.unit.compiler.loader import Loader
from radical.unit.compiler.scope_tools import populate_decls
from radical.unit.compiler.analysis_scope import AnalysisScope
from radical.unit.interp.builtins import setup_builtins
from radical.unit.interp.interpreter import Interpreter
from radical.unit.parser.lexer import Lexer
from radical.unit.parser.number_parsing import NumberFormat, identify_number_literal
from radical.unit.parser.parser import Parser
from radical.unit.sema.namespace import Namespace
from radical.util.core.unit import Unit


class Analyzer(Unit):
    _namespace: Namespace
    _loader: Loader
    _interpreter: Interpreter
    _builtin_lookup: BuiltinLookup

    _current_filename: str | None

    def __init__(
        self, namespace: Namespace, loader: Loader, interpreter: Interpreter
    ) -> None:
        self._namespace = namespace
        self._loader = loader
        self._interpreter = interpreter
        self._current_filename = None

    def load_module(self, module_name: str) -> int:
        module_id = self._namespace.add_or_get_module(module_name)
        if self._namespace.module_is_analyzed(module_id):
            return module_id

        module_parts = module_name.split(".")
        module_path = Path(*module_parts).with_suffix(".rad")
        module_contents = self._loader.load_file(module_path)
        self._current_filename = str(module_path)
        module_parser = Parser(
            Lexer(contents=module_contents, filename=self._current_filename),
            filename=str(module_path),
        )
        module_ast = module_parser.parse_module()
        self._analyze_module(module_id, module_ast)
        self._namespace.mark_module_analyzed(module_id)
        self._current_filename = None
        return module_id

    def _analyze_module(self, module_id: int, module_ast: ModuleNode) -> None:
        root_scope = AnalysisScope(
            module_id=module_id,
            namespace=self._namespace,
            parent=None,
        )
        self._builtin_lookup = setup_builtins(root_scope)
        populate_decls(root_scope, module_ast.body.declarations)
        for result in root_scope.type_bindings():
            self._check_value_assignment(result)
        for result in root_scope.bindings():
            self._check_type_annotation(result)
            self._check_value_assignment(result)

    def _check_value(self, scope: AnalysisScope, name: str) -> AnalysisResult | None:
        symbol_id = scope.intern_symbol(name)
        result = scope.lookup_binding(symbol_id)
        if not result:
            return None
        self._check_type_annotation(result)
        self._check_value_assignment(result)
        return result

    def _check_type(self, scope: AnalysisScope, name: str) -> AnalysisResult | None:
        symbol_id = scope.intern_symbol(name)
        result = scope.lookup_type_binding(symbol_id)
        if not result:
            return None
        self._check_value_assignment(result)
        return result

    def _check_type_annotation(self, result: AnalysisResult) -> None:
        if result.type_annotation_node and not result.type_annotation_expr:
            result.type_annotation_expr = self._infer(
                result.scope, result.type_annotation_node
            )
            type_value = self._interpreter.eval(result.type_annotation_expr)
            result.type_annotation = type_value

    def _check_value_assignment(self, result: AnalysisResult) -> None:
        if result.value_node and not result.value_expr:
            result.value_expr = self._infer(result.scope, result.value_node)
            if not isinstance(result.value_expr, SuspendedExpr):
                value = self._interpreter.eval(result.value_expr)
                result.value = value

    def _infer(
        self, scope: AnalysisScope, node: Node, bound: Type | None = None
    ) -> ExpressionType:
        expr: ExpressionType
        if isinstance(node, BinaryOperationNode) and node.operator == Operator.PLUS:
            expr = self._infer_int_addition(scope, node)
        elif isinstance(node, IntegerLiteralNode):
            expr = self._infer_int_literal(node)
        elif isinstance(node, FloatLiteralNode):
            expr = self._infer_float_literal(node)
        elif isinstance(node, SymbolNode):
            expr = self._infer_symbol(scope, node)
        elif isinstance(node, StringLiteralNode):
            expr = self._infer_string_literal(node)
        elif isinstance(node, RegexLiteralNode):
            expr = self._infer_regex_literal(node)
        else:
            self._raise_compile_error(
                f"Unsupported syntax: {type(node).__name__}", node
            )

        if bound and not expr.type.unify(bound):
            self._raise_compile_error(
                f"Type mismatch: expected {bound.name()}, got {expr.type.name()}",
                node,
            )
        return expr

    def _infer_regex_literal(self, node: RegexLiteralNode) -> ExpressionType:
        return LiteralExpr(
            type=self._builtin_lookup.regex_type,
            node=node,
            value=Value(node.contents.value),
        )

    def _infer_string_literal(self, node: StringLiteralNode) -> ExpressionType:
        return LiteralExpr(
            type=self._builtin_lookup.string_type,
            node=node,
            value=Value(node.contents.value),
        )

    def _infer_symbol(self, scope: AnalysisScope, node: SymbolNode) -> ExpressionType:
        result = self._check_value(scope, node.name.value)
        if not result:
            self._raise_compile_error(f"Undefined variable: '{node.name.value}'", node)
            raise RuntimeError("unreachable")  # appease type checker
        if not result.value_expr:
            self._raise_compile_error(
                f"Variable '{node.name.value}' has no value assigned", node
            )
            raise RuntimeError("unreachable")  # appease type checker
        return result.value_expr

    def _infer_int_addition(
        self, scope: AnalysisScope, node: BinaryOperationNode
    ) -> ExpressionType:
        left_expr = self._infer(scope, node.left, self._builtin_lookup.int_type)
        right_expr = self._infer(scope, node.right, self._builtin_lookup.int_type)
        return AddExpr(
            type=self._builtin_lookup.int_type,
            node=node,
            left=left_expr,
            right=right_expr,
        )

    def _infer_float_literal(self, node: FloatLiteralNode) -> ExpressionType:
        value = float(node.contents.value)
        return LiteralExpr(
            type=self._builtin_lookup.float_type, node=node, value=Value(value)
        )

    def _infer_int_literal(self, node: IntegerLiteralNode) -> ExpressionType:
        value: int
        match identify_number_literal(node.contents.value):
            case NumberFormat.DECIMAL:
                value = int(node.contents.value, 10)
            case NumberFormat.BINARY:
                value = int(node.contents.value, 2)
            case NumberFormat.OCTAL:
                value = int(node.contents.value, 8)
            case NumberFormat.HEXADECIMAL:
                value = int(node.contents.value, 16)
            case _:
                raise RuntimeError("unreachable")
        return LiteralExpr(
            type=self._builtin_lookup.int_type, node=node, value=Value(value)
        )

    def _raise_compile_error(self, message: str, node: Node) -> NoReturn:
        position = node.position
        filename = self._current_filename or "<unknown>"
        raise CompileError(message, position=position, filename=filename)
