from typing import NoReturn
from radical.data.parser.errors import ParseError
from radical.data.parser.position import Position
from radical.data.parser.token import Token, TokenType
from radical.util.core.unit import Unit


class Lexer(Unit):

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
        self._token_index = 0

    def peek(self, n: int = 0) -> Token:
        while len(self._tokens) <= self._token_index + n:
            if self._at_end():
                return self._tokens[-1]
            self._read_token()
        return self._tokens[self._token_index + n]

    def read(self) -> Token:
        token = self.peek()
        self._token_index += 1
        return token

    def read_all(self) -> list[Token]:
        while not self._at_end():
            self._read_token()
        return self._tokens[:]

    def _read_token(self) -> None:
        if self._at_end():
            self._raise_parse_error("Unexpected end of input")

        char = self._peek_char()
        next_char = self._peek_char(1)
        if char == "\n":
            self._advance_newline()
        elif char.isspace():
            self._advance_whitespace()
        elif char == "(" and next_char == "*":
            self._read_multiline_comment()
        elif char == "-" and next_char == "-":
            self._read_singleline_comment()
        elif char == ",":
            self._add_token(TokenType.COMMA, char)
            self._advance_non_whitespace()
        elif char == ":":
            self._add_token(TokenType.COLON, char)
            self._advance_non_whitespace()
        elif char == "|" and next_char == ">":
            self._add_token(TokenType.PIPE, "|>")
            self._advance_non_whitespace(2)
        elif char == "|":
            self._add_token(TokenType.VARIANT, char)
            self._advance_non_whitespace()
        elif char == "-" and next_char == ">":
            self._add_token(TokenType.ARROW, "->")
            self._advance_non_whitespace(2)
        elif char == "." and next_char == "." and self._peek_char(2) == ".":
            self._add_token(TokenType.ELLIPSIS, "...")
            self._advance_non_whitespace(3)
        elif char == "?":
            self._add_token(TokenType.QUESTION, char)
            self._advance_non_whitespace()
        elif char == "." and self._previous_char_was_expression():
            self._add_token(TokenType.DOT, char)
            self._advance_non_whitespace()
        elif char == "*" and next_char == "*":
            self._add_token(TokenType.EXPONENTIATION, "**")
            self._advance_non_whitespace(2)
        elif char == "*":
            self._add_token(TokenType.MULTIPLY, char)
            self._advance_non_whitespace()
        elif char == "/" and next_char == "/":
            self._add_token(TokenType.FLOOR_DIVIDE, "//")
            self._advance_non_whitespace(2)
        elif char == "/":
            self._add_token(TokenType.DIVIDE, char)
            self._advance_non_whitespace()
        elif char == "%":
            self._add_token(TokenType.MODULO, char)
            self._advance_non_whitespace()
        elif char == "+":
            self._add_token(TokenType.PLUS, char)
            self._advance_non_whitespace()
        elif char == "-":
            self._add_token(TokenType.MINUS, char)
            self._advance_non_whitespace()
        elif char == "=" and next_char == "=":
            self._add_token(TokenType.EQUAL, "==")
            self._advance_non_whitespace(2)
        elif char == "!" and next_char == "=":
            self._add_token(TokenType.NOT_EQUAL, "!=")
            self._advance_non_whitespace(2)
        elif char == "<" and next_char == "=":
            self._add_token(TokenType.LESS_THAN_EQUAL, "<=")
            self._advance_non_whitespace(2)
        elif char == ">" and next_char == "=":
            self._add_token(TokenType.GREATER_THAN_EQUAL, ">=")
            self._advance_non_whitespace(2)
        elif char == "<":
            self._add_token(TokenType.LESS_THAN, char)
            self._advance_non_whitespace()
        elif char == ">":
            self._add_token(TokenType.GREATER_THAN, char)
            self._advance_non_whitespace()
        elif char == "=":
            self._add_token(TokenType.ASSIGN, char)
            self._advance_non_whitespace()
        elif char == "@":
            self._add_token(TokenType.AT, char)
            self._advance_non_whitespace()
        elif (
            char == "f"
            and next_char == '"'
            and self._peek_char(2) == '"'
            and self._peek_char(3) == '"'
        ):
            self._read_multiline_format_string_literal()
        elif char == "f" and next_char == '"':
            self._read_format_string_literral()
        elif (
            char == "r"
            and next_char == '"'
            and self._peek_char(2) == '"'
            and self._peek_char(3) == '"'
        ):
            self._read_raw_multiline_string_literal()
        elif char == '"' and next_char == '"' and self._peek_char(2) == '"':
            self._read_multiline_string_literal()
        elif char == "r" and next_char == '"':
            self._read_raw_string_literal()
        elif char == '"':
            self._read_string_literal()
        elif char == "(":
            if self._previous_char_was_expression():
                self._read_function_call_expression()
            else:
                self._read_parentheses_expression()
        elif char == "[":
            if self._previous_char_was_expression():
                self._read_indexing_expression()
            else:
                self._read_list_expression()
        elif char == "{":
            self._read_object_expression()
        elif char == "`":
            self._read_quoted_symbol()
        elif char.isdigit():
            self._read_number()
        elif char.isalpha() or char == "_":
            self._read_word()
        else:
            self._raise_parse_error(f"Unexpected character: '{char}'")

        if self._at_end():
            self._add_token(TokenType.EOF, "", self._position())

    def _read_multiline_format_string_literal(self) -> None:
        start_position = self._position()
        self._advance_non_whitespace(4)  # Skip opening f"""
        self._add_token(TokenType.MULTILINE_FORMAT_STRING_START, 'f"""', start_position)
        while not (
            self._peek_char() == '"'
            and self._peek_char(1) == '"'
            and self._peek_char(2) == '"'
        ):
            if self._at_end():
                self._raise_parse_error(
                    "Unterminated multiline format string", start_position
                )
            elif self._peek_char() == "{":
                self._read_format_string_expression()
            else:
                self._read_multiline_format_string_section()
        self._add_token(TokenType.MULTILINE_FORMAT_STRING_END, '"""')
        self._advance_non_whitespace(3)  # Skip closing """

    def _read_multiline_format_string_section(self) -> None:
        start_position = self._position()
        string_chars: list[str] = []
        while self._peek_char() not in ("{", '"'):
            if self._at_end():
                self._raise_parse_error("Unterminated format string", start_position)
            string_chars.append(self._read_format_string_char())
        string_value = "".join(string_chars)
        self._add_token(
            TokenType.MULTILINE_FORMAT_STRING_SECTION, string_value, start_position
        )

    def _read_format_string_literral(self) -> None:
        start_position = self._position()
        self._add_token(TokenType.FORMAT_STRING_START, 'f"', start_position)
        self._advance_non_whitespace(2)  # Skip opening f"
        while not (self._peek_char() == '"'):
            if self._at_end() or self._peek_char() == "\n":
                self._raise_parse_error("Unterminated format string", start_position)
            elif self._peek_char() == "{":
                self._read_format_string_expression()
            else:
                self._read_format_string_section()
        self._add_token(TokenType.FORMAT_STRING_END, '"')
        self._advance_non_whitespace()  # Skip closing quote

    def _read_format_string_expression(self) -> None:
        start_position = self._position()
        self._add_token(TokenType.FORMAT_STRING_EXPR_START, "{")
        self._advance_non_whitespace()
        while self._peek_char() != "}":
            if self._at_end():
                self._raise_parse_error(
                    "Unterminated format string expression", start_position
                )
            self._read_token()
        self._add_token(TokenType.FORMAT_STRING_EXPR_END, "}")
        self._advance_non_whitespace()

    def _read_format_string_section(self) -> None:
        start_position = self._position()
        string_chars: list[str] = []
        while self._peek_char() not in ("{", '"'):
            if self._at_end() or self._peek_char() == "\n":
                self._raise_parse_error("Unterminated format string", start_position)
            string_chars.append(self._read_format_string_char())
        string_value = "".join(string_chars)
        self._add_token(TokenType.FORMAT_STRING_SECTION, string_value, start_position)

    def _read_format_string_char(self) -> str:
        if self._peek_char() == "\\":
            next_char = self._peek_char(1)
            if next_char == "{":
                self._advance_non_whitespace(2)
                return "{"
            elif next_char == "}":
                self._advance_non_whitespace(2)
                return "}"
            else:
                return self._read_string_literal_char()
        else:
            char = self._peek_char()
            self._advance_non_whitespace()
            return char

    def _read_indexing_expression(self) -> None:
        start_position = self._position()
        self._add_token(TokenType.INDEXING_START, "[")
        self._advance_non_whitespace()
        while self._peek_char() != "]":
            if self._at_end():
                self._raise_parse_error(
                    "Unterminated indexing expression", start_position
                )
            self._read_token()
        self._add_token(TokenType.INDEXING_END, "]")
        self._advance_non_whitespace()

    def _read_function_call_expression(self) -> None:
        start_position = self._position()
        self._add_token(TokenType.FUNCTION_CALL_START, "(")
        self._advance_non_whitespace()
        while self._peek_char() != ")":
            if self._at_end():
                self._raise_parse_error(
                    "Unterminated function call expression", start_position
                )
            self._read_token()
        self._add_token(TokenType.FUNCTION_CALL_END, ")")
        self._advance_non_whitespace()

    def _read_object_expression(self) -> None:
        start_position = self._position()
        self._add_token(TokenType.OBJECT_START, "{")
        self._advance_non_whitespace()
        while self._peek_char() != "}":
            if self._at_end():
                self._raise_parse_error(
                    "Unterminated object expression", start_position
                )
            self._read_token()
        self._add_token(TokenType.OBJECT_END, "}")
        self._advance_non_whitespace()

    def _read_list_expression(self) -> None:
        start_position = self._position()
        self._add_token(TokenType.LIST_START, "[")
        self._advance_non_whitespace()
        while self._peek_char() != "]":
            if self._at_end():
                self._raise_parse_error("Unterminated list expression", start_position)
            self._read_token()
        self._add_token(TokenType.LIST_END, "]")
        self._advance_non_whitespace()

    def _read_parentheses_expression(self) -> None:
        start_position = self._position()
        self._add_token(
            TokenType.PARENTHESES_START,
            "(",
        )
        self._advance_non_whitespace()
        while self._peek_char() != ")":
            if self._at_end():
                self._raise_parse_error(
                    "Unterminated parentheses expression", start_position
                )
            self._read_token()
        self._add_token(TokenType.PARENTHESES_END, ")")
        self._advance_non_whitespace()

    def _read_raw_multiline_string_literal(self) -> None:
        start_position = self._position()
        self._advance_non_whitespace(4)  # Skip opening r"""
        start_index = self._index
        while not (
            self._peek_char() == '"'
            and self._peek_char(1) == '"'
            and self._peek_char(2) == '"'
        ):
            if self._at_end():
                self._raise_parse_error(
                    "Unterminated raw multiline string literal", start_position
                )
            self._advance_non_whitespace()
        string_value = self._contents[start_index : self._index]
        self._advance_non_whitespace(3)  # Skip closing """
        self._add_token(
            TokenType.RAW_MULTILINE_STRING_LITERAL, string_value, start_position
        )

    def _read_raw_string_literal(self) -> None:
        start_position = self._position()
        self._advance_non_whitespace(2)  # Skip opening r"
        start_index = self._index
        while self._peek_char() != '"':
            if self._at_end() or self._peek_char() == "\n":
                self._raise_parse_error(
                    "Unterminated raw string literal", start_position
                )
            self._advance_non_whitespace()
        string_value = self._contents[start_index : self._index]
        self._advance_non_whitespace()  # Skip closing quote
        self._add_token(TokenType.RAW_STRING_LITERAL, string_value, start_position)

    def _read_multiline_string_literal(self) -> None:
        start_position = self._position()
        self._advance_non_whitespace(3)  # Skip opening """
        string_chars: list[str] = []
        while not (
            self._peek_char() == '"'
            and self._peek_char(1) == '"'
            and self._peek_char(2) == '"'
        ):
            if self._at_end():
                self._raise_parse_error(
                    "Unterminated multiline string literal", start_position
                )
            string_chars.append(self._read_string_literal_char())
        string_value = "".join(string_chars)
        self._advance_non_whitespace(3)  # Skip closing """
        self._add_token(
            TokenType.MULTILINE_STRING_LITERAL, string_value, start_position
        )

    def _read_string_literal(self) -> None:
        start_position = self._position()
        self._advance_non_whitespace()  # Skip opening quote
        string_chars: list[str] = []
        while self._peek_char() != '"':
            if self._at_end() or self._peek_char() == "\n":
                self._raise_parse_error("Unterminated string literal", start_position)
            string_chars.append(self._read_string_literal_char())
        string_value = "".join(string_chars)
        self._advance_non_whitespace()  # Skip closing quote
        self._add_token(TokenType.STRING_LITERAL, string_value, start_position)

    def _read_string_literal_char(self) -> str:
        char = self._peek_char()
        if char == "\\":
            next_char = self._peek_char(1)
            if next_char == "n":
                self._advance_non_whitespace(2)
                return "\n"
            elif next_char == "r":
                self._advance_non_whitespace(2)
                return "\r"
            elif next_char == "t":
                self._advance_non_whitespace(2)
                return "\t"
            elif next_char == "\\":
                self._advance_non_whitespace(2)
                return "\\"
            elif next_char == '"':
                self._advance_non_whitespace(2)
                return '"'
            else:
                self._raise_parse_error(f"Invalid escape sequence: '\\{next_char}'")
        else:
            self._advance_non_whitespace()
            return char

    def _read_number(self) -> None:
        start_position = self._position()
        start_index = self._index
        while self._peek_char().isdigit() or self._peek_char() in (
            "e",
            "E",
            "o",
            "O",
            "x",
            "X",
            "b",
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "_",
            "+",
            "-",
            ".",
        ):
            self._advance_non_whitespace()
        number = self._contents[start_index : self._index]
        try:
            int(number)
        except ValueError:
            try:
                int(number, 2)
            except ValueError:
                try:
                    int(number, 8)
                except ValueError:
                    try:
                        int(number, 16)
                    except ValueError:
                        try:
                            float(
                                number,
                            )
                        except ValueError:
                            self._raise_parse_error(
                                f"Invalid number format: '{number}'",
                                start_position,
                            )
                        else:
                            if "e" in number or "E" in number:
                                self._add_token(
                                    TokenType.SCI_FLOAT_LITERAL, number, start_position
                                )
                            else:
                                self._add_token(
                                    TokenType.FLOAT_LITERAL, number, start_position
                                )
                            return
        if "e" in number or "E" in number:
            self._add_token(TokenType.SCI_FLOAT_LITERAL, number, start_position)
        else:
            self._add_token(TokenType.INTEGER_LITERAL, number, start_position)

    _KEYWORDS = {
        "if",
        "then",
        "else",
        "and",
        "or",
        "not",
        "true",
        "false",
        "null",
        "type",
        "typeof",
        "module",
        "proc",
        "let",
        "in",
        "data",
        "case",
        "of",
        "import",
        "as",
        "const",
    }

    def _read_word(self) -> None:
        start_position = self._position()
        start_index = self._index
        while (
            self._peek_char().isalnum()
            or self._peek_char() == "_"
            or self._peek_char() == "'"
        ):
            self._advance_non_whitespace()
        word = self._contents[start_index : self._index]
        if word in self._KEYWORDS:
            self._add_token(TokenType(word), word, start_position)
        else:
            self._add_token(TokenType.SYMBOL, word, start_position)

    def _read_quoted_symbol(self) -> None:
        start_position = self._position()
        self._advance_non_whitespace()  # Skip opening backtick
        start_index = self._index
        while self._peek_char() != "`":
            if self._at_end():
                self._raise_parse_error("Unterminated quoted symbol", start_position)
            self._advance_non_whitespace()
        symbol = self._contents[start_index : self._index]
        self._advance_non_whitespace()  # Skip closing backtick
        self._add_token(TokenType.SYMBOL, symbol, start_position)

    def _read_multiline_comment(self) -> None:
        self._advance_whitespace(2)  # Skip '(*'
        while not self._at_end():
            if self._peek_char() == "(" and self._peek_char(1) == "*":
                self._read_multiline_comment()
            elif self._peek_char() == "*" and self._peek_char(1) == ")":
                self._advance_whitespace(2)  # Skip '*)'
                return
            elif self._peek_char() == "\n":
                self._advance_newline()
            else:
                self._advance_whitespace()
        self._raise_parse_error("Unterminated multiline comment")

    def _read_singleline_comment(self) -> None:
        self._advance_whitespace(2)  # Skip '--'
        while not self._at_end() and self._peek_char() != "\n":
            self._advance_whitespace()

    def _previous_char_was_expression(self) -> bool:
        if (
            self._peek_char(-1).isspace()
            or self._peek_char(-1) == ""
            or not self._tokens
        ):
            return False
        return self._tokens[-1].type in {
            TokenType.TRUE,
            TokenType.FALSE,
            TokenType.NULL,
            TokenType.STRING_LITERAL,
            TokenType.MULTILINE_STRING_LITERAL,
            TokenType.INTEGER_LITERAL,
            TokenType.FLOAT_LITERAL,
            TokenType.SCI_FLOAT_LITERAL,
            TokenType.SYMBOL,
            TokenType.PARENTHESES_END,
            TokenType.FUNCTION_CALL_END,
            TokenType.LIST_END,
            TokenType.INDEXING_END,
            TokenType.OBJECT_END,
        }

    def _peek_char(self, n: int = 0) -> str:
        return (
            self._contents[self._index + n]
            if 0 <= self._index + n < len(self._contents)
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

    def _add_token(
        self, token_type: TokenType, value: str, position: Position | None = None
    ) -> None:
        token = Token(
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
            type=token_type,
            value=value,
        )
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
