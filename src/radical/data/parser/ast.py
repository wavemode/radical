from dataclasses import dataclass

from radical.data.parser.position import Position
from typing import Any, cast
from radical.data.parser.token import Token
from enum import Enum
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
        elif isinstance(value, Operator):
            parts.append(f'"{value.value}"')
        else:
            parts.append(json.dumps(value))
        return "".join(parts)


# Type Expressions


@dataclass(frozen=True)
class TypeNameNode(Node):
    name: Token


@dataclass(frozen=True)
class ParenthesizedTypeExpressionNode(Node):
    expression: "TypeExpressionNodeType"


@dataclass(frozen=True)
class TupleTypeNode(Node):
    elements: list["TypeExpressionNodeType"]


@dataclass(frozen=True)
class TypeTypeExpressionNode(Node):
    expression: "ValueExpressionNodeType"


@dataclass(frozen=True)
class TypeOfTypeExpressionNode(Node):
    expression: "ValueExpressionNodeType"


@dataclass(frozen=True)
class ConstTypeExpressionNode(Node):
    expression: "ValueExpressionNodeType"


@dataclass(frozen=True)
class SpreadTypeExpressionNode(Node):
    expression: "TypeExpressionNodeType"


@dataclass(frozen=True)
class RecordTypeNode(Node):
    fields: list["TypeAnnotationNode | SpreadTypeExpressionNode"]


@dataclass(frozen=True)
class FunctionParameterNode(Node):
    name: "SymbolNode | None"
    optional: bool
    type_annotation: "TypeExpressionNodeType"


@dataclass(frozen=True)
class FunctionTypeNode(Node):
    parameters: list["FunctionParameterNode"]
    return_type: "TypeExpressionNodeType"


@dataclass(frozen=True)
class GenericTypeParameterNode(Node):
    name: "SymbolNode"
    constraint: "TypeExpressionNodeType | None"


@dataclass(frozen=True)
class GenericTypeExpressionNode(Node):
    parameters: list[GenericTypeParameterNode]
    expression: "TypeExpressionNodeType"


@dataclass(frozen=True)
class TypeUnionNode(Node):
    elements: list["TypeExpressionNodeType"]


@dataclass(frozen=True)
class GenericTypeApplicationNode(Node):
    generic_type: "TypeExpressionNodeType"
    arguments: list["TypeExpressionNodeType"]


# Literals


@dataclass(frozen=True)
class SymbolNode(Node):
    name: Token


@dataclass(frozen=True)
class StringLiteralNode(Node):
    open_quote: Token
    contents: Token
    close_quote: Token


@dataclass(frozen=True)
class FormatStringTextSectionNode(Node):
    string_contents: Token


@dataclass(frozen=True)
class FormatStringExpressionNode(Node):
    expression: "ValueExpressionNodeType"


@dataclass(frozen=True)
class FormatStringLiteralNode(Node):
    open_quote: Token
    contents: list[FormatStringTextSectionNode | FormatStringExpressionNode]
    close_quote: Token


@dataclass(frozen=True)
class NumberLiteralNode(Node):
    contents: Token


@dataclass(frozen=True)
class BooleanLiteralNode(Node):
    contents: Token


@dataclass(frozen=True)
class NullLiteralNode(Node):
    contents: Token


# Operations


class Operator(Enum):
    """
    Grouped by precedence level.

    Exponentiation is the only right-associative binary operator.
    """

    MODULE = "module"

    SPREAD = "..."

    EXPONENTIATION = "**"

    POSITIVE = "+x"
    NEGATIVE = "-x"

    MULTIPLY = "*"
    FLOOR_DIVIDE = "//"
    DIVIDE = "/"
    MODULO = "%"

    PLUS = "+"
    MINUS = "-"

    EQUAL = "=="
    NOT_EQUAL = "!="
    LESS_THAN_EQUAL = "<="
    GREATER_THAN_EQUAL = ">="
    LESS_THAN = "<"
    GREATER_THAN = ">"

    NOT = "not"

    AND = "and"

    OR = "or"

    PIPE = "|>"


@dataclass(frozen=True)
class BinaryOperationNode(Node):
    left: "ValueExpressionNodeType"
    operator: Operator
    right: "ValueExpressionNodeType"


@dataclass(frozen=True)
class UnaryOperationNode(Node):
    operator: Operator
    operand: "ValueExpressionNodeType"


@dataclass(frozen=True)
class SpreadOperationNode(Node):
    operand: "ValueExpressionNodeType"


# Compound Expressions


@dataclass(frozen=True)
class ListLiteralNode(Node):
    elements: list["ValueExpressionNodeType | SpreadOperationNode"]


@dataclass(frozen=True)
class ParenthesizedExpressionNode(Node):
    expression: "ValueExpressionNodeType"


@dataclass(frozen=True)
class TupleLiteralNode(Node):
    elements: list["ValueExpressionNodeType"]


