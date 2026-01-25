from dataclasses import dataclass
from enum import Enum

from radical.data.parser.position import Position
import json


class TokenType(Enum):
    IF = "if"
    THEN = "then"
    ELSE = "else"
    AND = "and"
    OR = "or"
    NOT = "not"
    TRUE = "true"
    FALSE = "false"
    NULL = "null"
    TYPE = "type"
    TYPEOF = "typeof"
    MODULE = "module"
    PROC = "proc"
    LET = "let"
    IN = "in"
    DATA = "data"
    CASE = "case"
    OF = "of"
    IMPORT = "import"
    AS = "as"
    CONST = "const"

    COMMA = ","
    COLON = ":"
    PIPE = "|>"
    VARIANT = "|"
    ARROW = "->"
    ELLIPSIS = "..."
    QUESTION = "?"
    DOT = "."
    EXPONENTIATION = "**"
    MULTIPLY = "*"
    FLOOR_DIVIDE = "//"
    DIVIDE = "/"
    MODULO = "%"
    PLUS = "+"
    MINUS = "-"
    EQUAL = "=="
    NOT_EQUAL = "!="
    LESS_THAN_EQUAL = "<="
    GREATER_THAN_EQUAL = ">="
    LESS_THAN = "<"
    GREATER_THAN = ">"
    ASSIGN = "="
    AT = "@"

    STRING_LITERAL = "STRING_LITERAL"
    RAW_STRING_LITERAL = "RAW_STRING_LITERAL"
    MULTILINE_STRING_LITERAL = "MULTILINE_STRING_LITERAL"
    RAW_MULTILINE_STRING_LITERAL = "RAW_MULTILINE_STRING_LITERAL"

    # in the string f"hello {a + b} world {c + d} !" we have:
    # FORMAT_STRING_START = 'f"'
    # FORMAT_STRING_SECTION = 'hello '
    # FORMAT_STRING_EXPR_START SYMBOL, PLUS, SYMBOL, FORMAT_STRING_EXPR_END
    # FORMAT_STRING_SECTION = ' world '
    # FORMAT_STRING_EXPR_START, SYMBOL, PLUS, SYMBOL, FORMAT_STRING_EXPR_END
    # FORMAT_STRING_SECTION = ' !'
    # FORMAT_STRING_END = '"'
    FORMAT_STRING_START = "FORMAT_STRING_START"
    FORMAT_STRING_SECTION = "FORMAT_STRING_SECTION"
    FORMAT_STRING_EXPR_START = "FORMAT_STRING_EXPR_START"
    FORMAT_STRING_EXPR_END = "FORMAT_STRING_EXPR_END"
    FORMAT_STRING_END = "FORMAT_STRING_END"
    MULTILINE_FORMAT_STRING_START = "MULTILINE_FORMAT_STRING_START"
    MULTILINE_FORMAT_STRING_SECTION = "MULTILINE_FORMAT_STRING_SECTION"
    MULTILINE_FORMAT_STRING_END = "MULTILINE_FORMAT_STRING_END"

    INTEGER_LITERAL = "INTEGER_LITERAL"
    FLOAT_LITERAL = "FLOAT_LITERAL"
    SCI_FLOAT_LITERAL = "SCI_FLOAT_LITERAL"

    SYMBOL = "SYMBOL"

    PARENTHESES_START = "PARENTHESES_START"
    PARENTHESES_END = "PARENTHESES_END"
    FUNCTION_CALL_START = "FUNCTION_CALL_START"
    FUNCTION_CALL_END = "FUNCTION_CALL_END"
    LIST_START = "LIST_START"
    LIST_END = "LIST_END"
    INDEXING_START = "INDEXING_START"
    INDEXING_END = "INDEXING_END"
    OBJECT_START = "OBJECT_START"
    OBJECT_END = "OBJECT_END"

    EOF = "EOF"


@dataclass(frozen=True)
class Token:
    position: Position
    type: TokenType
    value: str

    def __str__(self) -> str:
        return f"Token(type={self.type.name}, value={json.dumps(self.value)}, position=({self.position.line}, {self.position.column}, {self.position.indent_level}))"
