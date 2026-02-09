from typing import Callable, NoReturn, TypeVar
from radical.data.parser.operator import Operator
from radical.data.parser.node import Node
from radical.data.parser.ast import (
    AssignmentBindingNodeType,
    AssignmentNode,
    AssignmentStatementNode,
    BooleanLiteralNode,
    BooleanLiteralPatternNode,
    CaseBranchNode,
    CaseExpressionNode,
    ConstPatternNode,
    ConstTypeExpressionNode,
    DataDeclarationNode,
    DataFieldNode,
    DestructuringAssignmentNode,
    FormatStringExpressionPatternNode,
    FormatStringLiteralPatternNode,
    FormatStringPatternDirectionIndicatorNode,
    FormatStringPatternPartNodeType,
    FormatStringTextSectionPatternNode,
    FunctionCallArgumentNodeType,
    GenericTypeArgumentNode,
    KeyValueFieldPatternNode,
    DataTypePatternNode,
    FieldAccessExpressionNode,
    FormatStringExpressionNode,
    FormatStringLiteralNode,
    FormatStringTextSectionNode,
    FunctionCallExpressionNode,
    FunctionDeclarationNode,
    FunctionExpressionNode,
    FunctionParameterNode,
    FunctionTypeParameterNode,
    FunctionTypeNode,
    GenericTypeApplicationNode,
    GenericTypeExpressionNode,
    GenericTypeParameterNode,
    IfExpressionNode,
    ImportStatementEllipsisNode,
    ImportStatementFieldNode,
    ImportStatementNode,
    IndexingExpressionNode,
    LetExpressionDeclarationNodeType,
    LetExpressionNode,
    ListLiteralElementNodeType,
    ListLiteralNode,
    ListPatternNode,
    LocalDeclarationNode,
    MappingAssignmentNode,
    NamingAssignmentNode,
    NullLiteralPatternNode,
    NumberLiteralPatternNode,
    PatternAliasNode,
    RecordLiteralEntryNodeType,
    RecordLiteralNode,
    ModuleAssignmentDeclarationNode,
    ModuleBodyDeclarationNode,
    ModuleBodyNode,
    ModuleExpressionNode,
    ModuleNameNode,
    ModuleNode,
    NullLiteralNode,
    NumberLiteralNode,
    ParenthesizedExpressionNode,
    ParenthesizedPatternNode,
    ParenthesizedTypeExpressionNode,
    PatternAtomNodeType,
    PatternGuardNode,
    PatternNodeType,
    PlaceholderExpressionNode,
    PlaceholderTypeNode,
    ProcedureBodyStatementNode,
    ProcedureDeclarationNode,
    ProcedureExpressionNode,
    ProcedureTypeNode,
    RecordPatternNode,
    RecordTypeEntryNodeType,
    RecordTypeFieldNode,
    RecordTypeNode,
    RegexLiteralNode,
    RegexLiteralPatternNode,
    RestPatternNode,
    ShorthandAssignmentNode,
    SpreadAssignmentNode,
    SpreadTypeExpressionNode,
    StringLiteralNode,
    StringLiteralPatternNode,
    SymbolNode,
    SymbolPatternNode,
    TopLevelDeclarationNodeType,
    TypeAnnotationNode,
    TypeApplicationExpressionNode,
    TypeAnnotationExpressionNode,
    TypeDeclarationNode,
    TypeMatchPatternNode,
    TypeOfTypeExpressionNode,
    TypeTypeExpressionNode,
    TypeExpressionNodeType,
    TypeNameNode,
    TypeUnionNode,
    UnaryOperationNode,
    ValueExpressionNodeType,
    AtomNodeType,
    BinaryOperationNode,
)
from radical.data.parser.errors import ParseError
from radical.data.parser.position import Position
from radical.data.parser.token import EXPR_START_TOKENS, Token, TokenType
from radical.unit.parser.lexer import Lexer
from radical.util.core.unit import Unit

T = TypeVar("T")


