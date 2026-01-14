from dataclasses import dataclass

from radical.data.parser.position import Position
from typing import Literal, Any
import json


@dataclass(frozen=True)
class Node:
    position: Position

    def format(self, name: str | None = None, indent_level: int = 0) -> str:
        parts: list[str] = []
        indent = " " * 4 * indent_level
        if name is not None:
            parts.append(f"{indent}{name}=")
        else:
            parts.append(f"{indent}")
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
        parts: list[str] = []
        indent = " " * 4 * indent_level
        if name is not None:
            parts.append(f"{indent}{name}=")
        else:
            parts.append(f"{indent}")
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


@dataclass(frozen=True)
class NullLiteralNode(Node):
    pass


@dataclass(frozen=True)
class BooleanLiteralNode(Node):
    value: bool


# Operations

UnaryOperator = Literal["+", "-", "not"]


@dataclass(frozen=True)
class UnaryOperationNode(Node):
    operator: UnaryOperator
    operand: "ValueExpressionNode"


BinaryOperator = Literal[
    "+",
    "-",
    "*",
    "/",
    "//",
    "%",
    "**",
    ":",
    "|>",
    "and",
    "or",
    "==",
    "!=",
    "<",
    "<=",
    ">",
    ">=",
]


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
class FunctionCallNode(Node):
    function: "ValueExpressionNode"
    arguments: list["ValueExpressionNode"]


# Variables


@dataclass(frozen=True)
class VariableBindingNode(Node):
    name: SymbolNode
    value: "ValueExpressionNode"
    type: "ValueExpressionNode | None"


@dataclass(frozen=True)
class LetInNode(Node):
    definitions: list[VariableBindingNode]
    body: "ValueExpressionNode"


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
)


TopLevelDeclarationNode = VariableBindingNode


@dataclass(frozen=True)
class ModuleNode(Node):
    top_level_nodes: list[TopLevelDeclarationNode]

    def format(self, name: str | None = None, indent_level: int = 0) -> str:
        definition_lines: list[str] = []
        indent = " " * 4 * indent_level
        for node in self.top_level_nodes:
            definition_lines.append(node.format(indent_level=indent_level + 1))
        return f"{indent}Module(\n" + ",\n".join(definition_lines) + f"\n{indent})"
