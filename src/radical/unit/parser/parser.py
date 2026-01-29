from typing import Callable, NoReturn, TypeVar
from radical.data.parser.ast import (
    AssignmentNode,
    BooleanLiteralNode,
    ConstExpressionNode,
    DataDeclarationNode,
    DataFieldNode,
    FunctionParameterNode,
    FunctionTypeNode,
    GenericTypeApplicationNode,
    GenericTypeExpressionNode,
    GenericTypeParameterNode,
    IfExpressionNode,
    ImportStatementEllipsisNode,
    ImportStatementFieldNode,
    ImportStatementNode,
    ListLiteralNode,
    ModuleNode,
    Node,
    NullLiteralNode,
    NumberLiteralNode,
    ParenthesizedExpressionNode,
    ParenthesizedTypeExpressionNode,
    RecordTypeNode,
    SpreadAssignmentStatementNode,
    SpreadTypeExpressionNode,
    StringLiteralNode,
    SymbolNode,
    TopLevelDeclarationNodeType,
    TupleLiteralNode,
    TupleTypeNode,
    TypeAnnotationNode,
    TypeDeclarationNode,
    TypeOfExpressionNode,
    TypeTypeExpressionNode,
    TypeExpressionNodeType,
    TypeNameNode,
    TypeUnionNode,
    UnaryOperationNode,
    ValueExpressionNodeType,
    AtomNodeType,
    BinaryOperationNode,
    Operator,
)
from radical.data.parser.errors import ParseError
from radical.data.parser.position import Position
from radical.data.parser.token import Token, TokenType
from radical.unit.parser.lexer import Lexer
from radical.util.core.unit import Unit

T = TypeVar("T")


