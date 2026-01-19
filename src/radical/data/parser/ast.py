from dataclasses import dataclass

from radical.data.parser.position import Position
from typing import Any, Sequence, cast
import json
from enum import StrEnum


@dataclass(frozen=True)
class Node:
    position: Position

    def format(self, name: str | None = None, indent_level: int = 0) -> str:
        indent = " " * 4 * indent_level
        parts: list[str] = [indent]
        if name is not None:
            parts.append(f"{name}=")
        parts.append(f"{self.__class__.__name__[:-4]}(\n")

        field_lines: list[str] = []
        for field_name, field_value in self.__dict__.items():
            if field_value is None:
                continue
            if isinstance(field_value, Position):
                field_lines.append(
                    f"{indent}    {field_name}=({field_value.line}, {field_value.column})"
                )
            elif isinstance(field_value, Node):
                field_lines.append(
                    field_value.format(name=field_name, indent_level=indent_level + 1)
                )
            else:
                field_lines.append(
                    self.format_value(
                        field_value, name=field_name, indent_level=indent_level + 1
                    )
                )
        parts.append(",\n".join(field_lines))
        parts.append(f"\n{indent})")
        return "".join(parts)

    @staticmethod
    def format_value(value: Any, name: str | None = None, indent_level: int = 0) -> str:
        if isinstance(value, Node):
            return value.format(name=name, indent_level=indent_level)

        indent = " " * 4 * indent_level
        parts: list[str] = [indent]
        if name is not None:
            parts.append(f"{name}=")
        if isinstance(value, list):
            parts.append("[\n")
            element_lines: list[str] = []
            for element in cast(list[Any], value):
                element_lines.append(
                    Node.format_value(element, indent_level=indent_level + 1)
                )
            parts.append(",\n".join(element_lines))
            parts.append(f"\n{indent}]")
        else:
            parts.append(json.dumps(value))
        return "".join(parts)


# Types


@dataclass(frozen=True)
class TypeNameNode(Node):
    name: "SymbolNode"


@dataclass(frozen=True)
class StringLiteralTypeNode(Node):
    value: "StringNodeType"


@dataclass(frozen=True)
class NumberLiteralTypeNode(Node):
    value: "NumberNodeType"


@dataclass(frozen=True)
class UnionTypeNode(Node):
    left: "TypeExpressionNodeType"
    right: "TypeExpressionNodeType"


@dataclass(frozen=True)
class FunctionArgumentTypeNode(Node):
    name: "SymbolNode | None"
    type: "TypeExpressionNodeType"
    variadic: bool
    optional: bool
    implicit: bool


@dataclass(frozen=True)
class FunctionTypeNode(Node):
    argument_types: list[FunctionArgumentTypeNode]
    return_type: "TypeExpressionNodeType"


@dataclass(frozen=True)
class TypeOfExpressionNode(Node):
    value: "ValueExpressionNodeType"


@dataclass(frozen=True)
class TypeExpressionNode(Node):
    value: "ValueExpressionNodeType"


@dataclass(frozen=True)
class ParenthesizedTypeNode(Node):
    type: "TypeExpressionNodeType"


@dataclass(frozen=True)
class TupleTypeNode(Node):
    element_types: list["TypeExpressionNodeType"]


@dataclass(frozen=True)
class GenericTypeNode(Node):
    base_type: "TypeExpressionNodeType"
    type_arguments: list["TypeExpressionNodeType"]


TypeExpressionNodeType = (
    TypeNameNode
    | UnionTypeNode
    | FunctionTypeNode
    | TypeOfExpressionNode
    | TypeExpressionNode
    | ParenthesizedTypeNode
    | GenericTypeNode
    | TupleTypeNode
    | StringLiteralTypeNode
    | NumberLiteralTypeNode
    | FunctionTypeNode
)

# Scalars


@dataclass(frozen=True)
class SymbolNode(Node):
    name: str
    quoted: bool


@dataclass(frozen=True)
class TrueKeywordNode(Node):
    pass


@dataclass(frozen=True)
class FalseKeywordNode(Node):
    pass


@dataclass(frozen=True)
class NullKeywordNode(Node):
    pass


@dataclass(frozen=True)
class StringLiteralNode(Node):
    value: str


@dataclass(frozen=True)
class RawStringLiteralNode(Node):
    value: str


@dataclass(frozen=True)
class MultiLineStringLiteralNode(Node):
    value: str


@dataclass(frozen=True)
class RawMultiLineStringLiteralNode(Node):
    value: str


