from dataclasses import dataclass

from radical.data.parser.operator import Operator
from radical.data.parser.node import Node
from radical.data.parser.token import Token


# Type Expressions


@dataclass(frozen=True)
class TypeNameNode(Node):
    name: "SymbolNode"


@dataclass(frozen=True)
class PlaceholderTypeNode(Node):
    pass


@dataclass(frozen=True)
class ParenthesizedTypeExpressionNode(Node):
    expressions: list["TypeExpressionNodeType | SpreadTypeExpressionNode"]


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
class RecordTypeFieldNode(Node):
    name: "SymbolNode"
    optional: bool
    type_annotation: "TypeExpressionNodeType"


@dataclass(frozen=True)
class RecordTypeNode(Node):
    fields: list["RecordTypeFieldNode | SpreadTypeExpressionNode"]


@dataclass(frozen=True)
class FunctionTypeParameterNode(Node):
    name: "SymbolNode | None"
    variadic: bool
    optional: bool
    type_annotation: "TypeExpressionNodeType | SpreadTypeExpressionNode"


@dataclass(frozen=True)
class FunctionTypeNode(Node):
    parameters: list["FunctionTypeParameterNode"]
    return_type: "TypeExpressionNodeType"


@dataclass(frozen=True)
class ProcedureTypeNode(Node):
    parameters: list["FunctionTypeParameterNode"]
    return_type: "TypeExpressionNodeType"


@dataclass(frozen=True)
class GenericTypeParameterNode(Node):
    name: "SymbolNode"
    variadic: bool
    constraints: list["TypeExpressionNodeType"] | None


@dataclass(frozen=True)
class GenericTypeExpressionNode(Node):
    parameters: list[GenericTypeParameterNode]
    expression: "TypeExpressionNodeType"


@dataclass(frozen=True)
class TypeUnionNode(Node):
    elements: list["TypeExpressionNodeType"]


@dataclass(frozen=True)
class GenericTypeArgumentNode(Node):
    name: "SymbolNode | None"
    argument: "TypeExpressionNodeType"


@dataclass(frozen=True)
class GenericTypeApplicationNode(Node):
    generic_type: "TypeExpressionNodeType"
    arguments: list["GenericTypeArgumentNode | SpreadTypeExpressionNode"]


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
class RegexLiteralNode(Node):
    contents: Token


@dataclass(frozen=True)
class NumberLiteralNode(Node):
    contents: Token


@dataclass(frozen=True)
class BooleanLiteralNode(Node):
    contents: Token


@dataclass(frozen=True)
class NullLiteralNode(Node):
    contents: Token


# Binding


@dataclass(frozen=True)
class AssignmentNode(Node):
    target: SymbolNode
    value: "ValueExpressionNodeType"


@dataclass(frozen=True)
class NamingAssignmentNode(Node):
    name: SymbolNode
    value: "ValueExpressionNodeType"


@dataclass(frozen=True)
class DestructuringAssignmentNode(Node):
    pattern: "PatternNodeType"
    value: "ValueExpressionNodeType"


@dataclass(frozen=True)
class ShorthandAssignmentNode(Node):
    name: SymbolNode


@dataclass(frozen=True)
class MappingAssignmentNode(Node):
    key: "ValueExpressionNodeType"
    value: "ValueExpressionNodeType"


@dataclass(frozen=True)
class SpreadAssignmentNode(Node):
    expression: "ValueExpressionNodeType"


# Operations


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
class TypeAnnotationExpressionNode(Node):
    value_expression: "ValueExpressionNodeType"
    type_expression: "TypeExpressionNodeType"


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
class FunctionCallExpressionNode(Node):
    function_expression: "ValueExpressionNodeType"
    arguments: list["FunctionCallArgumentNodeType"]


@dataclass(frozen=True)
class PlaceholderExpressionNode(Node):
    expression: "ValueExpressionNodeType"


# Compound Expressions


@dataclass(frozen=True)
class ListLiteralNode(Node):
    elements: list["ListLiteralElementNodeType"]


@dataclass(frozen=True)
class RecordLiteralNode(Node):
    entries: list["RecordLiteralEntryNodeType"]


@dataclass(frozen=True)
class ParenthesizedExpressionNode(Node):
    elements: list["ValueExpressionNodeType"]


@dataclass(frozen=True)
class IfExpressionNode(Node):
    condition: "ValueExpressionNodeType"
    then_branch: "ValueExpressionNodeType"
    else_branch: "ValueExpressionNodeType"


@dataclass(frozen=True)
class LetExpressionNode(Node):
    declarations: list["LetExpressionDeclarationNodeType"]
    body: "ValueExpressionNodeType"