class Parser(Unit):
    def __init__(self, lexer: Lexer, filename: str):
        self._lexer = lexer
        self._filename = filename
        self._position = Position(
            line=1,
            column=1,
            indent_level=0,
        )
        self._atom_parsers: list[Callable[[], AtomNodeType | None]] = [
            self.parse_parenthesized_expression,
            self.parse_null_literal,
            self.parse_boolean_literal,
            self.parse_number_literal,
            self.parse_string_literal,
            self.parse_symbol,
            self.parse_list_literal,
            self.parse_if_expression,
        ]

        self._type_atom_parsers: list[Callable[[], TypeExpressionNodeType | None]] = [
            self.parse_type_name,
            self.parse_parenthesized_type_expression,
            self.parse_type_type_expression,
            self.parse_typeof_expression,
            self.parse_const_expression,
            self.parse_spread_type_expression,
            self.parse_record_type,
            self.parse_function_type,
        ]

        self._top_level_declaration_parsers: list[
            Callable[[], TopLevelDeclarationNodeType | None]
        ] = [
            self.parse_data_declaration,
            self.parse_type_declaration,
            self.parse_spread_assignment_statement,
            self.parse_import_statement,
            self.parse_assignment,
        ]

    def parse_module(self) -> ModuleNode:
        start_position = self._position
        declarations: list[TopLevelDeclarationNodeType] = []
        while not self.at_end():
            declarations.append(self.parse_top_level_declaration())
        return ModuleNode(
            position=start_position,
            declarations=declarations,
        )

    def parse_top_level_declaration(self) -> TopLevelDeclarationNodeType:
        for declaration_parser in self._top_level_declaration_parsers:
            if declaration := declaration_parser():
                return declaration
        self._raise_parse_error(
            message=f"Expected top level declaration. Unexpected token {self._peek().pretty()}"
        )

    def parse_data_declaration(self) -> DataDeclarationNode | None:
        start_position = self._position
        if self._peek().type != TokenType.DATA and not (
            self._peek().type == TokenType.LOCAL
            and self._peek(1).type == TokenType.DATA
        ):
            return None

        local = False
        if self.parse_token(TokenType.LOCAL):
            local = True

        self._read()  # consume DATA
        name_token = self.require_token(TokenType.SYMBOL)
        name = SymbolNode(
            position=name_token.position,
            name=name_token,
        )
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
            local=local,
        )

    def parse_data_field(self) -> DataFieldNode:
        field_start_position = self._position
        field_name: SymbolNode | None = None
        if (
            self._peek().type == TokenType.SYMBOL
            and self._peek(1).type == TokenType.COLON
        ):
            name_token = self._read()
            field_name = SymbolNode(
                position=name_token.position,
                name=name_token,
            )
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
        if self._peek().type not in (TokenType.TYPE,) and not (
            self._peek().type == TokenType.LOCAL
            and self._peek(1).type == TokenType.TYPE
        ):
            return None

        local = False
        if self.parse_token(TokenType.LOCAL):
            local = True

        self._read()  # consume TYPE

        name_token = self.require_token(TokenType.SYMBOL)
        name = SymbolNode(
            position=name_token.position,
            name=name_token,
        )

        parameters: list[GenericTypeParameterNode] | None = None
        if self._peek().type in (TokenType.LIST_START, TokenType.INDEXING_START):
            parameters = self.parse_generic_type_parameter_list()

        self.require_token(TokenType.ASSIGN)
        type_expr = self.parse_type_expression()
        return TypeDeclarationNode(
            position=start_position,
            name=name,
            type_expression=type_expr,
            local=local,
            parameters=parameters,
        )

    def parse_spread_assignment_statement(self) -> SpreadAssignmentStatementNode | None:
        start_position = self._position
        if not self.parse_token(TokenType.ELLIPSIS):
            return None
        value = self.parse_value_expression()
        return SpreadAssignmentStatementNode(
            position=start_position,
            value=value,
        )

    def parse_import_statement(self) -> ImportStatementNode | None:
        start_position = self._position
        if not self.parse_token(TokenType.IMPORT):
            return None

        module_parts: list[SymbolNode] | None = None
        module_expr: ValueExpressionNodeType | None = None
        filename: StringLiteralNode | None = None
        filename_expr: ValueExpressionNodeType | None = None
        fields: list[ImportStatementFieldNode | ImportStatementEllipsisNode] | None = (
            None
        )
        alias: SymbolNode | None = None

        if self._peek().type == TokenType.SYMBOL:
            module_parts = []
            module_part_token = self._read()
            module_parts.append(
                SymbolNode(
                    position=module_part_token.position,
                    name=module_part_token,
                )
            )
            while dot := self.parse_token(TokenType.DOT):
                if self._peek().type == TokenType.SYMBOL:
                    module_part_token = self._read()
                    module_parts.append(
                        SymbolNode(
                            position=module_part_token.position,
                            name=module_part_token,
                        )
                    )
                else:
                    self._raise_parse_error(
                        message="Expected module name part after '.' in import statement",
                        position=dot.position,
                    )
        elif self._peek().type == TokenType.STRING_LITERAL:
            filename_token = self._read()
            filename = StringLiteralNode(
                position=filename_token.position,
                contents=filename_token,
            )
        elif self._peek().type in (TokenType.LIST_START, TokenType.INDEXING_START):
            self._read()  # consume LIST_START
            filename_expr = self.parse_value_expression()
            self.require_any_token([TokenType.LIST_END, TokenType.INDEXING_END])
        elif self._peek().type == TokenType.MODULE:
            self._read()  # consume MODULE
            module_expr = self.parse_value_expression()
        else:
            self._raise_parse_error(
                message=f"Expected module name or filename in import statement. Unexpected token {self._peek().pretty()}"
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
            alias_token = self.require_token(TokenType.SYMBOL)
            alias = SymbolNode(
                position=alias_token.position,
                name=alias_token,
            )
        elif module_expr:
            self._raise_parse_error(
                message="Dynamic import statement must have an alias",
                position=start_position,
            )
        elif filename or filename_expr:
            self._raise_parse_error(
                message="Import statement with filename must have an alias",
                position=start_position,
            )

        return ImportStatementNode(
            position=start_position,
            module_parts=module_parts,
            module_expr=module_expr,
            filename=filename,
            filename_expr=filename_expr,
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
            name_token = self.require_token(TokenType.SYMBOL)
            name = SymbolNode(
                position=name_token.position,
                name=name_token,
            )
            alias: SymbolNode | None = None
            if self.parse_token(TokenType.AS):
                alias_token = self.require_token(TokenType.SYMBOL)
                alias = SymbolNode(
                    position=alias_token.position,
                    name=alias_token,
                )
            field = ImportStatementFieldNode(
                position=name.position,
                name=name,
                alias=alias,
            )
        return field

    def parse_assignment(
        self,
    ) -> AssignmentNode | TypeAnnotationNode | None:
        start_position = self._position
        if self._peek().type not in (
            TokenType.SYMBOL,
            TokenType.LIST_START,
        ) and not (
            self._peek().type == TokenType.LOCAL
            and self._peek(1).type in (TokenType.SYMBOL, TokenType.LIST_START)
        ):
            return None

        local = False
        type_annotation: TypeExpressionNodeType | None = None
        value: ValueExpressionNodeType | None = None

        if self._peek().type == TokenType.LOCAL:
            local = True
            self._read()  # consume LOCAL

        target: SymbolNode | None = None
        target_expr: ValueExpressionNodeType | None = None
        if target_token := self.parse_token(TokenType.SYMBOL):
            target = SymbolNode(
                position=target_token.position,
                name=target_token,
            )
        elif self._peek().type == TokenType.LIST_START:
            self._read()
            target_expr = self.parse_value_expression()
            self.require_token(TokenType.LIST_END)

        if self._peek().type == TokenType.COLON:
            self._read()  # consume COLON
            type_annotation = self.parse_type_expression()

        if self._peek().type == TokenType.ASSIGN:
            self._read()  # consume ASSIGN
            value = self.parse_value_expression()

        if value is not None:
            return AssignmentNode(
                position=start_position,
                target=target,
                target_expr=target_expr,
                value=value,
                type_annotation=type_annotation,
                local=local,
            )
        elif type_annotation is not None:
            return TypeAnnotationNode(
                position=start_position,
                name=target,
                name_expr=target_expr,
                type_annotation=type_annotation,
                local=local,
            )
        else:
            self._raise_parse_error(
                message="Assignment must have a value and/or a type annotation",
                position=start_position,
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
                element_parser=self.parse_type_expression,
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
        name = SymbolNode(
            position=start_position, name=self.require_token(TokenType.SYMBOL)
        )
        constraint: TypeExpressionNodeType | None = None

        if self.parse_token(TokenType.COLON):
            constraint = self.parse_type_expression()

        return GenericTypeParameterNode(
            position=start_position,
            name=name,
            constraint=constraint,
        )

    def parse_type_atom(self) -> TypeExpressionNodeType:
        for type_atom_parser in self._type_atom_parsers:
            if type_expr := type_atom_parser():
                return type_expr
        self._raise_parse_error(
            message=f"Expected type expression. Unexpected token {self._peek().pretty()}"
        )

    def parse_type_name(self) -> TypeExpressionNodeType | None:
        if token := self.parse_token(TokenType.SYMBOL):
            return TypeNameNode(
                position=token.position,
                name=token,
            )
        return None

    def parse_parenthesized_type_expression(
        self,
    ) -> ParenthesizedTypeExpressionNode | TupleTypeNode | None:
        start_position = self._position
        if not self.parse_any_token(
            [TokenType.PARENTHESES_START, TokenType.FUNCTION_CALL_START]
        ):
            return None

        type_expressions = self.parse_comma_or_newline_separated(
            element_parser=self.parse_type_expression,
            ending_tokens=[TokenType.PARENTHESES_END, TokenType.FUNCTION_CALL_END],
        )

        if len(type_expressions) == 1:
            return ParenthesizedTypeExpressionNode(
                position=start_position,
                expression=type_expressions[0],
            )
        else:
            return TupleTypeNode(
                position=start_position,
                elements=type_expressions,
            )

    def parse_type_type_expression(self) -> TypeTypeExpressionNode | None:
        start_position = self._position
        if not (self.parse_token(TokenType.TYPE)):
            return None
        expression = self.parse_value_expression()
        return TypeTypeExpressionNode(
            position=start_position,
            expression=expression,
        )

    def parse_typeof_expression(self) -> TypeOfExpressionNode | None:
        start_position = self._position
        if not (self.parse_token(TokenType.TYPEOF)):
            return None
        expression = self.parse_value_expression()
        return TypeOfExpressionNode(
            position=start_position,
            expression=expression,
        )

    def parse_const_expression(self) -> ConstExpressionNode | None:
        start_position = self._position
        if not (self.parse_token(TokenType.CONST)):
            return None
        expression = self.parse_value_expression()
        return ConstExpressionNode(
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
            element_parser=self.parse_record_entry,
            ending_token=TokenType.OBJECT_END,
        )

        return RecordTypeNode(
            position=start_position,
            fields=fields,
        )

    def parse_record_entry(self) -> TypeAnnotationNode | SpreadTypeExpressionNode:
        entry: TypeAnnotationNode | SpreadTypeExpressionNode
        if spread_type := self.parse_spread_type_expression():
            entry = spread_type
        elif type_annotation := self.parse_assignment():
            if (
                not isinstance(type_annotation, TypeAnnotationNode)
                or type_annotation.local
            ):
                self._raise_parse_error(
                    message="Each entry of a record type must be an annotation of the form 'name : Type'",
                )
                raise RuntimeError("unreachable")  # appease type checker
            entry = type_annotation
        else:
            self._raise_parse_error(
                message="Expected type annotation or spread type expression in record type",
            )
        return entry

    def parse_function_type(self) -> FunctionTypeNode | None:
        start_position = self._position
        if not self.parse_token(TokenType.FUN):
            return None
        self.require_token(TokenType.PARENTHESES_START)

        parameters = self.parse_comma_or_newline_separated(
            element_parser=self.parse_function_parameter,
            ending_token=TokenType.PARENTHESES_END,
        )

        if not self.parse_token(TokenType.ARROW):
            self._raise_parse_error(
                message="Expected '->' after function parameter list in function type",
                position=start_position,
            )

        return_type = self.parse_type_expression()
        return FunctionTypeNode(
            position=start_position,
            parameters=parameters,
            return_type=return_type,
        )

    def parse_function_parameter(self) -> FunctionParameterNode:
        start_position = self._position
        name: SymbolNode | None = None
        optional = False

        if self._peek().type == TokenType.SYMBOL and self._peek(1).type in (
            TokenType.COLON,
            TokenType.QUESTION,
        ):
            name_token = self._read()
            name = SymbolNode(
                position=name_token.position,
                name=name_token,
            )

            if self.parse_token(TokenType.QUESTION):
                optional = True

        if self._peek().type == TokenType.COLON:
            self._read()  # consume COLON
        elif name:
            self._raise_parse_error(
                message="Expected ':' after parameter name in function type",
            )

        type_annotation = self.parse_type_expression()
        return FunctionParameterNode(
            position=start_position,
            name=name,
            optional=optional,
            type_annotation=type_annotation,
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
        if self.parse_token(TokenType.NOT):
            operand = self.parse_descend_expr_not()
            return UnaryOperationNode(
                position=operand.position,
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
        if op_token := self.parse_any_token([TokenType.PLUS, TokenType.MINUS]):
            operand = self.parse_descend_expr_pos_neg()
            op = (
                Operator.POSITIVE
                if op_token.type == TokenType.PLUS
                else Operator.NEGATIVE
            )
            return UnaryOperationNode(
                position=operand.position,
                operator=op,
                operand=operand,
            )
        return self.parse_descend_expr_pow()

    def parse_descend_expr_pow(self) -> ValueExpressionNodeType:
        lhs = self.parse_descend_expr_spread()
        while self.parse_token(TokenType.EXPONENTIATION):
            rhs = self.parse_descend_expr_pow()
            lhs = BinaryOperationNode(
                position=lhs.position,
                left=lhs,
                operator=Operator.EXPONENTIATION,
                right=rhs,
            )
        return lhs

    def parse_descend_expr_spread(self) -> ValueExpressionNodeType:
        if self.parse_token(TokenType.ELLIPSIS):
            operand = self.parse_descend_expr_spread()
            return UnaryOperationNode(
                position=operand.position,
                operator=Operator.SPREAD,
                operand=operand,
            )
        return self.parse_atom()

    def parse_atom(self) -> AtomNodeType:
        for atom_parser in self._atom_parsers:
            if value := atom_parser():
                return value
        self._raise_parse_error(
            message=f"Expected expression. Unexpected token {self._peek().pretty()}"
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
            element_parser=self.parse_value_expression,
            ending_token=TokenType.LIST_END,
        )

        return ListLiteralNode(
            position=start_position,
            elements=elements,
        )

    def parse_parenthesized_expression(
        self,
    ) -> ParenthesizedExpressionNode | TupleLiteralNode | None:
        start_position = self._position
        if not self.parse_token(TokenType.PARENTHESES_START):
            return None

        expressions = self.parse_comma_or_newline_separated(
            element_parser=self.parse_value_expression,
            ending_token=TokenType.PARENTHESES_END,
        )

        if len(expressions) == 1:
            return ParenthesizedExpressionNode(
                position=start_position,
                expression=expressions[0],
            )
        else:
            return TupleLiteralNode(
                position=start_position,
                elements=expressions,
            )

    def parse_null_literal(self) -> NullLiteralNode | None:
        token = self._peek()
        if token.type != TokenType.NULL:
            return None
        token = self._read()
        return NullLiteralNode(
            position=token.position,
            contents=token,
        )

    def parse_boolean_literal(self) -> BooleanLiteralNode | None:
        token = self._peek()
        if token.type not in {TokenType.TRUE, TokenType.FALSE}:
            return None
        token = self._read()
        return BooleanLiteralNode(
            position=token.position,
            contents=token,
        )

    def parse_number_literal(self) -> NumberLiteralNode | None:
        token = self._peek()
        if token.type not in {
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
        if not (token := self.parse_token(TokenType.STRING_LITERAL)):
            return None
        return StringLiteralNode(
            position=token.position,
            contents=token,
        )

    def parse_symbol(self) -> SymbolNode | None:
        if not (token := self.parse_token(TokenType.SYMBOL)):
            return None
        return SymbolNode(
            position=token.position,
            name=token,
        )

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
                assert isinstance(element, Node)
                if self._peek().position.line == element.position.line:
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

    def require_any_token(self, expected_types: list[TokenType]) -> Token:
        token = self.parse_any_token(expected_types)
        if token is None:
            expected_names = ", ".join(t.name for t in expected_types)
            message = (
                f"Expected token of type {expected_names}. Unexpected token {self._peek().pretty()}"
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
                f"Expected token of type {expected_type.name}. Unexpected token {self._peek().pretty()}"
                if self._peek().type != TokenType.EOF
                else f"Expected token of type {expected_type.name}. Unexpected end of file"
            )
            self._raise_parse_error(message=message)
            raise RuntimeError("unreachable")  # appease type checker
        return token

    def at_end(self) -> bool:
        return self._peek().type == TokenType.EOF

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
