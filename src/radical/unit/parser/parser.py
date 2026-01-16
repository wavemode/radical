from typing import NoReturn
from radical.data.parser.ast import (
    VariableBindingStatementNode,
    ModuleNode,
    MultiLineStringLiteralNode,
    RawMultiLineStringLiteralNode,
    RawStringLiteralNode,
    StringLiteralNode,
    SymbolNode,
    TopLevelDeclarationNode,
    ValueExpressionNode,
    IntegerLiteralNode,
    FloatLiteralNode,
    SciFloatLiteralNode,
    UnaryOperator,
    BinaryOperator,
    precedence_of_binary_op,
    precendence_of_unary_op,
    associativity_of_binary_op,
    associativity_of_unary_op,
    OperatorAssociativity,
    UnaryOperationNode,
    BinaryOperationNode,
)
from radical.data.parser.errors import ParseError
from radical.data.parser.position import Position
from radical.unit.parser.char_stream import CharStream
from radical.util.core.unit import Unit


class Parser(Unit):
    _char_stream: CharStream

    def __init__(self, char_stream: CharStream) -> None:
        super().__init__()
        self._char_stream = self.add_child(char_stream)
        self._seen_non_whitespace = False
        self._indent_level = 0

    def parse_module(self) -> ModuleNode:
        position = self._position()
        top_level_nodes: list[TopLevelDeclarationNode] = []
        self.skip_whitespace()
        while not self.at_end():
            if not self._indent_level == 0:
                self._raise_parse_error("Unexpected indentation at top-level")
            top_level_nodes.append(self.parse_top_level_declaration())
            self.skip_whitespace()
        return ModuleNode(
            position=position,
            top_level_nodes=top_level_nodes,
        )

    def parse_top_level_declaration(self) -> TopLevelDeclarationNode:
        if self.check_symbol():
            return self.parse_variable_binding()
        else:
            self._raise_parse_error("Expected a top-level declaration")

    def parse_variable_binding(self) -> VariableBindingStatementNode:
        # TODO: support type annotation
        start_position = self._position()
        name_node = self.parse_symbol()
        self.skip_non_breaking_whitespace()
        self.parse_specific_charachters("=")
        self.skip_whitespace()
        value_node = self.parse_value()
        return VariableBindingStatementNode(
            position=start_position,
            name=name_node,
            value=value_node,
            type=None,
        )

    def parse_value(self, min_precedence: int = 0) -> ValueExpressionNode:
        position_before_lhs = self._position()
        lhs: ValueExpressionNode | None = None
        if not self.check_unary_operator():
            lhs = self.parse_single_value_expression()
            self.skip_non_breaking_whitespace()

        while not self.at_end():
            position_before_op = self._position()
            op: BinaryOperator | UnaryOperator | None = None
            if lhs is None:
                op = self.parse_unary_operator()
            elif self.check_binary_operator():
                op = self.parse_binary_operator()

            if op is None:
                break

            precedence: int
            associativity: OperatorAssociativity

            if isinstance(op, BinaryOperator):
                precedence = precedence_of_binary_op(op)
                associativity = associativity_of_binary_op(op)
                if precedence < min_precedence:
                    self._reset_position(position_before_op)
                    break
            else:
                precedence = precendence_of_unary_op(op)
                associativity = associativity_of_unary_op(op)

            self.skip_whitespace()
            rhs = self.parse_value(
                min_precedence=(
                    # Adding 1 makes it so that another operation to the right with the same precedence
                    # level as the current operator will not be included in the rhs expression (due to
                    # the min_precedence now being 1 higher than the current operator's precedence).
                    # Thus causing left associativity (e.g. a - b - c  parsed as (a - b) - c).
                    precedence + 1
                    if associativity == OperatorAssociativity.LEFT
                    else precedence
                )
            )
            if isinstance(op, UnaryOperator):
                lhs = UnaryOperationNode(
                    operator=op, operand=rhs, position=position_before_op
                )
            else:
                assert lhs is not None
                lhs = BinaryOperationNode(
                    left=lhs,
                    operator=op,
                    right=rhs,
                    position=position_before_lhs,
                )
            self.skip_non_breaking_whitespace()

        assert lhs is not None
        return lhs

    def parse_single_value_expression(self) -> ValueExpressionNode:
        if self.check_raw_multi_line_string_literal():
            return self.parse_raw_multi_line_string_literal()
        elif self.check_raw_string_literal():
            return self.parse_raw_string_literal()
        elif self.check_multi_line_string_literal():
            return self.parse_multi_line_string_literal()
        elif self.check_string_literal():
            return self.parse_string_literal()
        elif self.check_number_literal():
            return self.parse_number_literal()
        elif self.check_symbol():
            return self.parse_symbol()
        else:
            self._raise_parse_error("Expected a value")

    def check_binary_operator(self) -> bool:
        return self.check_any_sequence(
            [
                op.value
                for op in BinaryOperator
                if op not in (BinaryOperator.AND, BinaryOperator.OR)
            ]
        ) or self.check_any_word(["and", "or"])

    def parse_binary_operator(self) -> BinaryOperator:
        if self.check_word("and"):
            self._read(3)
            return BinaryOperator.AND
        elif self.check_word("or"):
            self._read(2)
            return BinaryOperator.OR
        else:
            operator_str = self.parse_any_sequence(
                [
                    op.value
                    for op in BinaryOperator
                    if op not in (BinaryOperator.AND, BinaryOperator.OR)
                ]
            )
            return BinaryOperator(operator_str)

    def check_unary_operator(self) -> bool:
        return self._peek() in ("+", "-") or self.check_word("not")

    def parse_unary_operator(self) -> UnaryOperator:
        if self.check_word("not"):
            self._read(3)
            return UnaryOperator.NOT
        else:
            return UnaryOperator(self._read())

    def check_number_literal(self) -> bool:
        return self._peek().isdigit()

    def parse_number_literal(
        self,
    ) -> SciFloatLiteralNode | FloatLiteralNode | IntegerLiteralNode:
        position = self._position()

        integer_chars = self.parse_numeral_sequence()
        fractional_chars: list[str] | None = None
        e: str | None = None
        exponent_chars: list[str] | None = None
        exponent_sign: str | None = None

        if not self.at_end() and self._peek() == ".":
            self._read()
            fractional_chars = self.parse_numeral_sequence()

        if not self.at_end() and self._peek().lower() == "e":
            e = self._read()
            if self._peek() in ("+", "-"):
                exponent_sign = self._read()
            exponent_chars = self.parse_numeral_sequence()

        if exponent_chars is not None:
            parts: list[str] = [*integer_chars]
            if fractional_chars is not None:
                parts.append(".")
                parts.extend(fractional_chars)
            assert e is not None
            parts.append(e)
            parts.append(exponent_sign or "")
            parts.extend(exponent_chars)

            return SciFloatLiteralNode(
                position=position,
                value="".join(parts),
            )

        if fractional_chars is not None:
            value_parts: list[str] = [
                *integer_chars,
                ".",
                *fractional_chars,
            ]
            return FloatLiteralNode(
                position=position,
                value="".join(value_parts),
            )

        value = "".join(integer_chars)
        return IntegerLiteralNode(
            position=self._position(),
            value=value,
        )

    def parse_numeral_sequence(self) -> list[str]:
        numeral_chars: list[str] = []
        while not self.at_end():
            char = self._peek()
            if char.isdigit():
                numeral_chars.append(self._read())
            else:
                break
        if not numeral_chars:
            self._raise_parse_error("Expected numeral sequence")
        return numeral_chars

    def check_symbol(self) -> bool:
        # TODO: support backtick-quoted symbols
        char = self._peek()
        return char.isalpha() or char == "_"

    def parse_symbol(self) -> SymbolNode:
        start_position = self._position()
        name_chars: list[str] = []
        char = self._peek()
        if char.isalpha() or char == "_":
            name_chars.append(self._read())
        else:
            self._raise_parse_error("Expected symbol", position=start_position)
        while not self.at_end():
            if self._peek().isalnum() or self._peek() == "_":
                name_chars.append(self._read())
            else:
                break
        return SymbolNode(
            position=start_position,
            name="".join(name_chars),
        )

    def check_string_literal(self) -> bool:
        return self._peek() == '"'

    def parse_string_literal(self) -> StringLiteralNode:
        start_position = self._position()
        self.parse_specific_charachters('"')
        value_chars: list[str] = []
        while not self.at_end() and not self._peek() == "\n":
            if self.check_specific_charachters('"'):
                self._read()
                return StringLiteralNode(
                    position=start_position,
                    value="".join(value_chars),
                )
            elif self._peek() == "\\":
                value_chars.append(self.parse_string_literal_escape_sequence())
            else:
                value_chars.append(self._read())
        self._raise_parse_error("Unterminated string literal", position=start_position)

    def check_multi_line_string_literal(self) -> bool:
        return self.check_specific_charachters('"""')

    def parse_multi_line_string_literal(self) -> MultiLineStringLiteralNode:
        start_position = self._position()
        self.parse_specific_charachters('"""')
        value_chars: list[str] = []
        while not self.at_end():
            if self.check_specific_charachters('"""'):
                self._read(3)
                return MultiLineStringLiteralNode(
                    position=start_position,
                    value="".join(value_chars),
                )
            elif self._peek() == "\\":
                value_chars.append(self.parse_string_literal_escape_sequence())
            else:
                value_chars.append(self._read())
        self._raise_parse_error(
            "Unterminated multi-line string literal", position=start_position
        )

    def check_raw_string_literal(self) -> bool:
        return self.check_specific_charachters('r"')

    def parse_raw_string_literal(self) -> RawStringLiteralNode:
        start_position = self._position()
        self.parse_specific_charachters('r"')
        value_chars: list[str] = []
        while not self.at_end() and not self._peek() == "\n":
            if self.check_specific_charachters('"'):
                self._read()
                return RawStringLiteralNode(
                    position=start_position,
                    value="".join(value_chars),
                )
            elif self.check_specific_charachters('""'):
                self._read(2)
                value_chars.append('"')
            else:
                value_chars.append(self._read())
        self._raise_parse_error(
            "Unterminated raw string literal", position=start_position
        )

    def check_raw_multi_line_string_literal(self) -> bool:
        return self.check_specific_charachters('r"""')

    def parse_raw_multi_line_string_literal(self) -> RawMultiLineStringLiteralNode:
        start_position = self._position()
        self.parse_specific_charachters('r"""')
        value_chars: list[str] = []
        while not self.at_end():
            if self.check_specific_charachters('"""'):
                self._read(3)
                return RawMultiLineStringLiteralNode(
                    position=start_position,
                    value="".join(value_chars),
                )
            elif self.check_specific_charachters('""'):
                self._read(2)
                value_chars.append('"')
            else:
                value_chars.append(self._read())
        self._raise_parse_error(
            "Unterminated raw multi-line string literal", position=start_position
        )

    STRING_LITERAL_ESCAPE_SEQUENCES = {
        "n": "\n",
        "r": "\r",
        "t": "\t",
        "\\": "\\",
        '"': '"',
    }

    def parse_string_literal_escape_sequence(self) -> str:
        self.parse_specific_charachters("\\")
        escape_char = self._read()
        if escape_char in self.STRING_LITERAL_ESCAPE_SEQUENCES:
            return self.STRING_LITERAL_ESCAPE_SEQUENCES[escape_char]
        else:
            self._raise_parse_error(
                f"Unknown escape sequence '\\{escape_char}' in string literal"
            )

    def check_single_line_comment(self) -> bool:
        return self.check_specific_charachters("--")

    def skip_single_line_comment(self) -> None:
        self.parse_specific_charachters("--")
        while not self.at_end() and not self._peek() == "\n":
            self._read()

    def check_multi_line_comment(self) -> bool:
        return self.check_specific_charachters("(*")

    def skip_multi_line_comment(self) -> None:
        self.parse_specific_charachters("(*")
        level = 1
        while not self.at_end():
            if self.check_specific_charachters("(*"):
                level += 1
                self._read(2)
            elif self.check_specific_charachters("*)"):
                level -= 1
                self._read(2)
                if level == 0:
                    return
            else:
                self._read()
        self._raise_parse_error("Unterminated multi-line comment")

    def skip_non_breaking_whitespace(self) -> None:
        self.skip_chars({" ", "\t", "\r"})

    def skip_whitespace(self) -> None:
        self.skip_chars({" ", "\t", "\r", "\n"})

    def skip_chars(self, chars: set[str]) -> None:
        while not self.at_end():
            if self.check_single_line_comment():
                self.skip_single_line_comment()
            elif self.check_multi_line_comment():
                self.skip_multi_line_comment()
            else:
                char = self._peek()
                if char in chars:
                    self._read()
                else:
                    break

    def check_any_sequence(self, expected: list[str]) -> bool:
        position = self._position()
        longest = max(len(seq) for seq in expected)
        chars: list[str] = []
        index = 0
        while not self.at_end() and index < longest:
            chars.append(self._read())
            index += 1
        word = "".join(chars)
        self._reset_position(position)
        return any(word.startswith(seq) for seq in expected)

    def parse_any_sequence(self, expected: list[str]) -> str:
        position = self._position()
        longest = max(len(seq) for seq in expected)
        chars: list[str] = []
        index = 0
        while not self.at_end() and index < longest:
            chars.append(self._read())
            index += 1
        word = "".join(chars)
        self._reset_position(position)
        result = max(
            (seq for seq in expected if word.startswith(seq)),
            key=lambda s: len(s),
        )
        self._read(len(result))
        return result

    def check_any_word(self, expected: list[str]) -> bool:
        for word in expected:
            if self.check_word(word):
                return True
        return False

    def parse_any_word(self, expected: list[str]) -> str:
        for word in expected:
            if self.check_word(word):
                self._read(len(word))
                return word
        self._raise_parse_error(f"Expected one of: {', '.join(expected)}")

    def check_word(self, expected: str) -> bool:
        position = self._position()
        matching = True
        index = 0
        while not self.at_end():
            if index == len(expected):
                break
            if self._read() != expected[index]:
                matching = False
                break
            index += 1
        at_end = self.at_end()
        if at_end:
            next_char = ""
        else:
            next_char = self._peek()
        self._reset_position(position)
        return matching and (at_end or not (next_char.isalnum() or next_char == "_"))

    def check_specific_charachters(self, expected: str) -> bool:
        position = self._position()
        matching = True
        index = 0
        while index < len(expected):
            if self.at_end() or self._read() != expected[index]:
                matching = False
                break
            index += 1
        self._reset_position(position)
        return matching

    def parse_specific_charachters(self, expected: str) -> None:
        actual = self._read(len(expected))
        if actual != expected:
            self._raise_parse_error(f"Expected '{expected}', got '{actual}'")

    def at_end(self) -> bool:
        return self._char_stream.at_end()

    def _peek(self, n: int = 1) -> str:
        if n == 1:
            return self._char_stream.peek_char()
        return self._char_stream.peek_chars(n)

    def _read(self, n: int = 1) -> str:
        result = self._peek(n)
        for _ in range(n):
            char = self._char_stream.read_char()
            if char == "\n":
                self._seen_non_whitespace = False
                self._indent_level = 0
            elif char in (" ", "\t"):
                if not self._seen_non_whitespace:
                    self._indent_level += 1
            else:
                self._seen_non_whitespace = True
        return result

    def _position(self) -> Position:
        return self._char_stream.get_position()

    def _reset_position(self, position: Position) -> None:
        self._char_stream.reset_position(position)

    def _raise_parse_error(
        self, message: str, position: Position | None = None
    ) -> NoReturn:
        raise ParseError(message, position=position or self._position())
