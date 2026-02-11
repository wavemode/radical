from dataclasses import dataclass

from radical.data.core.data import Data
from radical.data.parser.node import Node
from radical.data.sema.type import Type
from radical.data.sema.value import Value


@dataclass(frozen=True)
class Expression(Data):
    type: Type
    node: Node

    def format_field(self, name: str, indent_level: int = 0) -> str | None:
        if name != "node":
            return super().format_field(name, indent_level)


@dataclass(frozen=True)
class LiteralExpr(Expression):
    value: Value


@dataclass(frozen=True)
class LocalVarExpr(Expression):
    symbol_id: int


# Type Conversions


@dataclass(frozen=True)
class ToFloatExpr(Expression):
    operand: "ExpressionType"


@dataclass(frozen=True)
class ToRationalExpr(Expression):
    operand: "ExpressionType"


# Unary Ops


@dataclass(frozen=True)
class NegativeExpr(Expression):
    operand: "ExpressionType"


@dataclass(frozen=True)
class NotExpr(Expression):
    operand: "ExpressionType"


# Binary Ops


@dataclass(frozen=True)
class ExponentiationExpr(Expression):
    left: "ExpressionType"
    right: "ExpressionType"


@dataclass(frozen=True)
class MultiplyExpr(Expression):
    left: "ExpressionType"
    right: "ExpressionType"


@dataclass(frozen=True)
class FloorDivideExpr(Expression):
    left: "ExpressionType"
    right: "ExpressionType"


@dataclass(frozen=True)
class DivideExpr(Expression):
    left: "ExpressionType"
    right: "ExpressionType"


@dataclass(frozen=True)
class ModuloExpr(Expression):
    left: "ExpressionType"
    right: "ExpressionType"


@dataclass(frozen=True)
class AddExpr(Expression):
    left: "ExpressionType"
    right: "ExpressionType"


@dataclass(frozen=True)
class SubExpr(Expression):
    left: "ExpressionType"
    right: "ExpressionType"


@dataclass(frozen=True)
class EqualExpr(Expression):
    left: "ExpressionType"
    right: "ExpressionType"


@dataclass(frozen=True)
class NotEqualExpr(Expression):
    left: "ExpressionType"
    right: "ExpressionType"


@dataclass(frozen=True)
class LessThanEqualExpr(Expression):
    left: "ExpressionType"
    right: "ExpressionType"


@dataclass(frozen=True)
class GreaterThanEqualExpr(Expression):
    left: "ExpressionType"
    right: "ExpressionType"


@dataclass(frozen=True)
class LessThanExpr(Expression):
    left: "ExpressionType"
    right: "ExpressionType"


@dataclass(frozen=True)
class GreaterThanExpr(Expression):
    left: "ExpressionType"
    right: "ExpressionType"


@dataclass(frozen=True)
class AndExpr(Expression):
    left: "ExpressionType"
    right: "ExpressionType"


@dataclass(frozen=True)
class OrExpr(Expression):
    left: "ExpressionType"
    right: "ExpressionType"


# Type Expressions


@dataclass(frozen=True)
class TypeUnionExpr(Expression):
    left: "ExpressionType"
    right: "ExpressionType"


ValueExpressionType = (
    LiteralExpr
    | LocalVarExpr
    | ToFloatExpr
    | ToRationalExpr
    | NotExpr
    | NegativeExpr
    | ExponentiationExpr
    | MultiplyExpr
    | FloorDivideExpr
    | DivideExpr
    | ModuloExpr
    | AddExpr
    | SubExpr
    | EqualExpr
    | NotEqualExpr
    | LessThanEqualExpr
    | GreaterThanEqualExpr
    | LessThanExpr
    | GreaterThanExpr
    | AndExpr
    | OrExpr
)
TypeExpressionType = LiteralExpr | TypeUnionExpr
ExpressionType = ValueExpressionType | TypeExpressionType
