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
from radical.unit.compiler.analysis_scope import AnalysisScope
from typing import assert_never


def extract_decls(
    scope: AnalysisScope, decls: list[TopLevelDeclarationNodeType]
) -> None:
    for decl in decls:
        _populate_decl(scope, decl)


def _populate_decl(scope: AnalysisScope, decl: TopLevelDeclarationNodeType) -> None:
    name: str
    is_value = False
    is_type = False
    if isinstance(decl, (ImportStatementNode, ModuleNameNode)):
        return
    elif isinstance(decl, AssignmentStatementNode):
        is_value = True
        assignment = decl.assignment
        # TODO: not yet supporting destructing assignment
        assert isinstance(assignment, (AssignmentNode, NamingAssignmentNode))
        name = assignment.target.name.value
    elif isinstance(decl, TypeAnnotationNode):
        is_value = True
        name = decl.name.name.value
    elif isinstance(decl, TypeDeclarationNode):
        is_type = True
        name = decl.name.name.value
    elif isinstance(
        decl,
        (
            DataDeclarationNode,
            ModuleBodyDeclarationNode,
            ModuleAssignmentDeclarationNode,
        ),
    ):
        is_value = True
        is_type = True
        name = decl.name.name.value
    elif isinstance(decl, (FunctionDeclarationNode, ProcedureDeclarationNode)):
        is_value = True
        name = decl.name.name.value
    elif isinstance(decl, LocalDeclarationNode):
        _populate_decl(scope, decl.declaration)
        return
    else:
        assert_never(decl)

    symbol_ref = scope.intern_symbol(name)
    if is_value:
        scope.add_binding(symbol_ref)
    if is_type:
        scope.add_type_binding(symbol_ref)
