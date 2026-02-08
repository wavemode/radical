from dataclasses import dataclass

from radical.data.core.data import Data
from radical.data.sema.constref import ConstRef
from radical.data.sema.type import Type
from radical.data.sema.typeref import TypeRef


@dataclass(frozen=True)
class AddIntExpr(Data):
    left: "ExpressionType"
    right: "ExpressionType"


@dataclass(frozen=True)
class ConstRefExpr(Data):
    type: Type
    ref: ConstRef


@dataclass(frozen=True)
class TypeUnionExpr(Data):
    left: "ExpressionType"
    right: "ExpressionType"


@dataclass(frozen=True)
class TypeRefExpr(Data):
    ref: TypeRef


ExpressionType = AddIntExpr | ConstRefExpr | TypeUnionExpr | TypeRefExpr