StringNodeType = (
    StringLiteralNode
    | RawStringLiteralNode
    | MultiLineStringLiteralNode
    | RawMultiLineStringLiteralNode
)


@dataclass(frozen=True)
class IntegerLiteralNode(Node):
    value: str


@dataclass(frozen=True)
class FloatLiteralNode(Node):
    value: str


@dataclass(frozen=True)
class SciFloatLiteralNode(Node):
    value: str


NumberNodeType = IntegerLiteralNode | FloatLiteralNode | SciFloatLiteralNode

# Operations


class UnaryOperator(StrEnum):
    PLUS = "+"
    MINUS = "-"
    NOT = "not"


class BinaryOperator(StrEnum):
    EXPONENTIATION = "**"
    MULTIPLY = "*"
    DIVIDE = "/"
    FLOOR_DIVIDE = "//"
    MODULO = "%"
    PLUS = "+"
    MINUS = "-"
    EQUAL = "=="
    NOT_EQUAL = "!="
    LESS_THAN = "<"
    LESS_THAN_EQUAL = "<="
    GREATER_THAN = ">"
    GREATER_THAN_EQUAL = ">="
    AND = "and"
    OR = "or"
    PIPE = "|>"


OPERATOR_PRECEDENCE: Sequence[Sequence[BinaryOperator | UnaryOperator]] = (
    (BinaryOperator.EXPONENTIATION,),
    (UnaryOperator.PLUS, UnaryOperator.MINUS),
    (
        BinaryOperator.MULTIPLY,
        BinaryOperator.DIVIDE,
        BinaryOperator.FLOOR_DIVIDE,
        BinaryOperator.MODULO,
    ),
    (
        BinaryOperator.PLUS,
        BinaryOperator.MINUS,
    ),
    (
        BinaryOperator.EQUAL,
        BinaryOperator.NOT_EQUAL,
        BinaryOperator.LESS_THAN,
        BinaryOperator.LESS_THAN_EQUAL,
        BinaryOperator.GREATER_THAN,
        BinaryOperator.GREATER_THAN_EQUAL,
    ),
    (UnaryOperator.NOT,),
    (BinaryOperator.AND,),
    (BinaryOperator.OR,),
    (BinaryOperator.PIPE,),
)


def precendence_of_unary_op(operator: UnaryOperator) -> int:
    for precedence, operators in enumerate(reversed(OPERATOR_PRECEDENCE), start=1):
        if operator in operators and precedence in (4, 8):
            return precedence
    raise ValueError(f"Unknown unary operator: {operator}")


def precedence_of_binary_op(operator: BinaryOperator) -> int:
    for precedence, operators in enumerate(reversed(OPERATOR_PRECEDENCE), start=1):
        if operator in operators and precedence not in (4, 8):
            return precedence
    raise ValueError(f"Unknown binary operator: {operator}")


class OperatorAssociativity(StrEnum):
    LEFT = "left"
    RIGHT = "right"


def associativity_of_binary_op(operator: BinaryOperator) -> OperatorAssociativity:
    return (
        OperatorAssociativity.RIGHT
        if operator == BinaryOperator.EXPONENTIATION
        else OperatorAssociativity.LEFT
    )


def associativity_of_unary_op(operator: UnaryOperator) -> OperatorAssociativity:
    return OperatorAssociativity.RIGHT


@dataclass(frozen=True)
class UnaryOperationNode(Node):
    operator: UnaryOperator
    operand: "ValueExpressionNodeType"


@dataclass(frozen=True)
class BinaryOperationNode(Node):
    left: "ValueExpressionNodeType"
    operator: BinaryOperator
    right: "ValueExpressionNodeType"


@dataclass(frozen=True)
class ParenthesizedExpressionNode(Node):
    expression: "ValueExpressionNodeType"


@dataclass(frozen=True)
class IndexAccessNode(Node):
    collection: "ValueExpressionNodeType"
    index: "ValueExpressionNodeType"


@dataclass(frozen=True)
class SliceAccessNode(Node):
    collection: "ValueExpressionNodeType"
    start: "ValueExpressionNodeType | None"
    end: "ValueExpressionNodeType | None"


@dataclass(frozen=True)
class AttributeAccessNode(Node):
    object: "ValueExpressionNodeType"
    attribute: SymbolNode


@dataclass(frozen=True)
class FunctionCallArgumentNode(Node):
    # TODO: variadic arguments
    name: SymbolNode | None
    value: "ValueExpressionNodeType"


