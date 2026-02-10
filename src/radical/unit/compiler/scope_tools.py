from radical.data.parser.ast import (
    AssignmentNode,
    AssignmentStatementNode,
    DataDeclarationNode,
    FunctionDeclarationNode,
    ImportStatementNode,
    LocalDeclarationNode,
    ModuleAssignmentDeclarationNode,
    ModuleBodyDeclarationNode,
    ModuleNameNode,
    NamingAssignmentNode,
    ProcedureDeclarationNode,
    TopLevelDeclarationNodeType,
    TypeAnnotationNode,
    TypeDeclarationNode,
)
from radical.data.parser.node import Node
from radical.unit.compiler.scope import Scope
from typing import assert_never


def populate_decls(scope: Scope, decls: list[TopLevelDeclarationNodeType]) -> None:
    for decl in decls:
        _populate_decl(scope, decl)


def _populate_decl(scope: Scope, decl: TopLevelDeclarationNodeType) -> None:
    name: str
    expr_node: Node | None = None
    type_node: Node | None = None
    is_value = False
    is_type = False
    match decl:
        case ImportStatementNode() | ModuleNameNode():
            # TODO: handle imports
            # TODO: handle module name constraint checking
            return
        case AssignmentStatementNode():
            is_value = True
            assignment = decl.assignment
            # TODO: not yet supporting destructing assignment
            assert isinstance(assignment, (AssignmentNode, NamingAssignmentNode))
            name = assignment.target.name.value
            expr_node = assignment.value
        case TypeAnnotationNode():
            is_value = True
            name = decl.name.name.value
            type_node = decl.type_expression
        case TypeDeclarationNode():
            is_type = True
            name = decl.name.name.value
            expr_node = decl
        case (
            DataDeclarationNode()
            | ModuleBodyDeclarationNode()
            | ModuleAssignmentDeclarationNode()
        ):
            is_value = True
            is_type = True
            name = decl.name.name.value
            expr_node = decl
        case FunctionDeclarationNode() | ProcedureDeclarationNode():
            is_value = True
            name = decl.name.name.value
            expr_node = decl
        case LocalDeclarationNode():
            _populate_decl(scope, decl.declaration)
            return
        case _:
            assert_never(decl)

    symbol_id = scope.intern_symbol(name)
    if is_value:
        result = scope.lookup_binding(symbol_id)
        if not result:
            result = scope.add_binding(name)
        result.value_node = expr_node
        result.type_annotation_node = type_node
    if is_type:
        result = scope.lookup_type_binding(symbol_id)
        if not result:
            result = scope.add_type_binding(name)
        result.value_node = expr_node
        result.type_annotation_node = type_node
