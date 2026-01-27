from typing import Callable, NoReturn
from radical.data.parser.ast import (
    AssignmentNode,
    ModuleNode,
    NumberLiteralNode,
    StringLiteralNode,
    SymbolNode,
    TopLevelDeclarationNodeType,
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
        return self.parse_descend_expr_add()

    def parse_descend_expr_add(self) -> ValueExpressionNodeType:
        lhs = self.parse_descend_expr_mult()
        while True:
            if not self.parse_token(TokenType.PLUS):
                return lhs
            rhs = self.parse_descend_expr_mult()
            lhs = BinaryOperationNode(
                position=lhs.position,
                left=lhs,
                operator=Operator.PLUS,
                right=rhs,
            )

    def parse_descend_expr_mult(self) -> ValueExpressionNodeType:
        lhs = self.parse_atom()
        while True:
            if not self.parse_token(TokenType.MULTIPLY):
                return lhs
            rhs = self.parse_atom()
            lhs = BinaryOperationNode(
                position=lhs.position,
                left=lhs,
                operator=Operator.MULTIPLY,
                right=rhs,
            )

    def parse_atom(self) -> AtomNodeType:
        for atom_parser in self._atom_parsers:
            if value := atom_parser():
                return value
        self._raise_parse_error(
            message=f"Expected atom. Unexpected token '{self._peek().value}'"
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