@dataclass(frozen=True)
class CaseBranchNode(Node):
    pattern: "PatternNodeType"
    expression: "ValueExpressionNodeType"


@dataclass(frozen=True)
class CaseExpressionNode(Node):
    expression: "ValueExpressionNodeType"
    branches: list["CaseBranchNode"]


@dataclass(frozen=True)
class FunctionExpressionNode(Node):
    parameters: list["FunctionParameterNode"]
    generic_parameters: list["GenericTypeParameterNode"] | None
    body: "ValueExpressionNodeType"


@dataclass(frozen=True)
class ProcedureExpressionNode(Node):
    parameters: list["FunctionParameterNode"]
    generic_parameters: list["GenericTypeParameterNode"] | None
    body: list["ProcedureBodyStatementNode"]


@dataclass(frozen=True)
class ModuleBodyNode(Node):
    name: SymbolNode | None
    declarations: list["TopLevelDeclarationNodeType"]


@dataclass(frozen=True)
class ModuleExpressionNode(Node):
    body: ModuleBodyNode


# Patterns


@dataclass(frozen=True)
class SymbolPatternNode(Node):
    symbol: SymbolNode


@dataclass(frozen=True)
class RestPatternNode(Node):
    name: SymbolNode | None


@dataclass(frozen=True)
class ParenthesizedPatternNode(Node):
    elements: list["PatternNodeType"]


@dataclass(frozen=True)
class ListPatternNode(Node):
    elements: list["PatternNodeType"]


@dataclass(frozen=True)
class NumberLiteralPatternNode(Node):
    number: NumberLiteralNode


@dataclass(frozen=True)
class StringLiteralPatternNode(Node):
    string: StringLiteralNode


@dataclass(frozen=True)
class RegexLiteralPatternNode(Node):
    regex: RegexLiteralNode


@dataclass(frozen=True)
class FormatStringTextSectionPatternNode(Node):
    string_contents: Token


@dataclass(frozen=True)
class FormatStringExpressionPatternNode(Node):
    pattern: "PatternNodeType"


@dataclass(frozen=True)
class FormatStringPatternDirectionIndicatorNode(Node):
    direction: Token


@dataclass(frozen=True)
class FormatStringLiteralPatternNode(Node):
    open_quote: Token
    contents: list["FormatStringPatternPartNodeType"]
    close_quote: Token


@dataclass(frozen=True)
class NullLiteralPatternNode(Node):
    null: NullLiteralNode


@dataclass(frozen=True)
class BooleanLiteralPatternNode(Node):
    boolean: BooleanLiteralNode


@dataclass(frozen=True)
class ConstPatternNode(Node):
    value: "ValueExpressionNodeType"


@dataclass(frozen=True)
class KeyValueFieldPatternNode(Node):
    name: SymbolNode | None
    pattern: "PatternNodeType"


@dataclass(frozen=True)
class DataTypePatternNode(Node):
    name: SymbolNode
    fields: list["KeyValueFieldPatternNode"] | None


@dataclass(frozen=True)
class RecordPatternNode(Node):
    fields: list[KeyValueFieldPatternNode]


@dataclass(frozen=True)
class PatternGuardNode(Node):
    pattern: "PatternNodeType"
    condition: "ValueExpressionNodeType"


@dataclass(frozen=True)
class PatternAliasNode(Node):
    pattern: "PatternNodeType"
    alias: SymbolNode


@dataclass(frozen=True)
class TypeMatchPatternNode(Node):
    pattern: "PatternNodeType"
    type_expression: "TypeExpressionNodeType"


# Declarations


@dataclass(frozen=True)
class LocalDeclarationNode(Node):
    declaration: "LetExpressionDeclarationNodeType"


@dataclass(frozen=True)
class AssignmentStatementNode(Node):
    assignment: "AssignmentBindingNodeType"


@dataclass(frozen=True)
class TypeAnnotationNode(Node):
    name: SymbolNode
    type_expression: "TypeExpressionNodeType"


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
    fields: list["ImportStatementFieldNode | ImportStatementEllipsisNode"] | None
    alias: SymbolNode | None


@dataclass(frozen=True)
class TypeDeclarationNode(Node):
    name: SymbolNode
    type_expression: "TypeExpressionNodeType"
    parameters: list[GenericTypeParameterNode] | None


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


@dataclass(frozen=True)
class ModuleBodyDeclarationNode(Node):
    name: SymbolNode
    body: ModuleBodyNode


@dataclass(frozen=True)
class ModuleAssignmentDeclarationNode(Node):
    name: SymbolNode
    value: "ValueExpressionNodeType"


