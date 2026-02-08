from unittest import TestCase

from radical.data.sema.expression import (
    AddIntExpr,
    ConstRefExpr,
    TypeRefExpr,
    TypeUnionExpr,
)
from radical.data.sema.type import UnionType
from radical.unit.interp.namespace import Namespace
from radical.unit.interp.interpreter import Interpreter
from radical.data.interp.value import Value


class TestInterpreter(TestCase):
    maxDiff = None

    def test_simple_expr(self) -> None:
        namespace = Namespace()
        interpreter = Interpreter(namespace)

        builtin_module_id = namespace.add_or_get_module("Core.Builtin")
        int_type_name = namespace.add_or_get_symbol(builtin_module_id, "Int")
        int_type_ref = namespace.lookup_type_binding(int_type_name)
        int_type = namespace.get_type(int_type_ref)

        module_id = namespace.add_or_get_module("Test")
        const_ref_1 = namespace.intern_constant(module_id, Value(1))
        const_ref_2 = namespace.intern_constant(module_id, Value(2))
        result = interpreter.eval(
            AddIntExpr(
                ConstRefExpr(int_type, const_ref_1),
                ConstRefExpr(int_type, const_ref_2),
            )
        )
        self.assertEqual(result, Value(3))

    def test_type_union_expr(self) -> None:
        namespace = Namespace()
        interpreter = Interpreter(namespace)

        builtin_module_id = namespace.add_or_get_module("Core.Builtin")
        int_type_name = namespace.add_or_get_symbol(builtin_module_id, "Int")
        int_type_ref = namespace.lookup_type_binding(int_type_name)
        int_type = namespace.get_type(int_type_ref)
        string_type_name = namespace.add_or_get_symbol(builtin_module_id, "String")
        string_type_ref = namespace.lookup_type_binding(string_type_name)
        string_type = namespace.get_type(string_type_ref)

        expected_result = Value(UnionType(types={int_type, string_type}))

        # Int | String
        result = interpreter.eval(
            TypeUnionExpr(
                TypeRefExpr(int_type_ref),
                TypeRefExpr(string_type_ref),
            )
        )
        self.assertEqual(result, expected_result)

        # String | Int
        result = interpreter.eval(
            TypeUnionExpr(
                TypeRefExpr(string_type_ref),
                TypeRefExpr(int_type_ref),
            )
        )
        self.assertEqual(result, expected_result)

        # (Int | String) | Int
        result = interpreter.eval(
            TypeUnionExpr(
                TypeUnionExpr(
                    TypeRefExpr(int_type_ref),
                    TypeRefExpr(string_type_ref),
                ),
                TypeRefExpr(int_type_ref),
            )
        )
        self.assertEqual(result, expected_result)

        # Int | (String | Int)
        result = interpreter.eval(
            TypeUnionExpr(
                TypeRefExpr(int_type_ref),
                TypeUnionExpr(
                    TypeRefExpr(string_type_ref),
                    TypeRefExpr(int_type_ref),
                ),
            )
        )
        self.assertEqual(result, expected_result)

        # (Int | String) | (String | Int)
        result = interpreter.eval(
            TypeUnionExpr(
                TypeUnionExpr(
                    TypeRefExpr(int_type_ref),
                    TypeRefExpr(string_type_ref),
                ),
                TypeUnionExpr(
                    TypeRefExpr(string_type_ref),
                    TypeRefExpr(int_type_ref),
                ),
            )
        )
        self.assertEqual(result, expected_result)
