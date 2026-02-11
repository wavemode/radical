from collections.abc import Callable
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
    NullLiteralNode,
    ParenthesizedExpressionNode,
    RegexLiteralNode,
    StringLiteralNode,
    SymbolNode,
    UnaryOperationNode,
)
from radical.data.parser.node import Node
from radical.data.parser.operator import Operator
from radical.data.parser.token import TokenType
from radical.data.sema.expression import (
    AddExpr,
    AndExpr,
    DivideExpr,
    EqualExpr,
    ExponentiationExpr,
    ExpressionType,
    FloorDivideExpr,
    GreaterThanEqualExpr,
    GreaterThanExpr,
    LessThanEqualExpr,
    LessThanExpr,
    ModuloExpr,
    MultiplyExpr,
    NegativeExpr,
    NotEqualExpr,
    NotExpr,
    OrExpr,
    SubExpr,
    ToFloatExpr,
    LiteralExpr,
    LocalVarExpr,
    ToRationalExpr,
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
        if isinstance(node, BinaryOperationNode):
            expr = self._infer_binary_op(scope, node)
        elif isinstance(node, UnaryOperationNode):
            expr = self._infer_unary_op(scope, node)
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
        elif isinstance(node, NullLiteralNode):
            expr = self._infer_null_literal(node)
        elif isinstance(node, ParenthesizedExpressionNode) and len(node.elements) == 1:
            expr = self._infer(scope, node.elements[0])
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

    def _infer_null_literal(self, node: NullLiteralNode) -> ExpressionType:
        return LiteralExpr(
            type=self._builtin_lookup.null_type, node=node, value=Value(None)
        )

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

    def _infer_unary_op(self, scope: Scope, node: UnaryOperationNode) -> ExpressionType:
        operand_expr = self._infer(scope, node.operand)
        match node.operator:
            case Operator.POSITIVE:
                return self._ensure_number(scope, operand_expr)
            case Operator.NEGATIVE:
                if self._is_float(operand_expr):
                    return NegativeExpr(
                        type=self._builtin_lookup.float_type,
                        node=node,
                        operand=operand_expr,
                    )
                if self._is_rational(operand_expr):
                    return NegativeExpr(
                        type=self._builtin_lookup.rational_type,
                        node=node,
                        operand=operand_expr,
                    )
                self._ensure_number(scope, operand_expr)
                return NegativeExpr(
                    type=self._builtin_lookup.int_type,
                    node=node,
                    operand=self._ensure_int(scope, operand_expr),
                )
            case Operator.NOT:
                return NotExpr(
                    type=self._builtin_lookup.bool_type,
                    node=node,
                    operand=self._ensure_boolean(scope, operand_expr),
                )
            case _:
                raise RuntimeError("unreachable")

    _standard_promotion_ops: dict[
        Operator, Callable[[Type, Node, ExpressionType, ExpressionType], ExpressionType]
    ] = {
        Operator.MULTIPLY: MultiplyExpr,
        Operator.MODULO: ModuloExpr,
        Operator.PLUS: AddExpr,
        Operator.MINUS: SubExpr,
    }

    _standard_promotion_comps: dict[
        Operator, Callable[[Type, Node, ExpressionType, ExpressionType], ExpressionType]
    ] = {
        Operator.EQUAL: EqualExpr,
        Operator.NOT_EQUAL: NotEqualExpr,
        Operator.LESS_THAN_EQUAL: LessThanEqualExpr,
        Operator.GREATER_THAN_EQUAL: GreaterThanEqualExpr,
        Operator.LESS_THAN: LessThanExpr,
        Operator.GREATER_THAN: GreaterThanExpr,
    }

    def _infer_binary_op(
        self, scope: Scope, node: BinaryOperationNode
    ) -> ExpressionType:
        left_expr = self._infer(scope, node.left)
        right_expr = self._infer(scope, node.right)
        if self._is_number(left_expr) or self._is_number(right_expr):
            left_num = self._ensure_number(scope, left_expr)
            right_num = self._ensure_number(scope, right_expr)
            if node.operator in self._standard_promotion_ops:
                promotion_func = self._standard_promotion_ops[node.operator]
                if self._is_float(left_num) or self._is_float(right_num):
                    return promotion_func(
                        self._builtin_lookup.float_type,
                        node,
                        self._ensure_float(scope, left_num),
                        self._ensure_float(scope, right_num),
                    )
                if self._is_rational(left_num) or self._is_rational(right_num):
                    return promotion_func(
                        self._builtin_lookup.rational_type,
                        node,
                        self._ensure_rational(scope, left_num),
                        self._ensure_rational(scope, right_num),
                    )
                return promotion_func(
                    self._builtin_lookup.int_type,
                    node,
                    self._ensure_int(scope, left_num),
                    self._ensure_int(scope, right_num),
                )
            if node.operator in self._standard_promotion_comps:
                promotion_func = self._standard_promotion_comps[node.operator]
                if self._is_float(left_num) or self._is_float(right_num):
                    return promotion_func(
                        self._builtin_lookup.bool_type,
                        node,
                        self._ensure_float(scope, left_num),
                        self._ensure_float(scope, right_num),
                    )
                if self._is_rational(left_num) or self._is_rational(right_num):
                    return promotion_func(
                        self._builtin_lookup.bool_type,
                        node,
                        self._ensure_rational(scope, left_num),
                        self._ensure_rational(scope, right_num),
                    )
                return promotion_func(
                    self._builtin_lookup.bool_type,
                    node,
                    self._ensure_int(scope, left_num),
                    self._ensure_int(scope, right_num),
                )
            if node.operator == Operator.EXPONENTIATION:
                return ExponentiationExpr(
                    self._builtin_lookup.float_type,
                    node,
                    self._ensure_float(scope, left_num),
                    self._ensure_float(scope, right_num),
                )
            if node.operator == Operator.FLOOR_DIVIDE:
                if self._is_float(left_num) or self._is_float(right_num):
                    return FloorDivideExpr(
                        type=self._builtin_lookup.int_type,
                        node=node,
                        left=self._ensure_float(scope, left_num),
                        right=self._ensure_float(scope, right_num),
                    )
                if self._is_rational(left_num) or self._is_rational(right_num):
                    return FloorDivideExpr(
                        type=self._builtin_lookup.int_type,
                        node=node,
                        left=self._ensure_rational(scope, left_num),
                        right=self._ensure_rational(scope, right_num),
                    )
                return FloorDivideExpr(
                    type=self._builtin_lookup.int_type,
                    node=node,
                    left=self._ensure_int(scope, left_num),
                    right=self._ensure_int(scope, right_num),
                )
            if node.operator == Operator.DIVIDE:
                if self._is_float(left_num) or self._is_float(right_num):
                    return DivideExpr(
                        type=self._builtin_lookup.float_type,
                        node=node,
                        left=self._ensure_float(scope, left_num),
                        right=self._ensure_float(scope, right_num),
                    )
                if self._is_rational(left_num) or self._is_rational(right_num):
                    return DivideExpr(
                        type=self._builtin_lookup.rational_type,
                        node=node,
                        left=self._ensure_rational(scope, left_num),
                        right=self._ensure_rational(scope, right_num),
                    )
                return DivideExpr(
                    type=self._builtin_lookup.rational_type,
                    node=node,
                    left=self._ensure_rational(scope, left_num),
                    right=self._ensure_rational(scope, right_num),
                )
        if (
            self._is_boolean(left_expr) or self._is_boolean(right_expr)
        ) and node.operator in (
            Operator.AND,
            Operator.OR,
            Operator.EQUAL,
            Operator.NOT_EQUAL,
        ):
            left_bool = self._ensure_boolean(scope, left_expr)
            right_bool = self._ensure_boolean(scope, right_expr)
            if node.operator == Operator.AND:
                return AndExpr(
                    type=self._builtin_lookup.bool_type,
                    node=node,
                    left=left_bool,
                    right=right_bool,
                )
            if node.operator == Operator.OR:
                return OrExpr(
                    type=self._builtin_lookup.bool_type,
                    node=node,
                    left=left_bool,
                    right=right_bool,
                )
        if (
            self._is_string(left_expr) or self._is_string(right_expr)
        ) and node.operator == Operator.PLUS:
            left_str = self._ensure_string(scope, left_expr)
            right_str = self._ensure_string(scope, right_expr)
            if node.operator == Operator.PLUS:
                return AddExpr(
                    type=self._builtin_lookup.string_type,
                    node=node,
                    left=left_str,
                    right=right_str,
                )
        # TODO: this shouldn't be supported for certain types, e.g. functions
        if node.operator in (
            Operator.EQUAL,
            Operator.NOT_EQUAL,
        ) and left_expr.type.unify(right_expr.type):
            return (
                EqualExpr(
                    type=self._builtin_lookup.bool_type,
                    node=node,
                    left=left_expr,
                    right=right_expr,
                )
                if node.operator == Operator.EQUAL
                else NotEqualExpr(
                    type=self._builtin_lookup.bool_type,
                    node=node,
                    left=left_expr,
                    right=right_expr,
                )
            )
        self._raise_compile_error(
            scope,
            (
                f"Unsupported operand types for operator '{node.operator.value}': "
                f"{left_expr.type.name()} and {right_expr.type.name()}"
            ),
            node,
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

    def _ensure_float(self, scope: Scope, expr: ExpressionType) -> ExpressionType:
        if expr.type.unify(self._builtin_lookup.float_type):
            return expr
        elif expr.type.unify(self._builtin_lookup.int_type) or expr.type.unify(
            self._builtin_lookup.rational_type
        ):
            return ToFloatExpr(
                type=self._builtin_lookup.float_type, node=expr.node, operand=expr
            )
        self._raise_compile_error(
            scope,
            f"Expected Int or Float operand, got {expr.type.name()}",
            expr.node,
        )

    def _ensure_int(self, scope: Scope, expr: ExpressionType) -> ExpressionType:
        if not expr.type.unify(self._builtin_lookup.int_type):
            self._raise_compile_error(
                scope, f"Expected Int operand, got {expr.type.name()}", expr.node
            )
        return expr

    def _ensure_number(self, scope: Scope, expr: ExpressionType) -> ExpressionType:
        if not (
            expr.type.unify(self._builtin_lookup.int_type)
            or expr.type.unify(self._builtin_lookup.float_type)
            or expr.type.unify(self._builtin_lookup.rational_type)
        ):
            self._raise_compile_error(
                scope,
                f"Expected numerical operand, got {expr.type.name()}",
                expr.node,
            )
        return expr

    def _ensure_rational(self, scope: Scope, expr: ExpressionType) -> ExpressionType:
        if expr.type.unify(self._builtin_lookup.int_type):
            return ToRationalExpr(
                type=self._builtin_lookup.rational_type,
                node=expr.node,
                operand=expr,
            )
        if not expr.type.unify(self._builtin_lookup.rational_type):
            self._raise_compile_error(
                scope,
                f"Expected Int or Rational operand, got {expr.type.name()}",
                expr.node,
            )
        return expr

    def _ensure_boolean(self, scope: Scope, expr: ExpressionType) -> ExpressionType:
        if not expr.type.unify(self._builtin_lookup.bool_type):
            self._raise_compile_error(
                scope, f"Expected Bool operand, got {expr.type.name()}", expr.node
            )
        return expr

    def _ensure_string(self, scope: Scope, expr: ExpressionType) -> ExpressionType:
        if not expr.type.unify(self._builtin_lookup.string_type):
            self._raise_compile_error(
                scope, f"Expected String operand, got {expr.type.name()}", expr.node
            )
        return expr

    def _is_float(self, expr: ExpressionType) -> bool:
        return expr.type.unify(self._builtin_lookup.float_type)

    def _is_int(self, expr: ExpressionType) -> bool:
        return expr.type.unify(self._builtin_lookup.int_type)

    def _is_rational(self, expr: ExpressionType) -> bool:
        return expr.type.unify(self._builtin_lookup.rational_type)

    def _is_number(self, expr: ExpressionType) -> bool:
        return self._is_int(expr) or self._is_float(expr) or self._is_rational(expr)

    def _is_boolean(self, expr: ExpressionType) -> bool:
        return expr.type.unify(self._builtin_lookup.bool_type)

    def _is_string(self, expr: ExpressionType) -> bool:
        return expr.type.unify(self._builtin_lookup.string_type)

    def _raise_compile_error(self, scope: Scope, message: str, node: Node) -> NoReturn:
        position = node.position
        raise CompileError(message, position=position, filename=scope.filename())