@dataclass(frozen=True)
class IfExpressionNode(Node):
    condition: "ValueExpressionNodeType"
    then_branch: "ValueExpressionNodeType"
    else_branch: "ValueExpressionNodeType"


@dataclass(frozen=True)
class TypeApplicationExpressionNode(Node):
    value_expression: "ValueExpressionNodeType"
    type_arguments: list["TypeExpressionNodeType"]


@dataclass(frozen=True)
class FieldAccessExpressionNode(Node):
    object_expression: "ValueExpressionNodeType"
    field: SymbolNode


@dataclass(frozen=True)
class IndexingExpressionNode(Node):
    object_expression: "ValueExpressionNodeType"
    index_expression: "ValueExpressionNodeType"


@dataclass(frozen=True)
class LetExpressionNode(Node):
    declarations: list["LetExpressionDeclarationNodeType"]
    body: "ValueExpressionNodeType"


@dataclass(frozen=True)
class ModuleExpressionNode(Node):
    declarations: list["TopLevelDeclarationNodeType"]


# Declarations


@dataclass(frozen=True)
class AssignmentNode(Node):
    target: SymbolNode | None
    target_expr: "ValueExpressionNodeType | None"
    value: "ValueExpressionNodeType"
    type_annotation: "TypeExpressionNodeType | None"
    local: bool


@dataclass(frozen=True)
class TypeAnnotationNode(Node):
    name: SymbolNode | None
    name_expr: "ValueExpressionNodeType | None"
    type_annotation: "TypeExpressionNodeType"
    local: bool


@dataclass(frozen=True)
class ImportStatementEllipsisNode(Node):
    pass


@dataclass(frozen=True)
class ImportStatementFieldNode(Node):
    name: SymbolNode
    alias: SymbolNode | None


@dataclass(frozen=True)
class ImportStatementNode(Node):
    module_parts: list[SymbolNode] | None
    module_expr: "ValueExpressionNodeType | None"
    filename: StringLiteralNode | None
    filename_expr: "ValueExpressionNodeType | None"
    fields: list["ImportStatementFieldNode | ImportStatementEllipsisNode"] | None
    alias: SymbolNode | None


@dataclass(frozen=True)
class TypeDeclarationNode(Node):
    name: SymbolNode
    type_expression: "TypeExpressionNodeType"
    parameters: list[GenericTypeParameterNode] | None
    local: bool


@dataclass(frozen=True)
class DataFieldNode(Node):
    name: SymbolNode | None
    type_annotation: "TypeExpressionNodeType"
    default_value: "ValueExpressionNodeType | None"


@dataclass(frozen=True)
class DataDeclarationNode(Node):
    name: SymbolNode
    parameters: list[GenericTypeParameterNode] | None
    fields: list[DataFieldNode] | None
    local: bool


@dataclass(frozen=True)
class ModuleBodyDeclarationNode(Node):
    name: SymbolNode
    declarations: list["TopLevelDeclarationNodeType"]


@dataclass(frozen=True)
class ModuleAssignmentDeclarationNode(Node):
    name: SymbolNode
    value: "ValueExpressionNodeType"


# Top Level


@dataclass(frozen=True)
class SpreadAssignmentStatementNode(Node):
    value: "ValueExpressionNodeType"


@dataclass(frozen=True)
class ModuleNameNode(Node):
    name: SymbolNode
    type_annotation: "TypeExpressionNodeType | None"


@dataclass(frozen=True)
class ModuleNode(Node):
    declarations: list["TopLevelDeclarationNodeType"]


# Node Types

AtomNodeType = (
    SymbolNode
    | StringLiteralNode
    | FormatStringLiteralNode
    | NumberLiteralNode
    | BooleanLiteralNode
    | NullLiteralNode
    | ParenthesizedExpressionNode
    | TupleLiteralNode
    | ListLiteralNode
    | IfExpressionNode
    | LetExpressionNode
    | ModuleExpressionNode
)
ValueExpressionNodeType = (
    AtomNodeType
    | BinaryOperationNode
    | UnaryOperationNode
    | TypeApplicationExpressionNode
    | FieldAccessExpressionNode
    | IndexingExpressionNode
)
TypeExpressionNodeType = (
    TypeNameNode
    | ParenthesizedTypeExpressionNode
    | TupleTypeNode
    | TypeTypeExpressionNode
    | TypeOfTypeExpressionNode
    | ConstTypeExpressionNode
    | SpreadTypeExpressionNode
    | RecordTypeNode
    | FunctionTypeNode
    | GenericTypeExpressionNode
    | TypeUnionNode
    | GenericTypeApplicationNode
)
LetExpressionDeclarationNodeType = (
    AssignmentNode
    | TypeAnnotationNode
    | ImportStatementNode
    | TypeDeclarationNode
    | DataDeclarationNode
    | ModuleBodyDeclarationNode
    | ModuleAssignmentDeclarationNode
)

TopLevelDeclarationNodeType = (
    LetExpressionDeclarationNodeType | SpreadAssignmentStatementNode | ModuleNameNode
)
