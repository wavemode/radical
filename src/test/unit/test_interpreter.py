from unittest import TestCase

from radical.data.sema.expression import (
    AddExpr,
    LiteralExpr,
    TypeUnionExpr,
)
from radical.data.sema.type import UnionType
from radical.unit.compiler.analysis_scope import AnalysisScope
from radical.unit.sema.namespace import Namespace
from radical.unit.interp.interpreter import Interpreter
from radical.data.sema.value import Value
from radical.unit.interp.builtins import setup_builtins


class TestInterpreter(TestCase):
    maxDiff = None

    def setUp(self) -> None:
        self.namespace = Namespace()
        self.module_id = self.namespace.add_or_get_module("Test")
        self.scope = AnalysisScope(
            module_id=self.module_id,
            namespace=self.namespace,
            parent=None,
        )
        self.builtins = setup_builtins(self.scope)
        self.interpreter = Interpreter(self.namespace)

    def test_simple_expr(self) -> None:
        const_1 = LiteralExpr(self.builtins.int_type, Value(1))
        const_2 = LiteralExpr(self.builtins.int_type, Value(2))
        result = self.interpreter.eval(
            AddExpr(
                self.builtins.int_type,
                const_1,
                const_2,
            )
        )
        self.assertEqual(result, Value(3))

    def test_type_union_expr(self) -> None:
        # Int | String
        expected_result = Value(
            UnionType(types={self.builtins.int_type, self.builtins.string_type})
        )

        # Int | String
        result = self.interpreter.eval(
            TypeUnionExpr(
                self.builtins.type_type,
                LiteralExpr(self.builtins.type_type, Value(self.builtins.int_type)),
                LiteralExpr(self.builtins.type_type, Value(self.builtins.string_type)),
            )
        )
        self.assertEqual(result, expected_result)

        # String | Int
        result = self.interpreter.eval(
            TypeUnionExpr(
                self.builtins.type_type,
                LiteralExpr(self.builtins.type_type, Value(self.builtins.string_type)),
                LiteralExpr(self.builtins.type_type, Value(self.builtins.int_type)),
            )
        )
        self.assertEqual(result, expected_result)

        # (Int | String) | Int
        result = self.interpreter.eval(
            TypeUnionExpr(
                self.builtins.type_type,
                TypeUnionExpr(
                    self.builtins.type_type,
                    LiteralExpr(self.builtins.type_type, Value(self.builtins.int_type)),
                    LiteralExpr(
                        self.builtins.type_type, Value(self.builtins.string_type)
                    ),
                ),
                LiteralExpr(self.builtins.type_type, Value(self.builtins.int_type)),
            )
        )
        self.assertEqual(result, expected_result)

        # Int | (String | Int)
        result = self.interpreter.eval(
            TypeUnionExpr(
                self.builtins.type_type,
                LiteralExpr(self.builtins.type_type, Value(self.builtins.int_type)),
                TypeUnionExpr(
                    self.builtins.type_type,
                    LiteralExpr(
                        self.builtins.type_type, Value(self.builtins.string_type)
                    ),
                    LiteralExpr(self.builtins.type_type, Value(self.builtins.int_type)),
                ),
            )
        )
        self.assertEqual(result, expected_result)

        # (Int | String) | (String | Int)
        result = self.interpreter.eval(
            TypeUnionExpr(
                self.builtins.type_type,
                TypeUnionExpr(
                    self.builtins.type_type,
                    LiteralExpr(self.builtins.type_type, Value(self.builtins.int_type)),
                    LiteralExpr(
                        self.builtins.type_type, Value(self.builtins.string_type)
                    ),
                ),
                TypeUnionExpr(
                    self.builtins.type_type,
                    LiteralExpr(
                        self.builtins.type_type, Value(self.builtins.string_type)
                    ),
                    LiteralExpr(self.builtins.type_type, Value(self.builtins.int_type)),
                ),
            )
        )
        self.assertEqual(result, expected_result)
