from pathlib import Path
from typing import NoReturn
from radical.data.compiler.analysis_result import AnalysisResult
from radical.data.compiler.errors import CompileError
from radical.data.interp.builtin_lookup import BuiltinLookup
from radical.data.parser.ast import (
    BinaryOperationNode,
    BooleanLiteralNode,
    FloatLiteralNode,
    IntegerLiteralNode,
    ModuleNode,
    RegexLiteralNode,
    StringLiteralNode,
    SymbolNode,
)
from radical.data.parser.node import Node
from radical.data.parser.operator import Operator
from radical.data.parser.token import TokenType
from radical.data.sema.expression import (
    AddExpr,
    ExpressionType,
    LiteralExpr,
    LocalVarExpr,
)
from radical.data.sema.type import Type
from radical.data.sema.value import Value
from radical.unit.compiler.loader import Loader
from radical.unit.compiler.scope_tools import populate_decls
from radical.unit.compiler.scope import Scope
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

    def __init__(
        self, namespace: Namespace, loader: Loader, interpreter: Interpreter
    ) -> None:
        self._namespace = namespace
        self._loader = loader
        self._interpreter = interpreter

    def load_module(self, module_name: str) -> int:
        module_id = self._namespace.add_or_get_module(module_name)
        if self._namespace.module_is_analyzed(module_id):
            return module_id

        module_parts = module_name.split(".")
        module_path = Path(*module_parts).with_suffix(".rad")
        module_contents = self._loader.load_file(module_path)
        filename = str(module_path)
        module_parser = Parser(
            Lexer(contents=module_contents, filename=filename),
            filename=str(module_path),
        )
        module_ast = module_parser.parse_module()
        self._analyze_module(module_id, filename, module_ast)
        self._namespace.mark_module_analyzed(module_id)
        return module_id

    def _analyze_module(
        self, module_id: int, filename: str, module_ast: ModuleNode
    ) -> None:
        scope = Scope(
            module_id=module_id,
            filename=filename,
            namespace=self._namespace,
            parent=None,
        )
        self._builtin_lookup = setup_builtins(scope)
        populate_decls(scope, module_ast.body.declarations)
        for result in scope.type_bindings():
            self._check_value_assignment(scope, result)
        for result in scope.bindings():
            self._check_type_annotation(scope, result)
            self._check_value_assignment(scope, result)

    def _check_value(self, scope: Scope, symbol_id: int) -> AnalysisResult | None:
        result = scope.lookup_binding(symbol_id)
        if not result:
            return None
        self._check_type_annotation(scope, result)
        self._check_value_assignment(scope, result)
        return result

    def _check_type(self, scope: Scope, symbol_id: int) -> AnalysisResult | None:
        result = scope.lookup_type_binding(symbol_id)
        if not result:
            return None
        self._check_value_assignment(scope, result)
        return result

    def _check_type_annotation(self, scope: Scope, result: AnalysisResult) -> None:
        if result.type_annotation_node and not result.type_annotation_expr:
            result.type_annotation_expr = self._infer(
                result.scope, result.type_annotation_node
            )
            type_value = self._interpreter.eval(scope, result.type_annotation_expr)
            result.type_annotation = type_value

    def _check_value_assignment(self, scope: Scope, result: AnalysisResult) -> None:
        if result.value_node and not result.value_expr:
            result.value_expr = self._infer(result.scope, result.value_node)
            value = self._interpreter.eval(scope, result.value_expr)
            result.value = value

    def _infer(
        self, scope: Scope, node: Node, bound: Type | None = None
    ) -> ExpressionType:
        expr: ExpressionType
        if isinstance(node, BinaryOperationNode) and node.operator == Operator.PLUS:
            expr = self._infer_addition(scope, node)
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
        elif isinstance(node, BooleanLiteralNode):
            expr = self._infer_boolean_literal(node)
        else:
            self._raise_compile_error(
                scope, f"Unsupported syntax: {type(node).__name__}", node
            )

        if bound and not expr.type.unify(bound):
            self._raise_compile_error(
                scope,
                f"Type mismatch: expected {bound.name()}, got {expr.type.name()}",
                node,
            )
        return expr

    def _infer_boolean_literal(self, node: BooleanLiteralNode) -> ExpressionType:
        value = node.contents.type == TokenType.TRUE
        return LiteralExpr(
            type=self._builtin_lookup.bool_type, node=node, value=Value(value)
        )

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

    def _infer_symbol(self, scope: Scope, node: SymbolNode) -> ExpressionType:
        symbol_id = scope.intern_symbol(node.name.value)
        result = self._check_value(scope, symbol_id)
        if not result:
            self._raise_compile_error(
                scope, f"Undefined variable: '{node.name.value}'", node
            )
            raise RuntimeError("unreachable")  # appease type checker
        if not result.value_expr:
            self._raise_compile_error(
                scope, f"Variable '{node.name.value}' has no value assigned", node
            )
            raise RuntimeError("unreachable")  # appease type checker
        return LocalVarExpr(
            type=(
                result.type_annotation.value
                if result.type_annotation
                else result.value_expr.type
            ),
            node=node,
            symbol_id=symbol_id,
        )

    def _infer_addition(
        self, scope: Scope, node: BinaryOperationNode
    ) -> ExpressionType:
        output_type = self._builtin_lookup.int_type
        left_expr = self._infer(scope, node.left)
        right_expr = self._infer(scope, node.right)
        if left_expr.type.unify(self._builtin_lookup.float_type):
            output_type = self._builtin_lookup.float_type
        elif not left_expr.type.unify(self._builtin_lookup.int_type):
            self._raise_compile_error(
                scope,
                f"Unsupported operand types for `+`: {left_expr.type.name()} and {right_expr.type.name()}",
                left_expr.node or node,
            )
        if right_expr.type.unify(self._builtin_lookup.float_type):
            output_type = self._builtin_lookup.float_type
        elif not right_expr.type.unify(self._builtin_lookup.int_type):
            self._raise_compile_error(
                scope,
                f"Unsupported operand types for `+`: {left_expr.type.name()} and {right_expr.type.name()}",
                right_expr.node or node,
            )
        return AddExpr(
            type=output_type,
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

    def _raise_compile_error(self, scope: Scope, message: str, node: Node) -> NoReturn:
        position = node.position
        raise CompileError(message, position=position, filename=scope.filename())
