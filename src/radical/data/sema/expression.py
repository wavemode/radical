from dataclasses import dataclass

from radical.data.core.data import Data
from radical.data.sema.constref import ConstRef
from radical.data.sema.type import Type
from radical.data.sema.typeref import TypeRef


@dataclass(frozen=True)
class Expression(Data):
    pass


@dataclass(frozen=True)
class AddIntExpr(Expression):
    left: "ExpressionType"
    right: "ExpressionType"


@dataclass(frozen=True)
class ConstRefExpr(Expression):
    type: Type
    ref: ConstRef


@dataclass(frozen=True)
class BoolLiteralExpr(Expression):
    value: bool


@dataclass(frozen=True)
class NullLiteralExpr(Expression):
    pass


@dataclass(frozen=True)
class IntLiteralExpr(Expression):
    value: int


@dataclass(frozen=True)
class FloatLiteralExpr(Expression):
    value: float


@dataclass(frozen=True)
class TypeUnionExpr(Expression):
    left: "ExpressionType"
    right: "ExpressionType"


@dataclass(frozen=True)
class TypeRefExpr(Expression):
    ref: TypeRef


ValueExpressionType = (
    NullLiteralExpr
    | BoolLiteralExpr
    | IntLiteralExpr
    | FloatLiteralExpr
    | ConstRefExpr
    | AddIntExpr
)
TypeExpressionType = TypeRefExpr | TypeUnionExpr
ExpressionType = ValueExpressionType | TypeExpressionType
