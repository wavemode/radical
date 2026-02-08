from radical.data.interp.builtin_lookup import BuiltinLookup
from radical.data.interp.value import Value
from radical.data.sema.expression import (
    AddIntExpr,
    ConstRefExpr,
    ExpressionType,
    TypeRefExpr,
    TypeUnionExpr,
)
from radical.data.sema.type import Type, UnionType
from radical.unit.interp.builtins import setup_builtins
from radical.util.core.unit import Unit
from radical.unit.interp.namespace import Namespace

from typing import assert_never


class Interpreter(Unit):
    _namespace: Namespace
    _builtins: BuiltinLookup

    def __init__(self, namespace: Namespace) -> None:
        self._namespace = namespace
        self._builtins = setup_builtins(self._namespace)

    def eval(self, expr: ExpressionType) -> Value:
        match expr:
            case AddIntExpr(left, right):
                left_val = self.eval(left)
                assert isinstance(left_val.value, int)
                right_val = self.eval(right)
                assert isinstance(right_val.value, int)
                return Value(left_val.value + right_val.value)
            case ConstRefExpr(_type, ref):
                return self._namespace.get_constant(ref)
            case TypeRefExpr(ref):
                return Value(self._namespace.get_type(ref))
            case TypeUnionExpr(left, right):
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

        assert_never(expr)
