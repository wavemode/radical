from typing import Callable, NoReturn
from radical.data.parser.ast import (
    AssignmentNode,
    BooleanLiteralNode,
    ConstExpressionNode,
    LocalTypeAnnotationNode,
    ModuleNode,
    NullLiteralNode,
    NumberLiteralNode,
    ParenthesizedExpressionNode,
    ParenthesizedTypeExpressionNode,
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
        ]

        self._type_atom_parsers: list[Callable[[], TypeExpressionNodeType | None]] = [
            self.parse_type_name,
            self.parse_parenthesized_type_expression,
            self.parse_type_type_expression,
            self.parse_typeof_expression,
            self.parse_const_expression,
            self.parse_spread_type_expression,
        ]

        self._top_level_declaration_parsers: list[
            Callable[[], TopLevelDeclarationNodeType | None]
        ] = [
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
            message=f"Expected top level declaration. Unexpected token '{self._peek().value}'"
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
        if self._peek().type not in (TokenType.SYMBOL, TokenType.LOCAL):
            return None

        local = False
        type_annotation: TypeExpressionNodeType | None = None
        value: ValueExpressionNodeType | None = None

        if self._peek().type == TokenType.LOCAL:
            local = True
            self._read()  # consume LOCAL

        target_token = self.require_token(TokenType.SYMBOL)
        target = SymbolNode(
            position=target_token.position,
            name=target_token,
        )

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
                    type=type_annotation,
                )
            elif value is not None:
                return LocalAssignmentNode(
                    position=start_position,
                    target=target,
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
                    value=value,
                    type_annotation=type_annotation,
                )
            elif type_annotation is not None:
                return TypeAnnotationNode(
                    position=start_position,
                    name=target,
                    type=type_annotation,
                )
            else:
                self._raise_parse_error(
                    message="Assignment must have a value and/or a type annotation",
                    position=start_position,
                )

    def parse_type_expression(self) -> TypeExpressionNodeType:
        return self.parse_type_atom()

    def parse_type_atom(self) -> TypeExpressionNodeType:
        for type_atom_parser in self._type_atom_parsers:
            if type_expr := type_atom_parser():
                return type_expr
        self._raise_parse_error(
            message=f"Expected type expression. Unexpected token '{self._peek().value}'"
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
        if not self.parse_token(TokenType.PARENTHESES_START):
            return None

        type_expressions: list[TypeExpressionNodeType] = []
        while not self.parse_token(TokenType.PARENTHESES_END):
            type_expr = self.parse_type_expression()
            type_expressions.append(type_expr)

            if self.parse_token(TokenType.PARENTHESES_END):
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
        lhs = self.parse_atom()
        while self.parse_token(TokenType.EXPONENTIATION):
            rhs = self.parse_descend_expr_pow()
            lhs = BinaryOperationNode(
                position=lhs.position,
                left=lhs,
                operator=Operator.EXPONENTIATION,
                right=rhs,
            )
        return lhs

    def parse_atom(self) -> AtomNodeType:
        for atom_parser in self._atom_parsers:
            if value := atom_parser():
                return value
        self._raise_parse_error(
            message=f"Expected expression. Unexpected token '{self._peek().value}'"
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
                message=f"Expected token of type {expected_type.name}. Unexpected token '{self._peek().value}'"
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
