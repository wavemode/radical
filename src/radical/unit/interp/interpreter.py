from radical.data.interp.builtin_lookup import BuiltinLookup
from radical.data.interp.value import Value
from radical.data.sema.expression import AddIntExpr, ConstExpr, ExpressionType
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
            case ConstExpr(_type, ref):
                return self._namespace.get_constant(ref)
        assert_never(expr)
