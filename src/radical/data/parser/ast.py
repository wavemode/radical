from dataclasses import dataclass

from radical.data.parser.position import Position
from typing import Any, cast
from radical.data.parser.token import Token
import json


@dataclass(frozen=True)
class Node:
    position: Position

    def __str__(self) -> str:
        return self.format()

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
                    f"{indent}    {field_name}=({field_value.line}, {field_value.column}, {field_value.indent_level})"
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
        elif isinstance(value, Token):
            parts.append(json.dumps(value.value))
        else:
            parts.append(json.dumps(value))
        return "".join(parts)


# Literals


@dataclass(frozen=True)
class SymbolNode(Node):
    name: Token


@dataclass(frozen=True)
class StringLiteralNode(Node):
    contents: Token


# Declarations


@dataclass(frozen=True)
class AssignmentNode(Node):
    target: SymbolNode
    value: "ValueExpressionNodeType"


# Top Level


@dataclass(frozen=True)
class ModuleNode(Node):
    declarations: list["TopLevelDeclarationNodeType"]


# Node Types

ValueExpressionNodeType = SymbolNode | StringLiteralNode

TopLevelDeclarationNodeType = AssignmentNode
