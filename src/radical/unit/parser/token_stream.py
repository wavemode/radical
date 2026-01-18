from typing import NoReturn
from radical.data.parser.errors import ParseError
from radical.data.parser.position import Position
from radical.data.parser.token import Token, TokenType
from radical.util.core.unit import Unit


class TokenStream(Unit):
    def __init__(self, contents: str, filename: str) -> None:
        super().__init__()
        self._contents = contents
        self._filename = filename
        self._tokens: list[Token] = []
        self._index = 0
        self._line = 1
        self._column = 1
        self._indent_level = 0
        self._seen_non_whitespace = False
        self._tokenize()

    def _tokenize(self) -> None:
        while not self._at_end():
            char = self._peek()
            next_char = self._peek(2)
            if char == "\n":
                self._advance_newline()
            elif char.isspace():
                self._advance_whitespace()
            elif char == "(" and next_char == "*":
                self._handle_multiline_comment()
            elif char == "-" and next_char == "-":
                self._handle_singleline_comment()
            elif char.isalpha() or char == "_":
                self._handle_word()
            else:
                self._raise_parse_error(f"Unexpected character: '{char}'")
        self._add_token(TokenType.EOF, "", self._position())

    _KEYWORDS = {
        "if",
        "then",
        "else",
        "for",
        "in",
        "and",
        "or",
        "not",
        "true",
        "false",
        "null",
        "type",
        "typeof",
        "fun",
        "let",
        "try",
        "catch",
        "finally",
        "raise",
        "assert",
        "data",
        "case",
        "of",
        "import",
        "as",
    }

    def _handle_word(self) -> None:
        start_position = self._position()
        start_index = self._index
        while self._peek().isalnum() or self._peek() == "_":
            self._advance_non_whitespace()
        word = self._contents[start_index : self._index]
        if word in self._KEYWORDS:
            self._add_token(TokenType(word), word, start_position)
        else:
            self._add_token(TokenType.SYMBOL, word, start_position)

    def _handle_multiline_comment(self) -> None:
        self._advance_whitespace(2)  # Skip '(*'
        while not self._at_end():
            if self._peek() == "(" and self._peek(2) == "*":
                self._handle_multiline_comment()
            elif self._peek() == "*" and self._peek(2) == ")":
                self._advance_whitespace(2)  # Skip '*)'
                return
            elif self._peek() == "\n":
                self._advance_newline()
            else:
                self._advance_whitespace()
        self._raise_parse_error("Unterminated multiline comment")

    def _handle_singleline_comment(self) -> None:
        self._advance_whitespace(2)  # Skip '--'
        while not self._at_end() and self._peek() != "\n":
            self._advance_whitespace()

    def _peek(self, n: int = 1) -> str:
        return (
            self._contents[self._index + n - 1]
            if self._index + n - 1 < len(self._contents)
            else ""
        )

    def _at_end(self) -> bool:
        return self._index >= len(self._contents)

    def _advance_non_whitespace(self, n: int = 1) -> None:
        self._index += n
        self._column += n
        self._seen_non_whitespace = True
        pass

    def _advance_whitespace(self, n: int = 1) -> None:
        self._index += n
        self._column += n
        if not self._seen_non_whitespace:
            self._indent_level += n
        pass

    def _advance_newline(self) -> None:
        self._index += 1
        self._line += 1
        self._column = 1
        self._seen_non_whitespace = False
        self._indent_level = 0
        pass

    def _position(self) -> Position:
        return Position(
            line=self._line,
            column=self._column,
            indent_level=self._indent_level,
            seen_non_whitespace=self._seen_non_whitespace,
        )

    def _add_token(self, token_type: TokenType, value: str, position: Position) -> None:
        token = Token(position=position, type=token_type, value=value)
        self._tokens.append(token)

    def _raise_parse_error(
        self, message: str, position: Position | None = None
    ) -> NoReturn:
        raise ParseError(
            message=message,
            filename=self._filename,
            position=(
                position
                if position is not None
                else Position(
                    line=self._line,
                    column=self._column,
                    indent_level=self._indent_level,
                    seen_non_whitespace=self._seen_non_whitespace,
                )
            ),
        )