@dataclass(frozen=True)
class FunctionCallNode(Node):
    function: "ValueExpressionNodeType"
    arguments: list[FunctionCallArgumentNode]


@dataclass(frozen=True)
class IfThenElseNode(Node):
    condition: "ValueExpressionNodeType"
    then_branch: "ValueExpressionNodeType"
    else_branch: "ValueExpressionNodeType"


# Variables


@dataclass(frozen=True)
class VariableBindingStatementNode(Node):
    name: SymbolNode
    value: "ValueExpressionNodeType"
    type: "TypeExpressionNodeType | None"


@dataclass(frozen=True)
class VariableTypeSignatureNode(Node):
    name: SymbolNode
    type: "TypeExpressionNodeType"


BindingStatementNodeType = VariableBindingStatementNode | VariableTypeSignatureNode


@dataclass(frozen=True)
class LetInNode(Node):
    bindings: list[BindingStatementNodeType]
    body: "ValueExpressionNodeType"


@dataclass(frozen=True)
class LetStatementNode(Node):
    binding: BindingStatementNodeType


# Collections


@dataclass(frozen=True)
class SpreadOperationNode(Node):
    collection: "ValueExpressionNodeType"


@dataclass(frozen=True)
class MapEntryNode(Node):
    key: "ValueExpressionNodeType"
    value: "ValueExpressionNodeType"
    expression_key: bool


@dataclass(frozen=True)
class TreeEntryNode(Node):
    key: "ValueExpressionNodeType"
    value: "ValueExpressionNodeType"
    expression_key: bool


@dataclass(frozen=True)
class ListLiteralNode(Node):
    elements: list["ValueExpressionNodeType | SpreadOperationNode"]


@dataclass(frozen=True)
class SetLiteralNode(Node):
    elements: list["ValueExpressionNodeType | SpreadOperationNode"]


@dataclass(frozen=True)
class MapLiteralNode(Node):
    entries: list["MapEntryNode | SpreadOperationNode"]


@dataclass(frozen=True)
class TreeLiteralNode(Node):
    entries: list["TreeEntryNode | SpreadOperationNode"]


@dataclass(frozen=True)
class TupleLiteralNode(Node):
    elements: list["ValueExpressionNodeType"]


@dataclass(frozen=True)
class ComprehensionGuardNode(Node):
    condition: "ValueExpressionNodeType"


@dataclass(frozen=True)
class ComprehensionBindingNode(Node):
    variables: list[SymbolNode]
    iterable: "ValueExpressionNodeType"


ComprehensionClauseNodeType = ComprehensionBindingNode | ComprehensionGuardNode


@dataclass(frozen=True)
class ListComprehensionNode(Node):
    element: "ValueExpressionNodeType"
    clauses: list[ComprehensionClauseNodeType]


@dataclass(frozen=True)
class SetComprehensionNode(Node):
    element: "ValueExpressionNodeType"
    clauses: list[ComprehensionClauseNodeType]


@dataclass(frozen=True)
class MapComprehensionNode(Node):
    entry: "MapEntryNode"
    clauses: list[ComprehensionClauseNodeType]


@dataclass(frozen=True)
class TreeComprehensionNode(Node):
    entry: "TreeEntryNode"
    clauses: list[ComprehensionClauseNodeType]


# TODO: raise, try-catch-then etc

ValueExpressionNodeType = (
    SymbolNode
    | TrueKeywordNode
    | FalseKeywordNode
    | NullKeywordNode
    | StringLiteralNode
    | RawStringLiteralNode
    | MultiLineStringLiteralNode
    | RawMultiLineStringLiteralNode
    | IntegerLiteralNode
    | FloatLiteralNode
    | SciFloatLiteralNode
    | UnaryOperationNode
    | BinaryOperationNode
    | ParenthesizedExpressionNode
    | IndexAccessNode
    | SliceAccessNode
    | AttributeAccessNode
    | FunctionCallNode
    | LetInNode
    | ListLiteralNode
    | SetLiteralNode
    | MapLiteralNode
    | TupleLiteralNode
    | ListComprehensionNode
    | SetComprehensionNode
    | MapComprehensionNode
    | TreeLiteralNode
    | TreeComprehensionNode
    | IfThenElseNode
)

CollectionElementNodeType = (
    ValueExpressionNodeType | SpreadOperationNode | MapEntryNode | TreeEntryNode
)

TopLevelDeclarationNodeType = BindingStatementNodeType


@dataclass(frozen=True)
class ModuleNode(Node):
    top_level_nodes: list[TopLevelDeclarationNodeType]
