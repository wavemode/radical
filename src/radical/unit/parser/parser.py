from typing import Callable, NoReturn
from radical.data.parser.ast import (
    AssignmentNode,
    BooleanLiteralNode,
    ConstExpressionNode,
    FunctionParameterNode,
    FunctionTypeNode,
    GenericTypeApplicationNode,
    GenericTypeExpressionNode,
    GenericTypeParameterNode,
    ImportStatementNode,
    ListLiteralNode,
    LocalTypeAnnotationNode,
    ModuleNode,
    NullLiteralNode,
    NumberLiteralNode,
    ParenthesizedExpressionNode,
    ParenthesizedTypeExpressionNode,
    RecordTypeNode,
    SpreadTypeExpressionNode,
    StringLiteralNode,
    SymbolNode,
    TopLevelDeclarationNodeType,
    TupleLiteralNode,
    TupleTypeNode,
    TypeAnnotationNode,
    TypeOfExpressionNode,
    TypeTypeExpressionNode,
    TypeExpressionNodeType,
    TypeNameNode,
    TypeUnionNode,
    UnaryOperationNode,
    ValueExpressionNodeType,
    LocalAssignmentNode,
    AtomNodeType,
    BinaryOperationNode,
    Operator,
)
from radical.data.parser.errors import ParseError
from radical.data.parser.position import Position
from radical.data.parser.token import Token, TokenType
from radical.unit.parser.lexer import Lexer
from radical.util.core.unit import Unit


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

    def parse_import_statement(self) -> ImportStatementNode | None:
        start_position = self._position
        if not self.parse_token(TokenType.IMPORT):
            return None
        if not (module_name := self.parse_symbol()):
            self._raise_parse_error(
                message="Expected module name after 'import' statement",
            )
            raise RuntimeError("unreachable")  # appease type checker

        module_parts: list[SymbolNode] = [module_name]
        while dot := self.parse_token(TokenType.DOT):
            if not (part := self.parse_symbol()):
                self._raise_parse_error(
                    message="Expected module name part after '.' in import statement",
                    position=dot.position,
                )
                raise RuntimeError("unreachable")  # appease type checker
            module_parts.append(part)

        return ImportStatementNode(
            position=start_position,
            module_parts=module_parts,
        )

    def parse_assignment(
        self,
    ) -> (
        AssignmentNode
        | LocalAssignmentNode
        | TypeAnnotationNode
        | LocalTypeAnnotationNode
        | None
    ):
        start_position = self._position
        if self._peek().type not in (
            TokenType.SYMBOL,
            TokenType.LOCAL,
            TokenType.LIST_START,
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

        if local:
            if type_annotation is not None and value is None:
                return LocalTypeAnnotationNode(
                    position=start_position,
                    name=target,
                    name_expr=target_expr,
                    type=type_annotation,
                )
            elif value is not None:
                return LocalAssignmentNode(
                    position=start_position,
                    target=target,
                    target_expr=target_expr,
                    value=value,
                    type_annotation=type_annotation,
                )
            else:
                self._raise_parse_error(
                    message="Local declaration must have a type annotation and/or an assignment",
                    position=start_position,
                )
        else:
            if value is not None:
                return AssignmentNode(
                    position=start_position,
                    target=target,
                    target_expr=target_expr,
                    value=value,
                    type_annotation=type_annotation,
                )
            elif type_annotation is not None:
                return TypeAnnotationNode(
                    position=start_position,
                    name=target,
                    name_expr=target_expr,
                    type=type_annotation,
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
            arguments: list[TypeExpressionNodeType] = []
            while not self.parse_any_token(
                [TokenType.LIST_END, TokenType.INDEXING_END]
            ):
                argument = self.parse_type_expression()
                arguments.append(argument)

                if self.parse_any_token([TokenType.LIST_END, TokenType.INDEXING_END]):
                    break

                if self.parse_token(TokenType.COMMA):
                    if self.parse_any_token(
                        [TokenType.LIST_END, TokenType.INDEXING_END]
                    ):
                        break
                else:
                    if self._peek().position.line == argument.position.line:
                        self._raise_parse_error(
                            message="Generic type arguments must be separated by a comma and/or newline"
                        )

            lhs = GenericTypeApplicationNode(
                position=start_position,
                generic_type=lhs,
                arguments=arguments,
            )
        return lhs

    def parse_descend_type_expr_generic(self) -> TypeExpressionNodeType:
        start_position = self._position
        if not self.parse_token(TokenType.LIST_START):
            return self.parse_type_atom()

        parameters: list[GenericTypeParameterNode] = []
        while not self.parse_token(TokenType.LIST_END):
            parameter = self.parse_generic_type_parameter()
            parameters.append(parameter)

            if self.parse_token(TokenType.LIST_END):
                break

            if self.parse_token(TokenType.COMMA):
                if self.parse_token(TokenType.LIST_END):
                    break
            else:
                if self._peek().position.line == parameter.position.line:
                    self._raise_parse_error(
                        message="Generic type parameters must be separated by a comma and/or newline"
                    )

        expression = self.parse_descend_type_expr_generic()
        return GenericTypeExpressionNode(
            position=start_position,
            expression=expression,
            parameters=parameters,
        )

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

        type_expressions: list[TypeExpressionNodeType] = []
        while not self.parse_any_token(
            [TokenType.PARENTHESES_END, TokenType.FUNCTION_CALL_END]
        ):
            type_expr = self.parse_type_expression()
            type_expressions.append(type_expr)

            if self.parse_any_token(
                [TokenType.PARENTHESES_END, TokenType.FUNCTION_CALL_END]
            ):
                break

            if (not self.parse_token(TokenType.COMMA)) and (
                self._peek().position.line == type_expr.position.line
            ):
                self._raise_parse_error(
                    message="Tuple type elements must be separated by a comma and/or newline"
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
            type=type_expr,
        )

    def parse_record_type(self) -> RecordTypeNode | None:
        start_position = self._position
        if not self.parse_token(TokenType.OBJECT_START):
            return None

        fields: list[TypeAnnotationNode | SpreadTypeExpressionNode] = []
        while not self.parse_token(TokenType.OBJECT_END):
            entry: TypeAnnotationNode | SpreadTypeExpressionNode
            if spread_type := self.parse_spread_type_expression():
                entry = spread_type
            elif type_annotation := self.parse_assignment():
                if not isinstance(type_annotation, TypeAnnotationNode):
                    self._raise_parse_error(
                        message="Each entry of a record type must be an annotation of the form 'name : Type'",
                    )
                    raise RuntimeError("unreachable")  # appease type checker
                entry = type_annotation
            else:
                self._raise_parse_error(
                    message="Expected type annotation or spread type expression in record type",
                )
            fields.append(entry)

            if self.parse_token(TokenType.OBJECT_END):
                break

            if self.parse_token(TokenType.COMMA):
                if self.parse_token(TokenType.OBJECT_END):
                    break
            else:
                if self._peek().position.line == entry.position.line:
                    self._raise_parse_error(
                        message="Record type fields must be separated by a comma and/or newline"
                    )

        return RecordTypeNode(
            position=start_position,
            fields=fields,
        )

    def parse_function_type(self) -> FunctionTypeNode | None:
        start_position = self._position
        if not self.parse_token(TokenType.FUN):
            return None
        self.require_token(TokenType.PARENTHESES_START)

        parameters: list[FunctionParameterNode] = []
        while not self.parse_token(TokenType.PARENTHESES_END):
            parameter = self.parse_function_parameter()
            parameters.append(parameter)

            if self.parse_token(TokenType.PARENTHESES_END):
                break

            if self.parse_token(TokenType.COMMA):
                if self.parse_token(TokenType.PARENTHESES_END):
                    break
            else:
                if self._peek().position.line == parameter.position.line:
                    self._raise_parse_error(
                        message="Function parameters must be separated by a comma and/or newline"
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

    def parse_list_literal(self) -> ListLiteralNode | None:
        start_position = self._position
        if not self.parse_token(TokenType.LIST_START):
            return None

        elements: list[ValueExpressionNodeType] = []
        while not self.parse_token(TokenType.LIST_END):
            element = self.parse_value_expression()
            elements.append(element)

            if self.parse_token(TokenType.LIST_END):
                break

            if (not self.parse_token(TokenType.COMMA)) and (
                self._peek().position.line == element.position.line
            ):
                self._raise_parse_error(
                    message="List elements must be separated by a comma and/or newline"
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
        expressions: list[ValueExpressionNodeType] = []
        while not self.parse_token(TokenType.PARENTHESES_END):
            expr = self.parse_value_expression()
            expressions.append(expr)

            if self.parse_token(TokenType.PARENTHESES_END):
                break

            if (not self.parse_token(TokenType.COMMA)) and (
                self._peek().position.line == expr.position.line
            ):
                self._raise_parse_error(
                    message="Tuple elements must be separated by a comma and/or newline"
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

    def require_token(self, expected_type: TokenType) -> Token:
        token = self.parse_token(expected_type)
        if token is None:
            self._raise_parse_error(
                message=f"Expected token of type {expected_type.name}. Unexpected token {self._peek().pretty()}"
            )
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
