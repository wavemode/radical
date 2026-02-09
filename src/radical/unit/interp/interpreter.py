from radical.data.interp.builtin_lookup import BuiltinLookup
from radical.data.interp.errors import InterpreterError
from radical.data.sema.value import Value
from radical.data.sema.expression import (
    AddExpr,
    ExpressionType,
    LiteralExpr,
    SuspendedExpr,
    TypeUnionExpr,
)
from radical.data.sema.type import IntType, Type, UnionType
from radical.util.core.unit import Unit
from radical.unit.sema.namespace import Namespace

from typing import assert_never


class Interpreter(Unit):
    _namespace: Namespace
    _builtins: BuiltinLookup

    def __init__(self, namespace: Namespace) -> None:
        self._namespace = namespace

    def eval(self, expr: ExpressionType) -> Value:
        match expr:
            case AddExpr(_type, left, right):
                # TODO: support addition for more data types
                assert isinstance(_type, IntType)
                left_val = self.eval(left)
                assert isinstance(left_val.value, int)
                right_val = self.eval(right)
                assert isinstance(right_val.value, int)
                return Value(left_val.value + right_val.value)
            case TypeUnionExpr(_type, left, right):
                types: set[Type] = set()

                left_type = self.eval(left)
                assert isinstance(left_type.value, Type)
                if isinstance(left_type.value, UnionType):
                    types.update(left_type.value.types)
                else:
                    types.add(left_type.value)

                right_type = self.eval(right)
                if isinstance(right_type.value, UnionType):
                    types.update(right_type.value.types)
                else:
                    types.add(right_type.value)

                return Value(UnionType(types=types))
            case LiteralExpr(_type, value):
                return value
            case SuspendedExpr(_type, expr):
                raise InterpreterError("Cannot evaluate suspended expression")

        assert_never(expr)