@dataclass(frozen=True)
class FunctionParameterNode(Node):
    param: "PatternNodeType"
    variadic: bool
    type_annotation: "TypeExpressionNodeType | PlaceholderTypeNode | None"
    default_value: "ValueExpressionNodeType | None"


@dataclass(frozen=True)
class FunctionDeclarationNode(Node):
    name: SymbolNode
    parameters: list["FunctionParameterNode"]
    generic_parameters: list["GenericTypeParameterNode"] | None
    return_type: "TypeExpressionNodeType | PlaceholderTypeNode | None"
    body: "ValueExpressionNodeType"


@dataclass(frozen=True)
class ProcedureBodyStatementNode(Node):
    declaration: LocalDeclarationNode | None
    expression: "ValueExpressionNodeType | None"


@dataclass(frozen=True)
class ProcedureDeclarationNode(Node):
    name: SymbolNode
    parameters: list["FunctionParameterNode"]
    generic_parameters: list["GenericTypeParameterNode"] | None
    return_type: "TypeExpressionNodeType | PlaceholderTypeNode | None"
    body: list[ProcedureBodyStatementNode]


# Top Level


@dataclass(frozen=True)
class ModuleNameNode(Node):
    name: SymbolNode
    type_annotation: "TypeExpressionNodeType | None"


@dataclass(frozen=True)
class ModuleNode(Node):
    body: ModuleBodyNode


# Node Types

AtomNodeType = (
    SymbolNode
    | StringLiteralNode
    | FormatStringLiteralNode
    | RegexLiteralNode
    | NumberLiteralNode
    | BooleanLiteralNode
    | NullLiteralNode
    | ParenthesizedExpressionNode
    | ListLiteralNode
    | RecordLiteralNode
    | IfExpressionNode
    | CaseExpressionNode
    | LetExpressionNode
    | FunctionExpressionNode
    | ProcedureExpressionNode
    | ModuleExpressionNode
    | PlaceholderExpressionNode
)
ValueExpressionNodeType = (
    AtomNodeType
    | BinaryOperationNode
    | UnaryOperationNode
    | TypeAnnotationExpressionNode
    | TypeApplicationExpressionNode
    | FieldAccessExpressionNode
    | IndexingExpressionNode
    | FunctionCallExpressionNode
)
PatternAtomNodeType = (
    SymbolPatternNode
    | DataTypePatternNode
    | RecordPatternNode
    | RestPatternNode
    | ParenthesizedPatternNode
    | ListPatternNode
    | NumberLiteralPatternNode
    | StringLiteralPatternNode
    | RegexLiteralPatternNode
    | FormatStringLiteralPatternNode
    | NullLiteralPatternNode
    | BooleanLiteralPatternNode
    | ConstPatternNode
)
FormatStringPatternPartNodeType = (
    FormatStringTextSectionPatternNode
    | FormatStringExpressionPatternNode
    | FormatStringPatternDirectionIndicatorNode
)
PatternNodeType = (
    PatternAtomNodeType | PatternGuardNode | PatternAliasNode | TypeMatchPatternNode
)
TypeExpressionNodeType = (
    TypeNameNode
    | ParenthesizedTypeExpressionNode
    | TypeTypeExpressionNode
    | TypeOfTypeExpressionNode
    | ConstTypeExpressionNode
    | RecordTypeNode
    | FunctionTypeNode
    | ProcedureTypeNode
    | GenericTypeExpressionNode
    | TypeUnionNode
    | GenericTypeApplicationNode
)
LetExpressionDeclarationNodeType = (
    AssignmentStatementNode
    | TypeAnnotationNode
    | ImportStatementNode
    | TypeDeclarationNode
    | DataDeclarationNode
    | ModuleBodyDeclarationNode
    | ModuleAssignmentDeclarationNode
    | FunctionDeclarationNode
    | ProcedureDeclarationNode
)
FunctionCallArgumentNodeType = (
    AssignmentNode
    | NamingAssignmentNode
    | SpreadAssignmentNode
    | ValueExpressionNodeType
)
RecordLiteralEntryNodeType = (
    AssignmentNode
    | NamingAssignmentNode
    | ShorthandAssignmentNode
    | MappingAssignmentNode
    | SpreadAssignmentNode
)
AssignmentBindingNodeType = (
    AssignmentNode | NamingAssignmentNode | DestructuringAssignmentNode
)
RecordTypeEntryNodeType = RecordTypeFieldNode | SpreadTypeExpressionNode
ListLiteralElementNodeType = ValueExpressionNodeType | SpreadAssignmentNode
TopLevelDeclarationNodeType = (
    LetExpressionDeclarationNodeType | ModuleNameNode | LocalDeclarationNode
)
