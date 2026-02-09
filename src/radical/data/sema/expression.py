from dataclasses import dataclass

from radical.data.core.data import Data
from radical.data.sema.type import Type
from radical.data.sema.value import Value


@dataclass(frozen=True)
class Expression(Data):
    type: Type


@dataclass(frozen=True)
class LiteralExpr(Expression):
    value: Value


@dataclass(frozen=True)
class AddExpr(Expression):
    left: "ExpressionType"
    right: "ExpressionType"


@dataclass(frozen=True)
class TypeUnionExpr(Expression):
    left: "ExpressionType"
    right: "ExpressionType"


ValueExpressionType = LiteralExpr | AddExpr
TypeExpressionType = LiteralExpr | TypeUnionExpr
ExpressionType = ValueExpressionType | TypeExpressionType
