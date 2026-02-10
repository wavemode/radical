from radical.data.interp.errors import InterpreterError
from radical.data.parser.node import Node
from radical.data.sema.value import Value
from radical.data.sema.expression import (
    AddExpr,
    ExpressionType,
    LiteralExpr,
    LocalVarExpr,
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
        if isinstance(expr, AddExpr):
            left_val = self.eval(scope, expr.left)
            right_val = self.eval(scope, expr.right)
            return Value(left_val.value + right_val.value)
        elif isinstance(expr, TypeUnionExpr):
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
        elif isinstance(expr, LiteralExpr):
            return expr.value
        elif isinstance(expr, LocalVarExpr):
            binding = scope.lookup_binding(expr.symbol_id)
            if not binding or not binding.value:
                # should be unreachable
                raise RuntimeError(
                    f"Undefined variable with symbol ID {expr.symbol_id}"
                )
            return binding.value

        assert_never(expr)

    def _raise_interp_error(self, scope: Scope, message: str, node: Node) -> NoReturn:
        raise InterpreterError(
            message=message,
            position=node.position,
            filename=scope.filename(),
        )
