from typing import Callable, NoReturn
from radical.data.parser.ast import (
    AssignmentNode,
    BooleanLiteralNode,
    ModuleNode,
    NullLiteralNode,
    NumberLiteralNode,
    ParenthesizedExpressionNode,
    StringLiteralNode,
    SymbolNode,
    TopLevelDeclarationNodeType,
    TupleLiteralNode,
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

        self._top_level_declaration_parsers: list[
            Callable[[], TopLevelDeclarationNodeType | None]
        ] = [
            self.parse_local_assignment,
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

    def parse_local_assignment(self) -> LocalAssignmentNode | None:
        if not self.parse_token(TokenType.LOCAL):
            return None
        target = self.require_token(TokenType.SYMBOL)
        self.require_token(TokenType.ASSIGN)
        value = self.parse_value_expression()
        return LocalAssignmentNode(
            position=target.position,
            target=SymbolNode(
                position=target.position,
                name=target,
            ),
            value=value,
        )

    def parse_assignment(self) -> AssignmentNode | None:
        if not (target := self.parse_symbol()):
            return None
        self.require_token(TokenType.ASSIGN)
        value = self.parse_value_expression()
        return AssignmentNode(
            position=target.position,
            target=target,
            value=value,
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
                position=expressions[0].position,
                expression=expressions[0],
            )
        else:
            return TupleLiteralNode(
                position=expressions[0].position,
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