class Parser(Unit):
    def __init__(self, lexer: Lexer, filename: str):
        self._lexer = lexer
        self._filename = filename
        self._position = self._lexer.peek().position
        self._placeholder_stack: list[Position] = []
        self._atom_parsers: list[Callable[[], AtomNodeType | None]] = [
            self.parse_parenthesized_expression,
            self.parse_null_literal,
            self.parse_boolean_literal,
            self.parse_tilde_literal,
            self.parse_number_literal,
            self.parse_string_literal,
            self.parse_regex_literal,
            self.parse_format_string_literal,
            self.parse_symbol,
            self.parse_list_literal,
            self.parse_record_literal,
            self.parse_if_expression,
            self.parse_case_expression,
            self.parse_let_expression,
            self.parse_function_expression,
            self.parse_procedure_expression,
            self.parse_module_expression,
        ]

        self._pattern_atom_parsers: list[Callable[[], PatternAtomNodeType | None]] = [
            self.parse_data_type_pattern,
            self.parse_record_pattern,
            self.parse_parenthesized_pattern,
            self.parse_list_pattern,
            self.parse_number_literal_pattern,
            self.parse_string_literal_pattern,
            self.parse_regex_literal_pattern,
            self.parse_format_string_literal_pattern,
            self.parse_null_literal_pattern,
            self.parse_boolean_literal_pattern,
            self.parse_const_pattern,
            self.parse_rest_pattern,
            self.parse_symbol_pattern,
        ]

        self._type_atom_parsers: list[Callable[[], TypeExpressionNodeType | None]] = [
            self.parse_type_name,
            self.parse_parenthesized_type_expression,
            self.parse_type_type_expression,
            self.parse_typeof_type_expression,
            self.parse_const_type_expression,
            self.parse_record_type,
            self.parse_function_type,
            self.parse_procedure_type,
        ]

        self._let_expression_declaration_parsers: list[
            Callable[[], LetExpressionDeclarationNodeType | None]
        ] = [
            self.parse_function_declaration,
            self.parse_procedure_declaration,
            self.parse_data_declaration,
            self.parse_type_declaration,
            self.parse_import_statement,
            self.parse_module_assignment_declaration,
            self.parse_module_body_declaration,
            self.parse_type_annotation,
            self.parse_assignment_statement,
        ]

        self._top_level_declaration_parsers: list[
            Callable[[], TopLevelDeclarationNodeType | None]
        ] = [
            self.parse_local_declaration,
            self.parse_module_name_declaration,
            *self._let_expression_declaration_parsers,
        ]

    def parse_let_expression(self) -> LetExpressionNode | None:
        start_position = self._position
        if not self.parse_token(TokenType.LET):
            return None

        assignments: list[LetExpressionDeclarationNodeType] = []
        seen_non_import_declaration = False
        for decl in self.parse_comma_or_newline_separated(
            element_parser=self.parse_let_expression_declaration,
            ending_token=TokenType.IN,
        ):
            if isinstance(decl, ImportStatementNode):
                if seen_non_import_declaration:
                    self._raise_parse_error(
                        message="Import statements must appear before any other declarations",
                        position=decl.position,
                    )
            else:
                seen_non_import_declaration = True
            assignments.append(decl)

        body = self.parse_value_expression()

        return LetExpressionNode(
            position=start_position,
            declarations=assignments,
            body=body,
        )

    def parse_let_expression_declaration(self) -> LetExpressionDeclarationNodeType:
        for declaration_parser in self._let_expression_declaration_parsers:
            if declaration := declaration_parser():
                return declaration
        self._raise_parse_error(
            message=f"Expected declaration. Unexpected token {self._peek().format()}"
        )

    def parse_module(self) -> ModuleNode:
        start_position = self._position
        body = self.parse_module_body()
        return ModuleNode(
            position=start_position,
            body=body,
        )

    def parse_module_expression(self) -> ModuleExpressionNode | None:
        start_position = self._position
        if not (
            self._peek().type == TokenType.MODULE and self._peek(1).type == TokenType.OF
        ):
            return None

        self._read()  # consume MODULE
        of_position = self._read().position  # consume OF

        body = self.parse_module_body(of_position)
        return ModuleExpressionNode(
            position=start_position,
            body=body,
        )

    def parse_module_body(
        self, start_position: Position | None = None
    ) -> ModuleBodyNode:
        declarations = self.parse_block_body(
            start_position=start_position,
            item_parser=self.parse_top_level_declaration,
        )
        seen_non_import = False
        seen_decl = False
        name: SymbolNode | None = None

        for decl in declarations:
            if isinstance(decl, ImportStatementNode):
                if seen_non_import:
                    self._raise_parse_error(
                        message="Import statements must appear before any other declarations",
                        position=decl.position,
                    )
            else:
                seen_non_import = True
                if isinstance(decl, ModuleNameNode):
                    if seen_decl:
                        self._raise_parse_error(
                            message="Module name declaration must appear after imports and before any other declarations",
                            position=decl.position,
                        )
                    if name is not None:
                        self._raise_parse_error(
                            message="Multiple module name declarations are not allowed",
                            position=decl.position,
                        )
                    name = decl.name
                else:
                    seen_decl = True

        return ModuleBodyNode(
            position=(
                start_position
                if start_position is not None
                else (
                    declarations[0].position
                    if declarations
                    else Position(
                        line=1,
                        column=1,
                        indent_level=0,
                    )
                )
            ),
            name=name,
            declarations=declarations,
        )

    def parse_top_level_declaration(self) -> TopLevelDeclarationNodeType:
        for declaration_parser in self._top_level_declaration_parsers:
            if declaration := declaration_parser():
                return declaration
        self._raise_parse_error(
            message=f"Expected top level declaration. Unexpected token {self._peek().format()}"
        )

    def parse_function_declaration(self) -> FunctionDeclarationNode | None:
        start_position = self._position
        if not self.parse_token(TokenType.FUN):
            return None

        name = self.parse_symbol()
        if not name:
            self._raise_parse_error(
                message=f"Expected function name. Unexpected token {self._peek().format()}"
            )
            raise RuntimeError("unreachable")  # appease typechecker

        generic_parameters: list[GenericTypeParameterNode] | None = None
        if self._peek().type in (TokenType.LIST_START, TokenType.INDEXING_START):
            generic_parameters = self.parse_generic_type_parameter_list()

        parameters: list[FunctionParameterNode] = []
        self.require_any_token(
            [TokenType.PARENTHESES_START, TokenType.FUNCTION_CALL_START]
        )
        parameters = self.parse_comma_or_newline_separated(
            element_parser=self.parse_function_parameter,
            ending_tokens=[TokenType.PARENTHESES_END, TokenType.FUNCTION_CALL_END],
        )

        return_type: TypeExpressionNodeType | PlaceholderTypeNode | None = None
        if self.parse_token(TokenType.RIGHT_ARROW):
            if not (return_type := self.parse_placeholder_type()):
                return_type = self.parse_type_expression()

        self.require_token(TokenType.ASSIGN)
        body = self.parse_value_expression()

        return FunctionDeclarationNode(
            position=start_position,
            name=name,
            parameters=parameters,
            generic_parameters=generic_parameters,
            return_type=return_type,
            body=body,
        )

    def parse_procedure_declaration(self) -> ProcedureDeclarationNode | None:
        start_position = self._position
        if not self.parse_token(TokenType.PROC):
            return None

        name = self.parse_symbol()
        if not name:
            self._raise_parse_error(
                message=f"Expected procedure name. Unexpected token {self._peek().format()}"
            )
            raise RuntimeError("unreachable")  # appease typechecker

        generic_parameters: list[GenericTypeParameterNode] | None = None
        if self._peek().type in (TokenType.LIST_START, TokenType.INDEXING_START):
            generic_parameters = self.parse_generic_type_parameter_list()

        parameters: list[FunctionParameterNode] = []
        self.require_any_token(
            [TokenType.PARENTHESES_START, TokenType.FUNCTION_CALL_START]
        )
        parameters = self.parse_comma_or_newline_separated(
            element_parser=self.parse_function_parameter,
            ending_tokens=[TokenType.PARENTHESES_END, TokenType.FUNCTION_CALL_END],
        )

        return_type: TypeExpressionNodeType | PlaceholderTypeNode | None = None
        if self.parse_token(TokenType.RIGHT_ARROW):
            if not (return_type := self.parse_placeholder_type()):
                return_type = self.parse_type_expression()

        of_position = self.require_token(TokenType.OF).position
        body = self.parse_procedure_body(
            start_position=start_position,
            of_position=of_position,
        )

        return ProcedureDeclarationNode(
            position=start_position,
            name=name,
            parameters=parameters,
            generic_parameters=generic_parameters,
            return_type=return_type,
            body=body,
        )

    def parse_procedure_body(
        self, start_position: Position, of_position: Position
    ) -> list[ProcedureBodyStatementNode]:
        body = self.parse_block_body(
            start_position=of_position,
            item_parser=self.parse_procedure_body_statement,
        )

        if not body:
            self._raise_parse_error(
                message="Procedure body must have at least one statement",
                position=start_position,
            )
        elif not body[-1].expression:
            self._raise_parse_error(
                message="Last statement in procedure body must be an expression",
                position=body[-1].position,
            )
        return body

    def parse_procedure_body_statement(self) -> ProcedureBodyStatementNode:
        start_position = self._position
        declaration: LocalDeclarationNode | None = None
        expression: ValueExpressionNodeType | None = None

        if not (declaration := self.parse_local_declaration()):
            expression = self.parse_value_expression()

        return ProcedureBodyStatementNode(
            position=start_position,
            declaration=declaration,
            expression=expression,
        )

    def parse_function_parameter(self) -> FunctionParameterNode:
        start_position = self._position

        variadic = False
        if self.parse_token(TokenType.ELLIPSIS):
            variadic = True

        param = self.parse_pattern_or_error()

        type_annotation: TypeExpressionNodeType | PlaceholderTypeNode | None = None
        default_value: ValueExpressionNodeType | None = None

        if self.parse_token(TokenType.COLON):
            if not (type_annotation := self.parse_placeholder_type()):
                type_annotation = self.parse_type_expression()

        if self.parse_token(TokenType.ASSIGN):
            default_value = self.parse_value_expression()

        if not isinstance(param, (SymbolPatternNode)):
            if variadic:
                self._raise_parse_error(
                    message="Variadic function parameter cannot be a pattern",
                    position=param.position,
                )
            elif default_value is not None:
                self._raise_parse_error(
                    message="Function parameter with default value cannot be a pattern",
                    position=param.position,
                )

        return FunctionParameterNode(
            position=start_position,
            param=param,
            variadic=variadic,
            type_annotation=type_annotation,
            default_value=default_value,
        )

    def parse_module_body_declaration(self) -> ModuleBodyDeclarationNode | None:
        start_position = self._position
        if not (
            self._peek().type == TokenType.MODULE
            and self._peek(1).type == TokenType.SYMBOL
            and self._peek(2).type == TokenType.OF
        ):
            return None

        self._read()  # consume MODULE

        name = self.parse_symbol()
        if not name:
            self._raise_parse_error(
                message=f"Expected module name. Unexpected token {self._peek().format()}"
            )
            raise RuntimeError("unreachable")  # appease typechecker

        of_position = self._read().position

        body = self.parse_module_body(of_position)

        return ModuleBodyDeclarationNode(
            position=start_position,
            name=name,
            body=body,
        )

    def parse_module_assignment_declaration(
        self,
    ) -> ModuleAssignmentDeclarationNode | None:
        start_position = self._position
        if not (
            self._peek().type == TokenType.MODULE
            and self._peek(1).type == TokenType.SYMBOL
            and self._peek(2).type == TokenType.ASSIGN
        ):
            return None

        self._read()  # consume MODULE

        name = self.parse_symbol()
        if not name:
            self._raise_parse_error(
                message=f"Expected module name. Unexpected token {self._peek().format()}"
            )
            raise RuntimeError("unreachable")  # appease typechecker

        self._read()  # consume ASSIGN

        value = self.parse_value_expression()

        return ModuleAssignmentDeclarationNode(
            position=start_position,
            name=name,
            value=value,
        )

    def parse_local_declaration(self) -> LocalDeclarationNode | None:
        start_position = self._position
        if not self.parse_token(TokenType.LOCAL):
            return None

        declaration = self.parse_let_expression_declaration()

        if isinstance(declaration, ImportStatementNode):
            self._raise_parse_error(
                message="Import statement cannot be a local declaration",
                position=declaration.position,
            )

        return LocalDeclarationNode(
            position=start_position,
            declaration=declaration,
        )

    def parse_module_name_declaration(self) -> ModuleNameNode | None:
        start_position = self._position
        if not (
            self._peek().type == TokenType.MODULE
            and self._peek(1).type == TokenType.SYMBOL
            and self._peek(2).type not in (TokenType.OF, TokenType.ASSIGN)
        ):
            return None
        self._read()  # consume MODULE

        name = self.parse_symbol()
        if not name:
            self._raise_parse_error(
                message=f"Expected module name. Unexpected token {self._peek().format()}"
            )
            raise RuntimeError("unreachable")  # appease typechecker

        type_annotation: TypeExpressionNodeType | None = None
        if self.parse_token(TokenType.COLON):
            type_annotation = self.parse_type_expression()

        return ModuleNameNode(
            position=start_position,
            name=name,
            type_annotation=type_annotation,
        )

    def parse_data_declaration(self) -> DataDeclarationNode | None:
        start_position = self._position
        if not self.parse_token(TokenType.DATA):
            return None

        name = self.parse_type_name_symbol()
        if not name:
            self._raise_parse_error(
                message=f"Expected data type name. Unexpected token {self._peek().format()}"
            )
            raise RuntimeError("unreachable")  # appease typechecker

        parameters: list[GenericTypeParameterNode] | None = None
        if self._peek().type in (TokenType.LIST_START, TokenType.INDEXING_START):
            parameters = self.parse_generic_type_parameter_list()

        fields: list[DataFieldNode] | None = None
        if self._peek().type in (
            TokenType.PARENTHESES_START,
            TokenType.FUNCTION_CALL_START,
        ):
            self._read()
            fields = self.parse_comma_or_newline_separated(
                element_parser=self.parse_data_field,
                ending_tokens=[TokenType.PARENTHESES_END, TokenType.FUNCTION_CALL_END],
            )

        return DataDeclarationNode(
            position=start_position,
            name=name,
            parameters=parameters,
            fields=fields,
        )

    def parse_data_field(self) -> DataFieldNode:
        field_start_position = self._position
        field_name: SymbolNode | None = None
        if (
            self._peek().type == TokenType.SYMBOL
            and self._peek(1).type == TokenType.COLON
        ):
            assert (field_name := self.parse_symbol())
            self._read()  # consume COLON
        type_annotation = self.parse_type_expression()
        default_value: ValueExpressionNodeType | None = None
        if self.parse_token(TokenType.ASSIGN):
            default_value = self.parse_value_expression()

        if default_value and not field_name:
            self._raise_parse_error(
                message="Data field with default value must have a name",
                position=default_value.position,
            )

        return DataFieldNode(
            position=field_start_position,
            name=field_name,
            type_annotation=type_annotation,
            default_value=default_value,
        )

    def parse_type_declaration(self) -> TypeDeclarationNode | None:
        start_position = self._position
        if not self.parse_token(TokenType.TYPE):
            return None

        name = self.parse_type_name_symbol()
        if not name:
            self._raise_parse_error(
                message=f"Expected type name. Unexpected token {self._peek().format()}"
            )
            raise RuntimeError("unreachable")  # appease typechecker

        parameters: list[GenericTypeParameterNode] | None = None
        if self._peek().type in (TokenType.LIST_START, TokenType.INDEXING_START):
            parameters = self.parse_generic_type_parameter_list()

        type_expr: TypeExpressionNodeType | None = None
        if self.parse_token(TokenType.ASSIGN):
            type_expr = self.parse_type_expression()

        return TypeDeclarationNode(
            position=start_position,
            name=name,
            type_expression=type_expr,
            parameters=parameters,
        )

    def parse_import_statement(self) -> ImportStatementNode | None:
        start_position = self._position
        if not self.parse_token(TokenType.IMPORT):
            return None

        module_parts: list[SymbolNode] | None = None
        module_expr: ValueExpressionNodeType | None = None
        filename: StringLiteralNode | None = None
        fields: list[ImportStatementFieldNode | ImportStatementEllipsisNode] | None = (
            None
        )
        alias: SymbolNode | None = None

        if self._peek().type == TokenType.SYMBOL:
            module_parts = []
            assert (part := self.parse_symbol())
            module_parts.append(part)

            while dot := self.parse_token(TokenType.DOT):
                if self._peek().type == TokenType.SYMBOL:
                    assert (part := self.parse_symbol())
                    module_parts.append(part)
                else:
                    self._raise_parse_error(
                        message=f"Expected module name after '.' in import statement. Unexpected token {self._peek().format()}",
                        position=dot.position,
                    )
        elif filename := self.parse_string_literal():
            pass
        elif self._peek().type == TokenType.MODULE:
            self._read()  # consume MODULE
            module_expr = self.parse_value_expression()
        else:
            self._raise_parse_error(
                message=f"Expected module name or filename in import statement. Unexpected token {self._peek().format()}"
            )

        if self._peek().type in (
            TokenType.PARENTHESES_START,
            TokenType.FUNCTION_CALL_START,
        ):
            self._read()
            fields = self.parse_comma_or_newline_separated(
                element_parser=self.parse_import_field,
                ending_tokens=[TokenType.PARENTHESES_END, TokenType.FUNCTION_CALL_END],
            )

        if self.parse_token(TokenType.AS):
            alias = self.parse_symbol()
            if not alias:
                self._raise_parse_error(
                    message=f"Expected import alias. Unexpected token {self._peek().format()}"
                )
                raise RuntimeError("unreachable")  # appease typechecker
        elif module_expr:
            self._raise_parse_error(
                message="Dynamic import statement must have an alias",
                position=start_position,
            )
        elif filename:
            self._raise_parse_error(
                message="Import statement with filename must have an alias",
                position=start_position,
            )

        return ImportStatementNode(
            position=start_position,
            module_parts=module_parts,
            module_expr=module_expr,
            filename=filename,
            fields=fields,
            alias=alias,
        )

    def parse_import_field(
        self,
    ) -> ImportStatementFieldNode | ImportStatementEllipsisNode:
        field: ImportStatementFieldNode | ImportStatementEllipsisNode
        if self.parse_token(TokenType.ELLIPSIS):
            field = ImportStatementEllipsisNode(
                position=self._position,
            )
        else:
            name = self.parse_symbol()
            if not name:
                self._raise_parse_error(
                    message=f"Expected import field name. Unexpected token {self._peek().format()}"
                )
                raise RuntimeError("unreachable")  # appease typechecker
            alias: SymbolNode | None = None
            if self.parse_token(TokenType.AS):
                alias = self.parse_symbol()
                if not alias:
                    self._raise_parse_error(
                        message=f"Expected import field alias. Unexpected token {self._peek().format()}"
                    )
            field = ImportStatementFieldNode(
                position=name.position,
                name=name,
                alias=alias,
            )
        return field

    def parse_assignment_statement(self) -> AssignmentStatementNode | None:
        start_position = self._position
        if not (assignment := self.parse_assignment_statement_assignment()):
            return None
        return AssignmentStatementNode(
            position=start_position,
            assignment=assignment,
        )

    def parse_assignment_statement_assignment(self) -> AssignmentBindingNodeType | None:
        if assignment := self.parse_assignment():
            return assignment

        if naming_assignment := self.parse_naming_assignment():
            return naming_assignment

        if destructuring_assignment := self.parse_destructuring_assignment():
            return destructuring_assignment

        return None

    def parse_assignment(self) -> AssignmentNode | None:
        start_position = self._position
        if (
            self._peek().type == TokenType.SYMBOL
            and self._peek(1).type == TokenType.ASSIGN
        ):
            assert (target := self.parse_symbol())
            self._read()  # consume ASSIGN
            value = self.parse_value_expression()
            return AssignmentNode(
                position=start_position,
                target=target,
                type_annotation=None,
                value=value,
            )

    def parse_naming_assignment(self) -> NamingAssignmentNode | None:
        start_position = self._position
        if self._peek().type == TokenType.SYMBOL:
            symbol_token = self._peek()
            upcoming_token = self._peek(1)
            if (
                upcoming_token.type in EXPR_START_TOKENS
                and upcoming_token.position.line == symbol_token.position.line
            ):
                assert (name := self.parse_symbol())
                value = self.parse_value_expression()
                return NamingAssignmentNode(
                    position=start_position,
                    target=name,
                    value=value,
                )

    def parse_destructuring_assignment(self) -> DestructuringAssignmentNode | None:
        start_position = self._position
        if pattern := self.parse_pattern():
            if not self.parse_token(TokenType.LEFT_ARROW):
                self._raise_parse_error(
                    message=f"Expected '=' after pattern. Unexpected token {self._peek().format()}",
                    position=start_position,
                )
            value = self.parse_value_expression()
            return DestructuringAssignmentNode(
                position=start_position,
                pattern=pattern,
                value=value,
            )

    def parse_spread_assignment(self) -> SpreadAssignmentNode | None:
        start_position = self._position
        if not self.parse_token(TokenType.ELLIPSIS):
            return None
        expression = self.parse_value_expression()
        return SpreadAssignmentNode(
            position=start_position,
            expression=expression,
        )

    def parse_type_annotation(
        self,
    ) -> TypeAnnotationNode | AssignmentStatementNode | None:
        start_position = self._position
        if not (
            self._peek().type == TokenType.SYMBOL
            and self._peek(1).type == TokenType.COLON
        ):
            return None

        assert (name := self.parse_symbol())
        self._read()  # consume COLON
        type_expression = self.parse_type_expression()

        if self.parse_token(TokenType.ASSIGN):
            value = self.parse_value_expression()
            return AssignmentStatementNode(
                position=start_position,
                assignment=AssignmentNode(
                    position=start_position,
                    target=name,
                    type_annotation=type_expression,
                    value=value,
                ),
            )

        return TypeAnnotationNode(
            position=start_position,
            name=name,
            type_expression=type_expression,
        )

    def parse_type_expression(self) -> TypeExpressionNodeType:
        return self.parse_descend_type_expr_union()

    def parse_descend_type_expr_union(self) -> TypeExpressionNodeType:
        lhs = self.parse_descend_type_expr_application()
        while self.parse_token(TokenType.VARIANT):
            if not isinstance(lhs, TypeUnionNode):
                lhs = TypeUnionNode(
                    position=lhs.position,
                    elements=[lhs],
                )
            rhs = self.parse_descend_type_expr_application()
            lhs.elements.append(rhs)
        return lhs

    def parse_descend_type_expr_application(self) -> TypeExpressionNodeType:
        start_position = self._position
        lhs = self.parse_descend_type_expr_generic()
        while self._peek().type in (TokenType.LIST_START, TokenType.INDEXING_START):
            self._read()  # consume LIST_START
            arguments = self.parse_comma_or_newline_separated(
                element_parser=self.parse_generic_application_argument,
                ending_tokens=[TokenType.LIST_END, TokenType.INDEXING_END],
            )
            if not arguments:
                self._raise_parse_error(
                    message="Generic type application must have at least one argument",
                    position=start_position,
                )

            lhs = GenericTypeApplicationNode(
                position=start_position,
                generic_type=lhs,
                arguments=arguments,
            )
        return lhs

    def parse_generic_application_argument(
        self,
    ) -> GenericTypeArgumentNode | SpreadTypeExpressionNode:
        start_position = self._position

        if spread_type := self.parse_spread_type_expression():
            return spread_type

        name: SymbolNode | None = None
        if self._peek().type == TokenType.SYMBOL and (
            self._peek(1).type == TokenType.ASSIGN
        ):
            assert (name := self.parse_type_name_symbol())
            self._read()  # consume ASSIGN

        type_expr = self.parse_type_expression()
        return GenericTypeArgumentNode(
            position=start_position,
            name=name,
            argument=type_expr,
        )

    def parse_descend_type_expr_generic(self) -> TypeExpressionNodeType:
        start_position = self._position
        if self._peek().type not in (TokenType.LIST_START, TokenType.INDEXING_START):
            return self.parse_type_atom()

        parameters = self.parse_generic_type_parameter_list()
        expression = self.parse_descend_type_expr_generic()
        return GenericTypeExpressionNode(
            position=start_position,
            expression=expression,
            parameters=parameters,
        )

    def parse_generic_type_parameter_list(self) -> list[GenericTypeParameterNode]:
        start_position = self._position
        self.require_any_token([TokenType.LIST_START, TokenType.INDEXING_START])
        parameters: list[GenericTypeParameterNode] = []
        parameters = self.parse_comma_or_newline_separated(
            element_parser=self.parse_generic_type_parameter,
            ending_tokens=[TokenType.LIST_END, TokenType.INDEXING_END],
        )

        if not parameters:
            self._raise_parse_error(
                message="Generic type declaration must have at least one parameter",
                position=start_position,
            )

        return parameters

    def parse_generic_type_parameter(self) -> GenericTypeParameterNode:
        start_position = self._position

        variadic = False
        if self.parse_token(TokenType.ELLIPSIS):
            variadic = True

        name = self.parse_type_name_symbol()
        if not name:
            self._raise_parse_error(
                message=f"Expected generic type parameter name. Unexpected token {self._peek().format()}"
            )
            raise RuntimeError("unreachable")  # appease typechecker

        return GenericTypeParameterNode(
            position=start_position,
            name=name,
            variadic=variadic,
        )

    def parse_type_atom(self) -> TypeExpressionNodeType:
        for type_atom_parser in self._type_atom_parsers:
            if type_expr := type_atom_parser():
                return type_expr
        self._raise_parse_error(
            message=f"Expected type expression. Unexpected token {self._peek().format()}"
        )

    def parse_type_name(self) -> TypeExpressionNodeType | None:
        if name := self.parse_type_name_symbol():
            return TypeNameNode(
                position=name.position,
                name=name,
            )
        return None

    def parse_type_name_symbol(self) -> SymbolNode | None:
        if not (token := self.parse_token(TokenType.SYMBOL)):
            return None
        if not token.value[0].isupper():
            self._raise_parse_error(
                message="Type names must start with an uppercase letter",
                position=token.position,
            )
        return SymbolNode(
            position=token.position,
            name=token,
        )

    def parse_placeholder_type(self) -> PlaceholderTypeNode | None:
        start_position = self._position
        if not self.parse_token(TokenType.TILDE):
            return None
        return PlaceholderTypeNode(
            position=start_position,
        )

    def parse_parenthesized_type_expression(
        self,
    ) -> ParenthesizedTypeExpressionNode | None:
        start_position = self._position
        if not self.parse_any_token(
            [TokenType.PARENTHESES_START, TokenType.FUNCTION_CALL_START]
        ):
            return None

        type_expressions = self.parse_comma_or_newline_separated(
            element_parser=self.parse_tuple_element,
            ending_tokens=[TokenType.PARENTHESES_END, TokenType.FUNCTION_CALL_END],
        )

        return ParenthesizedTypeExpressionNode(
            position=start_position,
            expressions=type_expressions,
        )

    def parse_tuple_element(self) -> TypeExpressionNodeType | SpreadTypeExpressionNode:
        if spread_type := self.parse_spread_type_expression():
            return spread_type
        return self.parse_type_expression()

    def parse_type_type_expression(self) -> TypeTypeExpressionNode | None:
        start_position = self._position
        if not (self.parse_token(TokenType.TYPE)):
            return None
        expression = self.parse_value_expression()
        return TypeTypeExpressionNode(
            position=start_position,
            expression=expression,
        )

    def parse_typeof_type_expression(self) -> TypeOfTypeExpressionNode | None:
        start_position = self._position
        if not (self.parse_token(TokenType.TYPEOF)):
            return None
        expression = self.parse_value_expression()
        return TypeOfTypeExpressionNode(
            position=start_position,
            expression=expression,
        )

    def parse_const_type_expression(self) -> ConstTypeExpressionNode | None:
        start_position = self._position
        if not (self.parse_token(TokenType.CONST)):
            return None
        expression = self.parse_value_expression()
        return ConstTypeExpressionNode(
            position=start_position,
            expression=expression,
        )

    def parse_spread_type_expression(self) -> SpreadTypeExpressionNode | None:
        start_position = self._position
        if not (self.parse_token(TokenType.ELLIPSIS)):
            return None
        type_expr = self.parse_type_expression()
        return SpreadTypeExpressionNode(
            position=start_position,
            expression=type_expr,
        )

    def parse_record_type(self) -> RecordTypeNode | None:
        start_position = self._position
        if not self.parse_token(TokenType.OBJECT_START):
            return None

        fields = self.parse_comma_or_newline_separated(
            element_parser=self.parse_record_type_entry,
            ending_token=TokenType.OBJECT_END,
        )

        return RecordTypeNode(
            position=start_position,
            fields=fields,
        )

    def parse_record_type_entry(self) -> RecordTypeEntryNodeType:
        entry: RecordTypeEntryNodeType
        if spread_type := self.parse_spread_type_expression():
            entry = spread_type
        elif field := self.parse_record_type_field():
            entry = field
        else:
            self._raise_parse_error(
                message=f"Expected record type entry. Unexpected token {self._peek().format()}"
            )
        return entry

    def parse_record_type_field(self) -> RecordTypeFieldNode | None:
        start_position = self._position
        if not (name := self.parse_symbol()):
            return None

        wildcard = False
        if self.parse_token(TokenType.MULTIPLY):
            wildcard = True

        optional = False
        if self.parse_token(TokenType.QUESTION):
            optional = True

            if self.parse_token(TokenType.MULTIPLY):
                wildcard = True

        self.require_token(TokenType.COLON)
        type_annotation = self.parse_type_expression()

        if wildcard and optional:
            self._raise_parse_error(
                message="Record type field cannot be both wildcard and optional",
                position=start_position,
            )

        return RecordTypeFieldNode(
            position=start_position,
            name=name,
            optional=optional,
            wildcard=wildcard,
            type_annotation=type_annotation,
        )

    def parse_function_type(
        self,
    ) -> FunctionTypeNode | GenericTypeExpressionNode | None:
        start_position = self._position
        if not self.parse_token(TokenType.FUN):
            return None

        generic_parameters: list[GenericTypeParameterNode] | None = None
        if self._peek().type in (TokenType.LIST_START, TokenType.INDEXING_START):
            generic_parameters = self.parse_generic_type_parameter_list()

        self.require_any_token(
            [TokenType.PARENTHESES_START, TokenType.FUNCTION_CALL_START]
        )

        parameters = self.parse_comma_or_newline_separated(
            element_parser=self.parse_function_type_parameter,
            ending_tokens=[TokenType.PARENTHESES_END, TokenType.FUNCTION_CALL_END],
        )

        if not self.parse_token(TokenType.RIGHT_ARROW):
            self._raise_parse_error(
                message=f"Expected '->' after function parameter list in function type. Unexpected token {self._peek().format()}",
                position=start_position,
            )

        return_type = self.parse_type_expression()
        function_type = FunctionTypeNode(
            position=start_position,
            parameters=parameters,
            return_type=return_type,
        )
        if generic_parameters:
            return GenericTypeExpressionNode(
                position=start_position,
                parameters=generic_parameters,
                expression=function_type,
            )
        return function_type

    def parse_procedure_type(
        self,
    ) -> ProcedureTypeNode | GenericTypeExpressionNode | None:
        start_position = self._position
        if not self.parse_token(TokenType.PROC):
            return None

        generic_parameters: list[GenericTypeParameterNode] | None = None
        if self._peek().type in (TokenType.LIST_START, TokenType.INDEXING_START):
            generic_parameters = self.parse_generic_type_parameter_list()

        self.require_any_token(
            [TokenType.PARENTHESES_START, TokenType.FUNCTION_CALL_START]
        )

        parameters = self.parse_comma_or_newline_separated(
            element_parser=self.parse_function_type_parameter,
            ending_tokens=[TokenType.PARENTHESES_END, TokenType.FUNCTION_CALL_END],
        )

        if not self.parse_token(TokenType.RIGHT_ARROW):
            self._raise_parse_error(
                message=f"Expected '->' after procedure parameter list in procedure type. Unexpected token {self._peek().format()}",
                position=start_position,
            )

        return_type = self.parse_type_expression()

        procedure_type = ProcedureTypeNode(
            position=start_position,
            parameters=parameters,
            return_type=return_type,
        )
        if generic_parameters:
            return GenericTypeExpressionNode(
                position=start_position,
                parameters=generic_parameters,
                expression=procedure_type,
            )
        return procedure_type

    def parse_function_type_parameter(self) -> FunctionTypeParameterNode:
        start_position = self._position

        variadic = False
        if self.parse_token(TokenType.ELLIPSIS):
            variadic = True

        name: SymbolNode | None = None
        optional = False
        if self._peek().type == TokenType.SYMBOL and self._peek(1).type in (
            TokenType.COLON,
            TokenType.QUESTION,
        ):
            assert (name := self.parse_symbol())
            if self.parse_token(TokenType.QUESTION):
                if variadic:
                    self._raise_parse_error(
                        message="Variadic function parameter cannot be optional",
                    )
                optional = True

        if self._peek().type == TokenType.COLON:
            self._read()  # consume COLON
        elif name:
            self._raise_parse_error(
                message=f"Expected ':' after parameter name in function type. Unexpected token {self._peek().format()}",
            )

        type_annotation: TypeExpressionNodeType | SpreadTypeExpressionNode
        if spread := self.parse_spread_type_expression():
            if name:
                self._raise_parse_error(
                    message="Spread type expression cannot have a name in function type parameter",
                )
            type_annotation = spread
        else:
            type_annotation = self.parse_type_expression()
        return FunctionTypeParameterNode(
            position=start_position,
            name=name,
            variadic=variadic,
            optional=optional,
            type_annotation=type_annotation,
        )

    def parse_pattern(self) -> PatternNodeType | None:
        lhs = self.parse_pattern_atom()
        if not lhs:
            return None
        while True:
            if self.parse_token(TokenType.IF):
                condition = self.parse_value_expression()
                lhs = PatternGuardNode(
                    position=lhs.position,
                    pattern=lhs,
                    condition=condition,
                )
            elif self.parse_token(TokenType.AS):
                alias = self.parse_symbol()
                if not alias:
                    self._raise_parse_error(
                        message=f"Expected pattern alias name after 'as'. Unexpected token {self._peek().format()}"
                    )
                    raise RuntimeError("unreachable")  # appease typechecker
                lhs = PatternAliasNode(
                    position=lhs.position,
                    pattern=lhs,
                    alias=alias,
                )
            elif self.parse_token(TokenType.OF):
                self.require_token(TokenType.TYPE)
                type_expr = self.parse_type_expression()
                lhs = TypeMatchPatternNode(
                    position=lhs.position,
                    pattern=lhs,
                    type_expression=type_expr,
                )
            else:
                break
        return lhs

    def parse_pattern_or_error(self) -> PatternNodeType:
        if pattern := self.parse_pattern():
            return pattern
        self._raise_parse_error(
            message=f"Expected pattern. Unexpected token {self._peek().format()}"
        )

    def parse_pattern_atom(self) -> PatternAtomNodeType | None:
        for pattern_parser in self._pattern_atom_parsers:
            if pattern := pattern_parser():
                return pattern

    def parse_null_literal_pattern(self) -> NullLiteralPatternNode | None:
        start_position = self._position
        if not (null := self.parse_null_literal()):
            return None
        return NullLiteralPatternNode(
            position=start_position,
            null=null,
        )

    def parse_boolean_literal_pattern(self) -> BooleanLiteralPatternNode | None:
        start_position = self._position
        if not (boolean_literal := self.parse_boolean_literal()):
            return None
        return BooleanLiteralPatternNode(
            position=start_position,
            boolean=boolean_literal,
        )

    def parse_const_pattern(self) -> ConstPatternNode | None:
        start_position = self._position
        if not self.parse_token(TokenType.CONST):
            return None
        value = self.parse_value_expression()
        return ConstPatternNode(
            position=start_position,
            value=value,
        )

    def parse_number_literal_pattern(self) -> NumberLiteralPatternNode | None:
        start_position = self._position
        if not (number_literal := self.parse_number_literal()):
            return None
        return NumberLiteralPatternNode(
            position=start_position,
            number=number_literal,
        )

    def parse_string_literal_pattern(self) -> StringLiteralPatternNode | None:
        start_position = self._position
        if not (string_literal := self.parse_string_literal()):
            return None
        return StringLiteralPatternNode(
            position=start_position,
            string=string_literal,
        )

    def parse_regex_literal_pattern(self) -> RegexLiteralPatternNode | None:
        start_position = self._position
        if not (regex_literal := self.parse_regex_literal()):
            return None
        return RegexLiteralPatternNode(
            position=start_position,
            regex=regex_literal,
        )

    def parse_format_string_literal_pattern(
        self,
    ) -> FormatStringLiteralPatternNode | None:
        start_position = self._position
        if not (
            open_quote := self.parse_any_token(
                [TokenType.FORMAT_STRING_START, TokenType.MULTILINE_FORMAT_STRING_START]
            )
        ):
            return None

        contents: list[FormatStringPatternPartNodeType] = []
        seen_direction_indicator = False
        seen_left_direction_indicator = False
        while not (
            close_quote := self.parse_any_token(
                [TokenType.FORMAT_STRING_END, TokenType.MULTILINE_FORMAT_STRING_END]
            )
        ):
            part = self.parse_format_string_pattern_part()
            if isinstance(part, FormatStringPatternDirectionIndicatorNode):
                if seen_direction_indicator:
                    self._raise_parse_error(
                        message="Format string pattern can only have one direction indicator",
                        position=part.position,
                    )
                seen_direction_indicator = True
                if part.direction.type == TokenType.LEFT_ARROW:
                    seen_left_direction_indicator = True
                elif contents:
                    self._raise_parse_error(
                        message="Right direction indicator must be at the start of the format string pattern",
                        position=part.position,
                    )
            elif seen_left_direction_indicator:
                self._raise_parse_error(
                    message="Left direction indicator must be at the end of the format string pattern",
                    position=part.position,
                )
            contents.append(part)

        return FormatStringLiteralPatternNode(
            position=start_position,
            open_quote=open_quote,
            contents=contents,
            close_quote=close_quote,
        )

    def parse_format_string_pattern_part(self) -> FormatStringPatternPartNodeType:
        if (
            direction_indicator
            := self.parse_format_string_pattern_direction_indicator()
        ):
            return direction_indicator

        if text_section := self.parse_format_string_text_section_pattern():
            return text_section

        if expression_section := self.parse_format_string_expression_pattern():
            return expression_section

        self._raise_parse_error(
            message=f"Expected format string pattern part. Unexpected token {self._peek().format()}"
        )

    def parse_format_string_pattern_direction_indicator(
        self,
    ) -> FormatStringPatternDirectionIndicatorNode | None:
        start_position = self._position
        if not (
            self._peek().type == TokenType.FORMAT_STRING_EXPR_START
            and self._peek(1).type in (TokenType.RIGHT_ARROW, TokenType.LEFT_ARROW)
        ):
            return None

        self._read()  # consume FORMAT_STRING_EXPR_START
        direction_token = self._read()  # consume RIGHT_ARROW or LEFT_ARROW
        self.require_token(TokenType.FORMAT_STRING_EXPR_END)

        return FormatStringPatternDirectionIndicatorNode(
            position=start_position,
            direction=direction_token,
        )

    def parse_format_string_text_section_pattern(
        self,
    ) -> FormatStringTextSectionPatternNode | None:
        start_position = self._position
        if not (content_token := self.parse_token(TokenType.STRING_CONTENTS)):
            return None
        return FormatStringTextSectionPatternNode(
            position=start_position,
            string_contents=content_token,
        )

    def parse_format_string_expression_pattern(
        self,
    ) -> FormatStringExpressionPatternNode | None:
        start_position = self._position
        if not self.parse_token(TokenType.FORMAT_STRING_EXPR_START):
            return None
        pattern = self.parse_pattern_or_error()
        self._read()  # consume FORMAT_STRING_EXPR_END
        return FormatStringExpressionPatternNode(
            position=start_position,
            pattern=pattern,
        )

    def parse_data_type_pattern(self) -> DataTypePatternNode | None:
        start_position = self._position
        if not (
            self._peek().type == TokenType.SYMBOL and self._peek().value[0].isupper()
        ):
            return None

        name = self.parse_type_name_symbol()
        if not name:
            self._raise_parse_error(
                message=f"Expected data type name in pattern. Unexpected token {self._peek().format()}"
            )
            raise RuntimeError("unreachable")  # appease typechecker

        fields: list[KeyValueFieldPatternNode] | None = None
        if self.parse_token(TokenType.FUNCTION_CALL_START):
            fields = self.parse_comma_or_newline_separated(
                element_parser=self.parse_key_value_field_pattern,
                ending_token=TokenType.FUNCTION_CALL_END,
            )

        return DataTypePatternNode(
            position=start_position,
            name=name,
            fields=fields,
        )

    def parse_record_pattern(self) -> RecordPatternNode | None:
        start_position = self._position
        if not self.parse_token(TokenType.OBJECT_START):
            return None

        fields = self.parse_comma_or_newline_separated(
            element_parser=self.parse_key_value_field_pattern,
            ending_token=TokenType.OBJECT_END,
        )
        for field in fields:
            if field.name is None and not (
                isinstance(field.pattern, (RestPatternNode, SymbolPatternNode))
            ):
                self._raise_parse_error(
                    message="Record field pattern must have a name unless it is a rest pattern",
                    position=field.position,
                )

        return RecordPatternNode(
            position=start_position,
            fields=fields,
        )

    def parse_key_value_field_pattern(self) -> KeyValueFieldPatternNode:
        start_position = self._position
        name: SymbolNode | None = None
        if (
            self._peek().type == TokenType.SYMBOL
            and self._peek(1).type == TokenType.ASSIGN
        ):
            assert (name := self.parse_symbol())
            self._read()  # consume ASSIGN
        pattern = self.parse_pattern_or_error()
        return KeyValueFieldPatternNode(
            position=start_position,
            name=name,
            pattern=pattern,
        )

    def parse_parenthesized_pattern(
        self,
    ) -> ParenthesizedPatternNode | None:
        start_position = self._position
        if not self.parse_any_token(
            [TokenType.PARENTHESES_START, TokenType.FUNCTION_CALL_START]
        ):
            return None

        elements = self.parse_comma_or_newline_separated(
            element_parser=self.parse_pattern_or_error,
            ending_tokens=[TokenType.PARENTHESES_END, TokenType.FUNCTION_CALL_END],
        )

        return ParenthesizedPatternNode(
            position=start_position,
            elements=elements,
        )

    def parse_list_pattern(self) -> ListPatternNode | None:
        start_position = self._position
        if not self.parse_any_token([TokenType.LIST_START, TokenType.INDEXING_START]):
            return None

        elements = self.parse_comma_or_newline_separated(
            element_parser=self.parse_pattern_or_error,
            ending_tokens=[TokenType.LIST_END, TokenType.INDEXING_END],
        )

        return ListPatternNode(
            position=start_position,
            elements=elements,
        )

    def parse_rest_pattern(self) -> RestPatternNode | None:
        start_position = self._position
        if not self.parse_token(TokenType.ELLIPSIS):
            return None
        symbol = self.parse_symbol()
        return RestPatternNode(
            position=start_position,
            name=symbol,
        )

    def parse_symbol_pattern(self) -> SymbolPatternNode | None:
        start_position = self._position
        if (self._peek().type == TokenType.SYMBOL) and (
            not self._peek().value[0].isupper()
        ):
            assert (symbol := self.parse_symbol())
            return SymbolPatternNode(
                position=start_position,
                symbol=symbol,
            )

    def parse_value_expression(self) -> ValueExpressionNodeType:
        return self.parse_descend_expr_pipe()

    def parse_descend_expr_pipe(self) -> ValueExpressionNodeType:
        lhs = self.parse_descend_expr_or()
        while self.parse_token(TokenType.PIPE):
            rhs = self.parse_descend_expr_or()
            lhs = BinaryOperationNode(
                position=lhs.position,
                left=lhs,
                operator=Operator.PIPE,
                right=rhs,
            )
        return lhs

    def parse_descend_expr_or(self) -> ValueExpressionNodeType:
        lhs = self.parse_descend_expr_and()
        while self.parse_token(TokenType.OR):
            rhs = self.parse_descend_expr_and()
            lhs = BinaryOperationNode(
                position=lhs.position,
                left=lhs,
                operator=Operator.OR,
                right=rhs,
            )
        return lhs

    def parse_descend_expr_and(self) -> ValueExpressionNodeType:
        lhs = self.parse_descend_expr_not()
        while self.parse_token(TokenType.AND):
            rhs = self.parse_descend_expr_not()
            lhs = BinaryOperationNode(
                position=lhs.position,
                left=lhs,
                operator=Operator.AND,
                right=rhs,
            )
        return lhs

    def parse_descend_expr_not(self) -> ValueExpressionNodeType:
        start_position = self._position
        if self.parse_token(TokenType.NOT):
            operand = self.parse_descend_expr_not()
            return UnaryOperationNode(
                position=start_position,
                operator=Operator.NOT,
                operand=operand,
            )
        return self.parse_descend_expr_comparison()

    def parse_descend_expr_comparison(self) -> ValueExpressionNodeType:
        lhs = self.parse_descend_expr_add()
        while comparison_token := self.parse_any_token(
            [
                TokenType.EQUAL,
                TokenType.NOT_EQUAL,
                TokenType.GREATER_THAN,
                TokenType.GREATER_THAN_EQUAL,
                TokenType.LESS_THAN,
                TokenType.LESS_THAN_EQUAL,
            ]
        ):
            rhs = self.parse_descend_expr_add()
            op = Operator(comparison_token.value)
            lhs = BinaryOperationNode(
                position=lhs.position,
                left=lhs,
                operator=op,
                right=rhs,
            )
        return lhs

    def parse_descend_expr_add(self) -> ValueExpressionNodeType:
        lhs = self.parse_descend_expr_mult()
        while op_token := self.parse_any_token([TokenType.PLUS, TokenType.MINUS]):
            rhs = self.parse_descend_expr_mult()
            op = Operator(op_token.value)
            lhs = BinaryOperationNode(
                position=lhs.position,
                left=lhs,
                operator=op,
                right=rhs,
            )
        return lhs

    def parse_descend_expr_mult(self) -> ValueExpressionNodeType:
        lhs = self.parse_descend_expr_pos_neg()
        while op_token := self.parse_any_token(
            [
                TokenType.MULTIPLY,
                TokenType.DIVIDE,
                TokenType.FLOOR_DIVIDE,
                TokenType.MODULO,
            ]
        ):
            rhs = self.parse_descend_expr_pos_neg()
            op = Operator(op_token.value)
            lhs = BinaryOperationNode(
                position=lhs.position,
                left=lhs,
                operator=op,
                right=rhs,
            )
        return lhs

    def parse_descend_expr_pos_neg(self) -> ValueExpressionNodeType:
        if not (op_token := self.parse_any_token([TokenType.PLUS, TokenType.MINUS])):
            return self.parse_descend_expr_pow()

        operand = self.parse_descend_expr_pos_neg()
        op = Operator.POSITIVE if op_token.type == TokenType.PLUS else Operator.NEGATIVE
        return UnaryOperationNode(
            position=op_token.position,
            operator=op,
            operand=operand,
        )

    def parse_descend_expr_pow(self) -> ValueExpressionNodeType:
        lhs = self.parse_descend_expr_as_type()
        while self.parse_token(TokenType.EXPONENTIATION):
            rhs = self.parse_descend_expr_pow()
            lhs = BinaryOperationNode(
                position=lhs.position,
                left=lhs,
                operator=Operator.EXPONENTIATION,
                right=rhs,
            )
        return lhs

    def parse_descend_expr_as_type(self) -> ValueExpressionNodeType:
        lhs = self.parse_descend_expr_postfix()
        while self.parse_token(TokenType.COLON):
            type_expression = self.parse_type_expression()
            lhs = TypeAnnotationExpressionNode(
                position=lhs.position,
                value_expression=lhs,
                type_expression=type_expression,
            )
        return lhs

    def parse_descend_expr_postfix(self) -> ValueExpressionNodeType:
        lhs = self.parse_atom()
        while True:
            if self.parse_token(TokenType.TYPE_APPLICATION_START):
                type_arguments = self.parse_comma_or_newline_separated(
                    element_parser=self.parse_type_expression,
                    ending_token=TokenType.TYPE_APPLICATION_END,
                )
                if not type_arguments:
                    self._raise_parse_error(
                        message="Type application must have at least one type argument",
                        position=self._position,
                    )
                lhs = TypeApplicationExpressionNode(
                    position=lhs.position,
                    value_expression=lhs,
                    type_arguments=type_arguments,
                )
            elif self.parse_token(TokenType.INDEXING_START):
                index_expression = self.parse_value_expression()
                self.require_token(TokenType.INDEXING_END)
                lhs = IndexingExpressionNode(
                    position=lhs.position,
                    object_expression=lhs,
                    index_expression=index_expression,
                )
            elif self.parse_token(TokenType.DOT):
                if property_token := self.parse_token(TokenType.SYMBOL):
                    field_name = SymbolNode(
                        position=property_token.position,
                        name=property_token,
                    )
                else:
                    self._raise_parse_error(
                        message=f"Expected field name after '.' in field access expression. Unexpected token {self._peek().format()}",
                    )
                lhs = FieldAccessExpressionNode(
                    position=lhs.position,
                    object_expression=lhs,
                    field=field_name,
                )
            elif self.parse_token(TokenType.FUNCTION_CALL_START):
                s = self._save_placeholder_stack_size()
                arguments = self.parse_comma_or_newline_separated(
                    element_parser=self.parse_function_call_argument,
                    ending_token=TokenType.FUNCTION_CALL_END,
                )
                lhs = FunctionCallExpressionNode(
                    position=lhs.position,
                    function_expression=lhs,
                    arguments=arguments,
                )
                if self._reset_placeholder_stack(s) > 0:
                    lhs = PlaceholderExpressionNode(
                        position=lhs.position,
                        expression=lhs,
                    )
            else:
                break
        return lhs

    def parse_function_call_argument(self) -> FunctionCallArgumentNodeType:
        if spread_assignment := self.parse_spread_assignment():
            return spread_assignment

        if assignment := self.parse_assignment():
            return assignment

        if naming_assignment := self.parse_naming_assignment():
            return naming_assignment

        return self.parse_value_expression()

    def parse_atom(self) -> AtomNodeType:
        for atom_parser in self._atom_parsers:
            if value := atom_parser():
                return value
        self._raise_parse_error(
            message=f"Expected expression. Unexpected token {self._peek().format()}"
        )

    def parse_function_expression(self) -> FunctionExpressionNode | None:
        start_position = self._position
        if not self.parse_token(TokenType.FUN):
            return None

        generic_parameters: list[GenericTypeParameterNode] | None = None
        if self._peek().type == TokenType.LIST_START:
            generic_parameters = self.parse_generic_type_parameter_list()

        self.parse_any_token(
            [TokenType.PARENTHESES_START, TokenType.FUNCTION_CALL_START]
        )
        parameters = self.parse_comma_or_newline_separated(
            element_parser=self.parse_function_parameter,
            ending_tokens=[TokenType.PARENTHESES_END, TokenType.FUNCTION_CALL_END],
        )

        self.require_token(TokenType.RIGHT_ARROW)
        body = self.parse_value_expression()
        return FunctionExpressionNode(
            position=start_position,
            parameters=parameters,
            generic_parameters=generic_parameters,
            body=body,
        )

    def parse_procedure_expression(self) -> ProcedureExpressionNode | None:
        start_position = self._position
        if not self.parse_token(TokenType.PROC):
            return None

        generic_parameters: list[GenericTypeParameterNode] | None = None
        if self._peek().type == TokenType.LIST_START:
            generic_parameters = self.parse_generic_type_parameter_list()

        self.parse_any_token(
            [TokenType.PARENTHESES_START, TokenType.FUNCTION_CALL_START]
        )
        parameters = self.parse_comma_or_newline_separated(
            element_parser=self.parse_function_parameter,
            ending_tokens=[TokenType.PARENTHESES_END, TokenType.FUNCTION_CALL_END],
        )

        of_position = self.require_token(TokenType.OF).position
        body = self.parse_procedure_body(
            start_position=start_position,
            of_position=of_position,
        )
        return ProcedureExpressionNode(
            position=start_position,
            parameters=parameters,
            generic_parameters=generic_parameters,
            body=body,
        )

    def parse_case_expression(self) -> CaseExpressionNode | None:
        start_position = self._position
        if not self.parse_token(TokenType.CASE):
            return None

        expression = self.parse_value_expression()
        of_position = self.require_token(TokenType.OF).position

        branches = self.parse_block_body(
            start_position=of_position,
            item_parser=self.parse_case_branch,
        )

        if not branches:
            self._raise_parse_error(
                message="Case expression must have at least one branch",
                position=start_position,
            )

        return CaseExpressionNode(
            position=start_position,
            expression=expression,
            branches=branches,
        )

    def parse_case_branch(self) -> CaseBranchNode:
        start_position = self._position
        pattern = self.parse_pattern_or_error()
        self.require_token(TokenType.RIGHT_ARROW)
        expression = self.parse_value_expression()
        return CaseBranchNode(
            position=start_position,
            pattern=pattern,
            expression=expression,
        )

    def parse_if_expression(self) -> IfExpressionNode | None:
        start_position = self._position
        if not self.parse_token(TokenType.IF):
            return None

        condition = self.parse_value_expression()
        self.require_token(TokenType.THEN)
        then_branch = self.parse_value_expression()
        self.require_token(TokenType.ELSE)
        else_branch = self.parse_value_expression()

        return IfExpressionNode(
            position=start_position,
            condition=condition,
            then_branch=then_branch,
            else_branch=else_branch,
        )

    def parse_list_literal(self) -> ListLiteralNode | None:
        start_position = self._position
        if not self.parse_token(TokenType.LIST_START):
            return None

        elements = self.parse_comma_or_newline_separated(
            element_parser=self.parse_list_literal_element,
            ending_token=TokenType.LIST_END,
        )

        return ListLiteralNode(
            position=start_position,
            elements=elements,
        )

    def parse_list_literal_element(self) -> ListLiteralElementNodeType:
        if spread_assignment := self.parse_spread_assignment():
            return spread_assignment

        return self.parse_value_expression()

    def parse_record_literal(self) -> RecordLiteralNode | None:
        start_position = self._position
        if not self.parse_token(TokenType.OBJECT_START):
            return None

        entries = self.parse_comma_or_newline_separated(
            element_parser=self.parse_record_literal_entry,
            ending_token=TokenType.OBJECT_END,
        )
        return RecordLiteralNode(
            position=start_position,
            entries=entries,
        )

    def parse_record_literal_entry(self) -> RecordLiteralEntryNodeType:
        if spread_assignment := self.parse_spread_assignment():
            return spread_assignment

        if assignment := self.parse_assignment():
            return assignment

        if naming_assignment := self.parse_naming_assignment():
            return naming_assignment

        if shorthand_assignment := self.parse_shorthand_assignment():
            return shorthand_assignment

        return self.parse_mapping_assignment()

    def parse_mapping_assignment(self) -> MappingAssignmentNode:
        start_position = self._position
        key = self.parse_value_expression()
        self.require_token(TokenType.MAPPING)
        value = self.parse_value_expression()
        return MappingAssignmentNode(
            position=start_position,
            key=key,
            value=value,
        )

    def parse_shorthand_assignment(self) -> ShorthandAssignmentNode | None:
        start_position = self._position
        if not (
            self._peek().type == TokenType.SYMBOL
            and self._peek(1).type not in (TokenType.ASSIGN, TokenType.MAPPING)
        ):
            return None
        assert (symbol := self.parse_symbol())
        return ShorthandAssignmentNode(
            position=start_position,
            name=symbol,
        )

    def parse_parenthesized_expression(
        self,
    ) -> ParenthesizedExpressionNode | PlaceholderExpressionNode | None:
        start_position = self._position
        if not self.parse_token(TokenType.PARENTHESES_START):
            return None

        s = self._save_placeholder_stack_size()
        expressions = self.parse_comma_or_newline_separated(
            element_parser=self.parse_value_expression,
            ending_token=TokenType.PARENTHESES_END,
        )

        expr = ParenthesizedExpressionNode(
            position=start_position,
            elements=expressions,
        )

        if self._reset_placeholder_stack(s) > 0:
            expr = PlaceholderExpressionNode(
                position=expr.position,
                expression=expr,
            )

        return expr

    def parse_null_literal(self) -> NullLiteralNode | None:
        if self._peek().type != TokenType.NULL:
            return None
        token = self._read()
        return NullLiteralNode(
            position=token.position,
            contents=token,
        )

    def parse_boolean_literal(self) -> BooleanLiteralNode | None:
        if self._peek().type not in {TokenType.TRUE, TokenType.FALSE}:
            return None
        token = self._read()
        return BooleanLiteralNode(
            position=token.position,
            contents=token,
        )

    def parse_tilde_literal(self) -> SymbolNode | None:
        if self._peek().type != TokenType.TILDE:
            return None
        token = self._read()
        self._placeholder_stack_push(token.position)
        return SymbolNode(
            position=token.position,
            name=token,
        )

    def parse_number_literal(self) -> NumberLiteralNode | None:
        if self._peek().type not in {
            TokenType.INTEGER_LITERAL,
            TokenType.FLOAT_LITERAL,
            TokenType.SCI_FLOAT_LITERAL,
        }:
            return None
        token = self._read()
        return NumberLiteralNode(
            position=token.position,
            contents=token,
        )

    def parse_string_literal(self) -> StringLiteralNode | None:
        start_position = self._position
        if not (
            open_quote := self.parse_any_token(
                [
                    TokenType.STRING_LITERAL_START,
                    TokenType.RAW_STRING_LITERAL_START,
                    TokenType.MULTILINE_STRING_LITERAL_START,
                    TokenType.RAW_MULTILINE_STRING_LITERAL_START,
                ]
            )
        ):
            return None
        token = self.require_token(TokenType.STRING_CONTENTS)
        close_quote = self._read()
        return StringLiteralNode(
            position=start_position,
            open_quote=open_quote,
            contents=token,
            close_quote=close_quote,
        )

    def parse_regex_literal(self) -> RegexLiteralNode | None:
        start_position = self._position
        if not self.parse_token(TokenType.REGEX_LITERAL_START):
            return None
        contents = self.require_token(TokenType.STRING_CONTENTS)
        self.require_token(TokenType.REGEX_LITERAL_END)
        return RegexLiteralNode(
            position=start_position,
            contents=contents,
        )

    def parse_format_string_literal(self) -> FormatStringLiteralNode | None:
        start_position = self._position
        if not (
            open_quote := self.parse_any_token(
                [TokenType.FORMAT_STRING_START, TokenType.MULTILINE_FORMAT_STRING_START]
            )
        ):
            return None

        contents: list[FormatStringTextSectionNode | FormatStringExpressionNode] = []
        while not (
            close_quote := self.parse_any_token(
                [TokenType.FORMAT_STRING_END, TokenType.MULTILINE_FORMAT_STRING_END]
            )
        ):
            if content_token := self.parse_token(TokenType.STRING_CONTENTS):
                contents.append(
                    FormatStringTextSectionNode(
                        position=content_token.position,
                        string_contents=content_token,
                    )
                )
            elif tok := self.parse_token(TokenType.FORMAT_STRING_EXPR_START):
                expr = self.parse_value_expression()
                self._read()  # consume FORMAT_STRING_EXPR_END
                contents.append(
                    FormatStringExpressionNode(
                        position=tok.position,
                        expression=expr,
                    )
                )
        return FormatStringLiteralNode(
            position=start_position,
            open_quote=open_quote,
            contents=contents,
            close_quote=close_quote,
        )

    def parse_symbol(self) -> SymbolNode | None:
        if not (token := self.parse_any_token([TokenType.SYMBOL, TokenType.SYMBOL])):
            return None
        return SymbolNode(
            position=token.position,
            name=token,
        )

    def parse_block_body(
        self,
        start_position: Position | None,
        item_parser: Callable[[], T],
    ) -> list[T]:
        items: list[T] = []
        indent_level = -1

        def end_of_block() -> bool:
            return self.at_end() or (
                start_position is not None
                and self._position.indent_level <= start_position.indent_level
                and self._position.line != start_position.line
            )

        ended_with_semicolon = False
        while not end_of_block():
            if self.parse_multiple_tokens(TokenType.SEMICOLON):
                if end_of_block():
                    ended_with_semicolon = True
                    break
            if start_position is None and self._position.indent_level != 0:
                self._raise_parse_error(message="Top-level items must not be indented")
            elif (
                start_position is not None
                and self._position.line != start_position.line
            ):
                if indent_level == -1:
                    indent_level = self._position.indent_level
                elif self._position.indent_level != indent_level:
                    self._raise_parse_error(
                        message="All items in block must have the same indent level",
                    )

            item = item_parser()
            self._assert_empty_placeholder_stack()
            items.append(item)

            if end_of_block():
                break

            if self.parse_multiple_tokens(TokenType.SEMICOLON):
                if end_of_block():
                    ended_with_semicolon = True
                    break
            elif isinstance(item, Node) and self._position.line == item.position.line:
                self._raise_parse_error(
                    message="Block statements must be separated by semicolons or newlines",
                )

        if not items and not ended_with_semicolon and start_position is not None:
            self._raise_parse_error(
                message="Blocks must have at least one item, or be terminated with a semicolon ';'",
                position=start_position,
            )
        return items

    def parse_comma_or_newline_separated(
        self,
        element_parser: Callable[[], T],
        ending_token: TokenType | None = None,
        ending_tokens: list[TokenType] | None = None,
        ending_parser: Callable[[], Token | None] | None = None,
    ) -> list[T]:
        elements: list[T] = []

        def reached_end() -> bool:
            if ending_token:
                return self.parse_token(ending_token) is not None
            elif ending_tokens:
                return self.parse_any_token(ending_tokens) is not None
            elif ending_parser:
                return ending_parser() is not None
            return False

        while not reached_end():
            element = element_parser()
            elements.append(element)

            if reached_end():
                break

            if self.parse_token(TokenType.COMMA):
                if reached_end():
                    break
            else:
                position = getattr(element, "position", None)
                if isinstance(position, Position):
                    if self._peek().position.line == position.line:
                        self._raise_parse_error(
                            message="Elements must be separated by a comma and/or newline",
                            position=self._peek().position,
                        )

        return elements

    def parse_any_token(self, expected_types: list[TokenType]) -> Token | None:
        token = self._peek()
        if token.type not in expected_types:
            return None
        return self._read()

    def parse_token(self, expected_type: TokenType) -> Token | None:
        token = self._peek()
        if token.type != expected_type:
            return None
        return self._read()

    def parse_multiple_tokens(self, expected_type: TokenType) -> list[Token]:
        tokens: list[Token] = []
        while token := self.parse_token(expected_type):
            tokens.append(token)
        return tokens

    def require_any_token(self, expected_types: list[TokenType]) -> Token:
        token = self.parse_any_token(expected_types)
        if token is None:
            expected_names = ", ".join(t.name for t in expected_types)
            message = (
                f"Expected token of type {expected_names}. Unexpected token {self._peek().format()}"
                if self._peek().type != TokenType.EOF
                else f"Expected token of type {expected_names}. Unexpected end of file"
            )
            self._raise_parse_error(message=message)
            raise RuntimeError("unreachable")  # appease type checker
        return token

    def require_token(self, expected_type: TokenType) -> Token:
        token = self.parse_token(expected_type)
        if token is None:
            message = (
                f"Expected token of type {expected_type.name}. Unexpected token {self._peek().format()}"
                if self._peek().type != TokenType.EOF
                else f"Expected token of type {expected_type.name}. Unexpected end of file"
            )
            self._raise_parse_error(message=message)
            raise RuntimeError("unreachable")  # appease type checker
        return token

    def at_end(self) -> bool:
        return self._peek().type == TokenType.EOF

    def _assert_empty_placeholder_stack(self) -> None:
        if self._placeholder_stack:
            self._raise_parse_error(
                message="Placeholder '~' not contained within parentheses or a function call expression",
                position=self._placeholder_stack[-1],
            )

    def _save_placeholder_stack_size(self) -> int:
        return len(self._placeholder_stack)

    def _placeholder_stack_push(self, position: Position) -> None:
        self._placeholder_stack.append(position)

    def _reset_placeholder_stack(self, size: int) -> int:
        popped = 0
        while len(self._placeholder_stack) > size:
            self._placeholder_stack.pop()
            popped += 1
        return popped

    def _raise_parse_error(
        self, message: str, position: Position | None = None
    ) -> NoReturn:
        raise ParseError(
            message=message,
            filename=self._filename,
            position=position or self._position,
        )

    def _peek(self, n: int = 0) -> Token:
        return self._lexer.peek(n)

    def _read(self) -> Token:
        token = self._lexer.read()
        self._position = self._lexer.peek().position
        return token
