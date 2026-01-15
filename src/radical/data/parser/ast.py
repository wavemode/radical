from dataclasses import dataclass

from radical.data.parser.position import Position
from typing import Any
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
            if field_name == "position" or field_value is None:
                continue
            if isinstance(field_value, Node):
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
            for element in value:
                element_lines.append(
                    Node.format_value(element, indent_level=indent_level + 1)
                )
            parts.append(",\n".join(element_lines))
            parts.append(f"\n{indent}]")
        else:
            parts.append(json.dumps(value))
        return "".join(parts)


# Scalars


@dataclass(frozen=True)
class SymbolNode(Node):
    name: str


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


@dataclass(frozen=True)
class IntegerLiteralNode(Node):
    value: str


@dataclass(frozen=True)
class FloatLiteralNode(Node):
    value: str


@dataclass(frozen=True)
class SciFloatLiteralNode(Node):
    value: str


# Operations


class UnaryOperator(StrEnum):
    PLUS = "+"
    MINUS = "-"
    NOT = "not"


@dataclass(frozen=True)
class UnaryOperationNode(Node):
    operator: UnaryOperator
    operand: "ValueExpressionNode"


class BinaryOperator(StrEnum):
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    FLOOR_DIVIDE = "//"
    MODULO = "%"
    EXPONENTIATION = "**"
    COLON = ":"
    PIPE = "|>"
    AND = "and"
    OR = "or"
    EQUAL = "=="
    NOT_EQUAL = "!="
    LESS_THAN = "<"
    LESS_THAN_EQUAL = "<="
    GREATER_THAN = ">"
    GREATER_THAN_EQUAL = ">="


@dataclass(frozen=True)
class BinaryOperationNode(Node):
    left: "ValueExpressionNode"
    operator: BinaryOperator
    right: "ValueExpressionNode"


@dataclass(frozen=True)
class IndexAccessNode(Node):
    collection: "ValueExpressionNode"
    index: "ValueExpressionNode"


@dataclass(frozen=True)
class SliceAccessNode(Node):
    collection: "ValueExpressionNode"
    start: "ValueExpressionNode | None"
    end: "ValueExpressionNode | None"


@dataclass(frozen=True)
class AttributeAccessNode(Node):
    object: "ValueExpressionNode"
    attribute: SymbolNode


@dataclass(frozen=True)
class FunctionCallArgumentNode(Node):
    name: SymbolNode | None
    value: "ValueExpressionNode"


@dataclass(frozen=True)
class FunctionCallNode(Node):
    function: "ValueExpressionNode"
    arguments: list[FunctionCallArgumentNode]


# Variables


@dataclass(frozen=True)
class VariableBindingStatementNode(Node):
    name: SymbolNode
    value: "ValueExpressionNode"
    type: "ValueExpressionNode | None"


@dataclass(frozen=True)
class LetInNode(Node):
    definitions: list[VariableBindingStatementNode]
    body: "ValueExpressionNode"


@dataclass(frozen=True)
class LetStatementNode(Node):
    definition: VariableBindingStatementNode


# Collections


@dataclass(frozen=True)
class ListLiteralNode(Node):
    elements: list["ValueExpressionNode"]


@dataclass(frozen=True)
class SetLiteralNode(Node):
    elements: list["ValueExpressionNode"]


@dataclass(frozen=True)
class MapLiteralNode(Node):
    entries: list[tuple["ValueExpressionNode", "ValueExpressionNode"]]


@dataclass(frozen=True)
class TupleLiteralNode(Node):
    elements: list["ValueExpressionNode"]


@dataclass(frozen=True)
class ComprehensionGuardNode(Node):
    condition: "ValueExpressionNode"


@dataclass(frozen=True)
class ComprehensionBindingNode(Node):
    variables: list[SymbolNode]
    iterable: "ValueExpressionNode"


ComprehensionClause = ComprehensionBindingNode | ComprehensionGuardNode


@dataclass(frozen=True)
class ListComprehensionNode(Node):
    element: "ValueExpressionNode"
    clauses: list[ComprehensionClause]


@dataclass(frozen=True)
class SetComprehensionNode(Node):
    element: "ValueExpressionNode"
    clauses: list[ComprehensionClause]


@dataclass(frozen=True)
class MapComprehensionNode(Node):
    key: "ValueExpressionNode"
    value: "ValueExpressionNode"
    clauses: list[ComprehensionClause]


# do block, if-then, raise, try-catch-then etc

ValueExpressionNode = (
    SymbolNode
    | StringLiteralNode
    | RawStringLiteralNode
    | MultiLineStringLiteralNode
    | RawMultiLineStringLiteralNode
    | IntegerLiteralNode
    | FloatLiteralNode
    | SciFloatLiteralNode
    | UnaryOperationNode
    | BinaryOperationNode
)


TopLevelDeclarationNode = VariableBindingStatementNode


@dataclass(frozen=True)
class ModuleNode(Node):
    top_level_nodes: list[TopLevelDeclarationNode]
