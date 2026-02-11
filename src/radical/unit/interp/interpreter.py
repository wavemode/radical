from fractions import Fraction
from radical.data.interp.errors import InterpreterError
from radical.data.parser.node import Node
from radical.data.sema.value import Value
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
    LiteralExpr,
    LocalVarExpr,
    ModuloExpr,
    MultiplyExpr,
    NegativeExpr,
    NotEqualExpr,
    NotExpr,
    OrExpr,
    SubExpr,
    ToFloatExpr,
    ToRationalExpr,
    TypeUnionExpr,
)
from radical.data.sema.type import Type, UnionType
from radical.unit.compiler.scope import Scope
from radical.util.core.unit import Unit

from typing import NoReturn, assert_never


class Interpreter(Unit):
    def __init__(self) -> None:
        pass

    def eval(self, scope: Scope, expr: ExpressionType) -> Value:
        if isinstance(expr, ToFloatExpr):
            return self._eval_to_float_expr(scope, expr)
        elif isinstance(expr, ToRationalExpr):
            return self._eval_to_rational_expr(scope, expr)
        elif isinstance(expr, NegativeExpr):
            return self._eval_negate_expr(scope, expr)
        elif isinstance(expr, NotExpr):
            return self._eval_not_expr(scope, expr)
        elif isinstance(expr, ExponentiationExpr):
            return self._eval_exponentiation_expr(scope, expr)
        elif isinstance(expr, MultiplyExpr):
            return self._eval_multiply_expr(scope, expr)
        elif isinstance(expr, FloorDivideExpr):
            return self._eval_floor_divide_expr(scope, expr)
        elif isinstance(expr, DivideExpr):
            return self._eval_divide_expr(scope, expr)
        elif isinstance(expr, ModuloExpr):
            return self._eval_modulo_expr(scope, expr)
        elif isinstance(expr, AddExpr):
            return self._eval_add_expr(scope, expr)
        elif isinstance(expr, SubExpr):
            return self._eval_sub_expr(scope, expr)
        elif isinstance(expr, EqualExpr):
            return self._eval_equal_expr(scope, expr)
        elif isinstance(expr, NotEqualExpr):
            return self._eval_not_equal_expr(scope, expr)
        elif isinstance(expr, LessThanEqualExpr):
            return self._eval_less_than_equal_expr(scope, expr)
        elif isinstance(expr, GreaterThanEqualExpr):
            return self._eval_greater_than_equal_expr(scope, expr)
        elif isinstance(expr, LessThanExpr):
            return self._eval_less_than_expr(scope, expr)
        elif isinstance(expr, GreaterThanExpr):
            return self._eval_greater_than_expr(scope, expr)
        elif isinstance(expr, AndExpr):
            return self._eval_and_expr(scope, expr)
        elif isinstance(expr, OrExpr):
            return self._eval_or_expr(scope, expr)
        elif isinstance(expr, TypeUnionExpr):
            return self._eval_type_union_expr(scope, expr)
        elif isinstance(expr, LiteralExpr):
            return self._eval_literal_expr(scope, expr)
        elif isinstance(expr, LocalVarExpr):
            return self._eval_local_var_expr(scope, expr)

        assert_never(expr)

    def _eval_sub_expr(self, scope: Scope, expr: SubExpr) -> Value:
        left_val = self.eval(scope, expr.left)
        right_val = self.eval(scope, expr.right)
        return Value(left_val.value - right_val.value)

    def _eval_to_rational_expr(self, scope: Scope, expr: ToRationalExpr) -> Value:
        operand_val = self.eval(scope, expr.operand)
        return Value(Fraction(operand_val.value, 1))

    def _eval_modulo_expr(self, scope: Scope, expr: ModuloExpr) -> Value:
        left_val = self.eval(scope, expr.left)
        right_val = self.eval(scope, expr.right)
        return Value(left_val.value % right_val.value)

    def _eval_less_than_equal_expr(
        self, scope: Scope, expr: LessThanEqualExpr
    ) -> Value:
        left_val = self.eval(scope, expr.left)
        right_val = self.eval(scope, expr.right)
        return Value(left_val.value <= right_val.value)

    def _eval_greater_than_equal_expr(
        self, scope: Scope, expr: GreaterThanEqualExpr
    ) -> Value:
        left_val = self.eval(scope, expr.left)
        right_val = self.eval(scope, expr.right)
        return Value(left_val.value >= right_val.value)

    def _eval_less_than_expr(self, scope: Scope, expr: LessThanExpr) -> Value:
        left_val = self.eval(scope, expr.left)
        right_val = self.eval(scope, expr.right)
        return Value(left_val.value < right_val.value)

    def _eval_greater_than_expr(self, scope: Scope, expr: GreaterThanExpr) -> Value:
        left_val = self.eval(scope, expr.left)
        right_val = self.eval(scope, expr.right)
        return Value(left_val.value > right_val.value)

    def _eval_and_expr(self, scope: Scope, expr: AndExpr) -> Value:
        left_val = self.eval(scope, expr.left)
        if not left_val.value:
            return Value(False)
        right_val = self.eval(scope, expr.right)
        return Value(bool(right_val.value))

    def _eval_or_expr(self, scope: Scope, expr: OrExpr) -> Value:
        left_val = self.eval(scope, expr.left)
        if left_val.value:
            return Value(True)
        right_val = self.eval(scope, expr.right)
        return Value(bool(right_val.value))

    def _eval_not_equal_expr(self, scope: Scope, expr: NotEqualExpr) -> Value:
        left_val = self.eval(scope, expr.left)
        right_val = self.eval(scope, expr.right)
        return Value(left_val.value != right_val.value)

    def _eval_equal_expr(self, scope: Scope, expr: EqualExpr) -> Value:
        left_val = self.eval(scope, expr.left)
        right_val = self.eval(scope, expr.right)
        return Value(left_val.value == right_val.value)

    def _eval_divide_expr(self, scope: Scope, expr: DivideExpr) -> Value:
        left_val = self.eval(scope, expr.left)
        right_val = self.eval(scope, expr.right)
        return Value(left_val.value / right_val.value)

    def _eval_floor_divide_expr(self, scope: Scope, expr: FloorDivideExpr) -> Value:
        left_val = self.eval(scope, expr.left)
        right_val = self.eval(scope, expr.right)
        return Value(int(left_val.value // right_val.value))

    def _eval_multiply_expr(self, scope: Scope, expr: MultiplyExpr) -> Value:
        left_val = self.eval(scope, expr.left)
        right_val = self.eval(scope, expr.right)
        return Value(left_val.value * right_val.value)

    def _eval_exponentiation_expr(
        self, scope: Scope, expr: ExponentiationExpr
    ) -> Value:
        left_val = self.eval(scope, expr.left)
        right_val = self.eval(scope, expr.right)
        return Value(left_val.value**right_val.value)

    def _eval_not_expr(self, scope: Scope, expr: NotExpr) -> Value:
        operand_val = self.eval(scope, expr.operand)
        return Value(not operand_val.value)

    def _eval_to_float_expr(self, scope: Scope, expr: ToFloatExpr) -> Value:
        operand_val = self.eval(scope, expr.operand)
        return Value(float(operand_val.value))

    def _eval_negate_expr(self, scope: Scope, expr: NegativeExpr) -> Value:
        operand_val = self.eval(scope, expr.operand)
        return Value(-operand_val.value)

    def _eval_local_var_expr(self, scope: Scope, expr: LocalVarExpr) -> Value:
        binding = scope.lookup_binding(expr.symbol_id)
        if not binding or not binding.value:
            # should be unreachable
            raise RuntimeError(f"Undefined variable with symbol ID {expr.symbol_id}")
        return binding.value

    def _eval_literal_expr(self, scope: Scope, expr: LiteralExpr) -> Value:
        return expr.value

    def _eval_add_expr(self, scope: Scope, expr: AddExpr) -> Value:
        left_val = self.eval(scope, expr.left)
        right_val = self.eval(scope, expr.right)
        return Value(left_val.value + right_val.value)

    def _eval_type_union_expr(self, scope: Scope, expr: TypeUnionExpr) -> Value:
        types: set[Type] = set()

        left_type = self.eval(scope, expr.left)
        assert isinstance(left_type.value, Type)
        if isinstance(left_type.value, UnionType):
            types.update(left_type.value.types)
        else:
            types.add(left_type.value)

        right_type = self.eval(scope, expr.right)
        if isinstance(right_type.value, UnionType):
            types.update(right_type.value.types)
        else:
            types.add(right_type.value)

        return Value(UnionType(types=types))

    def _raise_interp_error(self, scope: Scope, message: str, node: Node) -> NoReturn:
        raise InterpreterError(
            message=message,
            position=node.position,
            filename=scope.filename(),
        )
