from typing import NoReturn
from radical.data.parser.ast import (
    DefinitionNode,
    ModuleNode,
    MultiLineStringLiteralNode,
    RawMultiLineStringLiteralNode,
    RawStringLiteralNode,
    StringLiteralNode,
    SymbolNode,
    TopLevelDeclarationNode,
    ExpressionNode,
)
from radical.data.parser.errors import ParseError
from radical.unit.parser.char_stream import CharStream
from radical.util.core.unit import Unit


class Parser(Unit):
    _char_stream: CharStream

    def __init__(self, char_stream: CharStream) -> None:
        super().__init__()
        self._char_stream = self.add_child(char_stream)

    def parse_module(self) -> ModuleNode:
        # TODO: support backslash line continuations
        position = self._char_stream.get_position()
        top_level_nodes: list[TopLevelDeclarationNode] = []
        self.skip_whitespace()
        while not self._char_stream.at_end():
            if self.check_empty_statement():
                self.parse_empty_statement()
            elif self.check_definition():
                top_level_nodes.append(self.parse_definition())
            else:
                self._raise_parse_error("Expected a top-level declaration")
            self.skip_non_breaking_whitespace()
            self.parse_statement_separator()
        return ModuleNode(
            top_level_nodes=top_level_nodes,
            position=position,
        )

    def check_empty_statement(self) -> bool:
        return self.check_breaking_whitespace() or self.check_specific_characters(";")

    def parse_empty_statement(self) -> None:
        if self.check_breaking_whitespace():
            self.parse_breaking_whitespace()
        elif self.check_specific_characters(";"):
            self.parse_specific_characters(";")
        else:
            self._raise_parse_error("Expected an empty statement")

    def check_definition(self) -> bool:
        # TODO: support type annotations
        return self.check_symbol()

    def parse_definition(self) -> DefinitionNode:
        # TODO: support type annotations
        position = self._char_stream.get_position()
        name_node = self.parse_symbol()
        self.skip_non_breaking_whitespace()
        self.parse_specific_characters("=")
        self.skip_non_breaking_whitespace()
        value_node = self.parse_value()
        return DefinitionNode(
            name=name_node.name,
            value=value_node,
            position=position,
        )

    def parse_value(self) -> ExpressionNode:
        if self.check_multi_line_string_literal():
            return self.parse_multi_line_string_literal()
        elif self.check_raw_multi_line_string_literal():
            return self.parse_raw_multi_line_string_literal()
        elif self.check_string_literal():
            return self.parse_string_literal()
        elif self.check_raw_string_literal():
            return self.parse_raw_string_literal()
        elif self.check_symbol():
            return self.parse_symbol()
        else:
            self._raise_parse_error("Expected a value")

    def check_reserved_word(self) -> bool:
        # none yet
        return False

    def check_symbol(self) -> bool:
        # TODO: backtick quoted symbols
        char = self._char_stream.peek_char()
        return (not self.check_reserved_word()) and (char.isalpha() or char == "_")

    def parse_symbol(self) -> SymbolNode:
        position = self._char_stream.get_position()
        symbol_chars: list[str] = [self.parse_alphabetic_character()]
        while self.check_word_character():
            symbol_chars.append(self.parse_word_character())
        return SymbolNode(
            name="".join(symbol_chars),
            position=position,
        )

    def check_string_literal(self) -> bool:
        return self._char_stream.peek_char() == '"'

    def parse_string_literal(self) -> StringLiteralNode:
        position = self._char_stream.get_position()
        self.parse_specific_characters('"')
        string_chars: list[str] = []
        while not self.check_specific_characters('"'):
            string_chars.append(self.parse_string_literal_character())
        self.parse_specific_characters('"')
        return StringLiteralNode(
            value="".join(string_chars),
            position=position,
        )

    def check_raw_string_literal(self) -> bool:
        return self._char_stream.peek_chars(2) == 'r"'

    def parse_raw_string_literal(self) -> RawStringLiteralNode:
        position = self._char_stream.get_position()
        self.parse_specific_characters('r"')
        string_chars: list[str] = []
        while not self.check_specific_characters('"'):
            if self.check_breaking_whitespace():
                self._raise_parse_error("Unexpected line break in raw string literal")
            string_chars.append(self._char_stream.read_char())
        self.parse_specific_characters('"')
        return RawStringLiteralNode(
            value="".join(string_chars),
            position=position,
        )

    def check_multi_line_string_literal(self) -> bool:
        return self.check_specific_characters('"""')

    def parse_multi_line_string_literal(self) -> MultiLineStringLiteralNode:
        position = self._char_stream.get_position()
        self.parse_specific_characters('"""')
        string_chars: list[str] = []
        while not self.check_specific_characters('"""'):
            string_chars.append(self.parse_multi_line_string_literal_character())
        self.parse_specific_characters('"""')
        return MultiLineStringLiteralNode(
            value="".join(string_chars),
            position=position,
        )

    def check_raw_multi_line_string_literal(self) -> bool:
        return self.check_specific_characters('r"""')

    def parse_raw_multi_line_string_literal(self) -> RawMultiLineStringLiteralNode:
        position = self._char_stream.get_position()
        self.parse_specific_characters('r"""')
        string_chars: list[str] = []
        while not self.check_specific_characters('"""'):
            string_chars.append(self._char_stream.read_char())
        self.parse_specific_characters('"""')
        return RawMultiLineStringLiteralNode(
            value="".join(string_chars),
            position=position,
        )

    def parse_string_literal_character(self) -> str:
        if self.check_breaking_whitespace():
            self._raise_parse_error("Unexpected line break in string literal")
        char = self._char_stream.read_char()
        if char == '"':
            # The caller of this function should have already checked that the upcoming character
            # is not an ending quote.
            self._raise_parse_error("Unexpected end of string literal")
        if char == "\\":
            return self.parse_escape_sequence()
        return char

    def parse_multi_line_string_literal_character(self) -> str:
        char = self._char_stream.read_char()
        if char == "\\":
            return self.parse_escape_sequence()
        return char

    def parse_escape_sequence(self) -> str:
        # TODO: unicode scalars
        next_char = self._char_stream.read_char()
        if next_char == "n":
            return "\n"
        elif next_char == "r":
            return "\r"
        elif next_char == "t":
            return "\t"
        elif next_char == "\\":
            return "\\"
        elif next_char == '"':
            return '"'
        else:
            self._raise_parse_error(f"Unknown escape sequence '\\{next_char}'")

    def check_alphabetic_character(self) -> bool:
        return self._char_stream.peek_char().isalpha()

    def parse_alphabetic_character(self) -> str:
        char = self._char_stream.read_char()
        if not (char.isalpha()):
            self._raise_parse_error("Expected an alphabetic character")
        return char

    def check_word_character(self) -> bool:
        char = self._char_stream.peek_char()
        return char.isalnum() or char == "_"

    def parse_word_character(self) -> str:
        char = self._char_stream.read_char()
        if not (char.isalnum() or char == "_"):
            self._raise_parse_error("Expected a word character")
        return char

    def skip_whitespace(self) -> None:
        while (
            not self._char_stream.at_end() and self._char_stream.peek_char().isspace()
        ):
            self._char_stream.read_char()

    def skip_non_breaking_whitespace(self) -> None:
        while not self._char_stream.at_end() and self._char_stream.peek_char() in (
            " ",
            "\t",
        ):
            self._char_stream.read_char()

    def parse_statement_separator(self) -> None:
        if self.check_breaking_whitespace():
            self.parse_breaking_whitespace()
        elif self.check_specific_characters(";"):
            self.parse_specific_characters(";")
        else:
            self._raise_parse_error(
                "Expected a statement separator (newline or semicolon)"
            )

    def check_breaking_whitespace(self) -> bool:
        return self._char_stream.peek_char() in ("\n", "\r")

    def parse_breaking_whitespace(self) -> str:
        char = self._char_stream.read_char()
        if char == "\n":
            return "\n"
        elif char == "\r":
            if self.check_specific_characters("\n"):
                self._char_stream.read_char()
                char += "\n"
            return char
        else:
            self._raise_parse_error("Expected a line break")

    def check_specific_characters(self, expected_chars: str) -> bool:
        position = self._char_stream.get_position()
        index = 0
        matching = True
        while index < len(expected_chars):
            expected_char = expected_chars[index]
            if self._char_stream.at_end():
                matching = False
                break
            if self._char_stream.read_char() != expected_char:
                matching = False
                break
            index += 1
        self._char_stream.reset_position(position)
        return matching

    def parse_specific_characters(self, expected_chars: str) -> str:
        chars = self._char_stream.read_chars(len(expected_chars))
        if chars != expected_chars:
            self._raise_parse_error(f"Unexpected characters: {chars}")
        return chars

    def _raise_parse_error(self, message: str) -> NoReturn:
        raise ParseError(
            message,
            position=self._char_stream.get_position(),
        )
