from unittest import TestCase

import os

from radical.data.sema.expression import AddIntExpr, ConstExpr
from radical.unit.interp.namespace import Namespace
from radical.unit.interp.interpreter import Interpreter
from radical.data.interp.value import Value

if os.environ.get("RAD_DEBUG"):
    import debugpy

    debugpy.listen(5678)
    debugpy.wait_for_client()


class TestInterpreter(TestCase):
    maxDiff = None

    def test_addition(self) -> None:
        namespace = Namespace()
        interpreter = Interpreter(namespace)

        builtin_module_id = namespace.add_or_get_module("Core.Builtin")
        int_type_name = namespace.intern_symbol(builtin_module_id, "Int")
        int_type_ref = namespace.lookup_type_binding(int_type_name)

        module_id = namespace.add_or_get_module("Test")
        const_ref_1 = namespace.intern_constant(module_id, Value(1))
        const_ref_2 = namespace.intern_constant(module_id, Value(2))
        result = interpreter.eval(
            AddIntExpr(
                ConstExpr(int_type_ref, const_ref_1),
                ConstExpr(int_type_ref, const_ref_2),
            )
        )
        self.assertEqual(result, Value(3))
