from dataclasses import dataclass
from enum import Enum

from radical.data.parser.position import Position


class TokenType(Enum):
    IF = "if"
    THEN = "then"
    ELSE = "else"
    FOR = "for"
    IN = "in"
    AND = "and"
    OR = "or"
    NOT = "not"
    TRUE = "true"
    FALSE = "false"
    NULL = "null"
    TYPE = "type"
    TYPEOF = "typeof"
    FUN = "fun"
    LET = "let"
    TRY = "try"
    CATCH = "catch"
    FINALLY = "finally"
    RAISE = "raise"
    ASSERT = "assert"
    DATA = "data"
    CASE = "case"
    OF = "of"
    IMPORT = "import"
    AS = "as"

    COMMA = ","
    COLON = ":"
    PIPE = "|>"
    ARROW = "->"
    SPREAD = "..."
    ASSIGN = "="
    QUESTION = "?"
    DOT = "."
    EXPONENTIATION = "**"
    MULTIPLY = "*"
    DIVIDE = "/"
    FLOOR_DIVIDE = "//"
    MODULO = "%"
    ADD = "+"
    SUBTRACT = "-"
    EQUAL = "=="
    NOT_EQUAL = "!="
    LESS_THAN = "<"
    LESS_THAN_EQUAL = "<="
    GREATER_THAN = ">"
    GREATER_THAN_EQUAL = ">="

    SYMBOL = "SYMBOL"
    STRING_LITERAL = "STRING_LITERAL"
    RAW_STRING_LITERAL = "RAW_STRING_LITERAL"
    MULTILINE_STRING_LITERAL = "MULTILINE_STRING_LITERAL"
    RAW_MULTILINE_STRING_LITERAL = "RAW_MULTILINE_STRING_LITERAL"
    INTEGER_LITERAL = "INTEGER_LITERAL"
    FLOAT_LITERAL = "FLOAT_LITERAL"
    SCI_FLOAT_LITERAL = "SCI_FLOAT_LITERAL"
    LIST_START = "LIST_START"
    LIST_END = "LIST_END"
    INDEXING_START = "INDEXING_START"
    INDEXING_END = "INDEXING_END"
    MAP_START = "MAP_START"
    MAP_END = "MAP_END"
    PARENTHESES_START = "PARENTHESES_START"
    PARENTHESES_END = "PARENTHESES_END"
    FUNCTION_CALL_START = "FUNCTION_CALL_START"
    FUNCTION_CALL_END = "FUNCTION_CALL_END"

    EOF = "EOF"


@dataclass(frozen=True)
class Token:
    position: Position
    type: TokenType
    value: str

    def __str__(self) -> str:
        return f"Token(type={self.type.name}, value='{self.value}', position=({self.position.line}, {self.position.column}, {self.position.indent_level}))"
