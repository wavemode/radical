from dataclasses import dataclass

from radical.data.core.data import Data
from radical.data.parser.node import Node
from radical.data.sema.type import Type
from radical.data.sema.value import Value


@dataclass(frozen=True)
class Expression(Data):
    type: Type
    node: Node | None

    def format_field(self, name: str, indent_level: int = 0) -> str | None:
        if name != "node":
            return super().format_field(name, indent_level)


@dataclass(frozen=True)
class LiteralExpr(Expression):
    value: Value


@dataclass(frozen=True)
class LocalVarExpr(Expression):
    symbol_id: int


@dataclass(frozen=True)
class AddExpr(Expression):
    left: "ExpressionType"
    right: "ExpressionType"


@dataclass(frozen=True)
class TypeUnionExpr(Expression):
    left: "ExpressionType"
    right: "ExpressionType"


ValueExpressionType = LiteralExpr | AddExpr | LocalVarExpr
TypeExpressionType = LiteralExpr | TypeUnionExpr
ExpressionType = ValueExpressionType | TypeExpressionType
