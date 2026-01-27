from typing import NoReturn
from radical.data.parser.ast import (
    AssignmentNode,
    ModuleNode,
    StringLiteralNode,
    SymbolNode,
    TopLevelDeclarationNodeType,
    ValueExpressionNodeType,
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
        return self.parse_assignment()

    def parse_assignment(self) -> AssignmentNode:
        target = self.parse_token(TokenType.SYMBOL)
        self.parse_token(TokenType.ASSIGN)
        value = self.parse_value_expression()
        return AssignmentNode(
            position=target.position,
            target=SymbolNode(
                position=target.position,
                name=target,
            ),
            value=value,
        )

    def parse_value_expression(self) -> ValueExpressionNodeType:
        next_token = self._peek()
        if next_token.type == TokenType.SYMBOL:
            return self.parse_symbol()
        elif next_token.type == TokenType.STRING_LITERAL:
            return self.parse_string_literal()
        else:
            self._raise_parse_error(
                message=f"Expected value expression. Unexpected token '{next_token.value}'",
                position=next_token.position,
            )

    def parse_symbol(self) -> SymbolNode:
        token = self.parse_token(TokenType.SYMBOL)
        return SymbolNode(
            position=token.position,
            name=token,
        )

    def parse_string_literal(self) -> StringLiteralNode:
        token = self.parse_token(TokenType.STRING_LITERAL)
        return StringLiteralNode(
            position=token.position,
            contents=token,
        )

    def parse_token(self, expected_type: TokenType) -> Token:
        token = self._read()
        if token.type != expected_type:
            self._raise_parse_error(
                message=f"Expected token of type {expected_type.name}, but got '{token.value}'",
                position=token.position,
            )
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
