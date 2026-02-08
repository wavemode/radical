from dataclasses import dataclass

from radical.data.core.data import Data
from radical.data.sema.constref import ConstRef
from radical.data.sema.typeref import TypeRef


@dataclass(frozen=True)
class AddIntExpr(Data):
    left: "ExpressionType"
    right: "ExpressionType"


@dataclass(frozen=True)
class ConstExpr(Data):
    type: TypeRef
    ref: ConstRef


ExpressionType = AddIntExpr | ConstExpr
