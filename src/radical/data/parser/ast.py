from dataclasses import dataclass

from radical.data.parser.position import Position
from typing import Literal

@dataclass(frozen=True)
class Node:
    position: Position

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

UnaryOperator = Literal['+', '-', 'not']

@dataclass(frozen=True)
class UnaryOperationNode(Node):
    operator: UnaryOperator
    operand: 'ExpressionNode'

BinaryOperator = Literal[
    '+', '-', '*', '/', '//', '%', '**', ':'
    'and', 'or',
    '==', '!=', '<', '<=', '>', '>='
]
@dataclass(frozen=True)
class BinaryOperationNode(Node):
    left: 'ExpressionNode'
    operator: BinaryOperator
    right: 'ExpressionNode'

@dataclass(frozen=True)
class IndexAccessNode(Node):
    collection: 'ExpressionNode'
    index: 'ExpressionNode'

@dataclass(frozen=True)
class SliceAccessNode(Node):
    collection: 'ExpressionNode'
    start: 'ExpressionNode | None'
    end: 'ExpressionNode | None'

@dataclass(frozen=True)
class AttributeAccessNode(Node):
    object: 'ExpressionNode'
    attribute: SymbolNode

@dataclass(frozen=True)
class FunctionCallNode(Node):
    function: 'ExpressionNode'
    arguments: list['ExpressionNode']


# Variables

@dataclass(frozen=True)
class DefinitionNode(Node):
    name: SymbolNode
    value: 'ExpressionNode'
    type: 'ExpressionNode | None'

@dataclass(frozen=True)
class LetInNode(Node):
    definitions: list[DefinitionNode]
    body: 'ExpressionNode'

# Collections

@dataclass(frozen=True)
class ListLiteralNode(Node):
    elements: list['ExpressionNode']

@dataclass(frozen=True)
class SetLiteralNode(Node):
    elements: list['ExpressionNode']

@dataclass(frozen=True)
class MapLiteralNode(Node):
    entries: list[tuple['ExpressionNode', 'ExpressionNode']]

@dataclass(frozen=True)
class TupleLiteralNode(Node):
    elements: list['ExpressionNode']


@dataclass(frozen=True)
class ComprehensionGuardNode(Node):
    condition: 'ExpressionNode'

@dataclass(frozen=True)
class ComprehensionBindingNode(Node):
    variables: list[SymbolNode]
    iterable: 'ExpressionNode'

ComprehensionClause = (
    ComprehensionBindingNode
    | ComprehensionGuardNode
)

@dataclass(frozen=True)
class ListComprehensionNode(Node):
    element: 'ExpressionNode'
    clauses: list[ComprehensionClause]

@dataclass(frozen=True)
class SetComprehensionNode(Node):
    element: 'ExpressionNode'
    clauses: list[ComprehensionClause]

@dataclass(frozen=True)
class MapComprehensionNode(Node):
    key: 'ExpressionNode'
    value: 'ExpressionNode'
    clauses: list[ComprehensionClause]

# do block, if-then, raise, try-catch-then etc

ExpressionNode = (
    SymbolNode
    | StringLiteralNode
    | RawStringLiteralNode
    | MultiLineStringLiteralNode
    | RawMultiLineStringLiteralNode
)




TopLevelDeclarationNode = DefinitionNode


@dataclass(frozen=True)
class ModuleNode(Node):
    top_level_nodes: list[TopLevelDeclarationNode]
