from pathlib import Path
from radical.data.compiler.analysis_result import AnalysisResult
from radical.data.compiler.errors import CompileError
from radical.data.interp.builtin_lookup import BuiltinLookup
from radical.data.parser.ast import BinaryOperationNode, ModuleNode, NumberLiteralNode
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
        module_parser = Parser(
            Lexer(contents=module_contents, filename=str(module_path)),
            filename=str(module_path),
        )
        module_ast = module_parser.parse_module()
        self._analyze_module(module_id, module_ast)
        self._namespace.mark_module_analyzed(module_id)
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

    def check_value(
        self, scope: AnalysisScope, name: str, bound: Type | None = None
    ) -> AnalysisResult:
        symbol_id = scope.intern_symbol(name)
        result = scope.lookup_binding(symbol_id)
        if not result:
            raise CompileError(f"Undefined symbol: {name}")
        self._check_type_annotation(result)
        self._check_value_assignment(result, bound)
        return result

    def check_type(self, scope: AnalysisScope, name: str) -> AnalysisResult:
        symbol_id = scope.intern_symbol(name)
        result = scope.lookup_type_binding(symbol_id)
        if not result:
            raise CompileError(f"Undefined type: {name}")
        self._check_value_assignment(result)
        return result

    def _check_type_annotation(self, result: AnalysisResult) -> None:
        if result.type_annotation_node and not result.type_annotation_expr:
            result.type_annotation_expr = self.infer(
                result.scope, result.type_annotation_node
            )
            type_value = self._interpreter.eval(result.type_annotation_expr)
            result.type_annotation = type_value

    def _check_value_assignment(
        self, result: AnalysisResult, bound: Type | None = None
    ) -> None:
        if result.value_node and not result.value_expr:
            result.value_expr = self.infer(result.scope, result.value_node, bound)
            if not isinstance(result.value_expr, SuspendedExpr):
                value = self._interpreter.eval(result.value_expr)
                result.value = value
        if bound:
            assert result.value_expr
            # TODO: improve unification error messages
            # TODO: unify should be a standalone function
            result.value_expr.type.unify(bound)

    def infer(
        self, scope: AnalysisScope, node: Node, bound: Type | None = None
    ) -> ExpressionType:
        if isinstance(node, BinaryOperationNode) and node.operator == Operator.PLUS:
            return self._infer_int_addition(scope, node)
        elif isinstance(node, NumberLiteralNode):
            return self._infer_int_literal(node)
        else:
            raise CompileError(f"Unsupported node type: {node}")

    def _infer_int_addition(
        self, scope: AnalysisScope, node: BinaryOperationNode
    ) -> ExpressionType:
        left_expr = self.infer(scope, node.left, self._builtin_lookup.int_type)
        right_expr = self.infer(scope, node.right, self._builtin_lookup.int_type)
        return AddExpr(
            type=self._builtin_lookup.int_type,
            node=node,
            left=left_expr,
            right=right_expr,
        )

    def _infer_int_literal(self, node: NumberLiteralNode) -> ExpressionType:
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
            case NumberFormat.FLOAT | NumberFormat.SCI_FLOAT:
                raise CompileError(
                    "Expected value of type Int, got value of type Float"
                )
            case NumberFormat.UNKNOWN:
                raise CompileError(f"Invalid integer literal: '{node.contents.value}'")
        return LiteralExpr(
            type=self._builtin_lookup.int_type, node=node, value=Value(value)
        )
