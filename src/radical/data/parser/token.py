from dataclasses import dataclass
from enum import Enum

from radical.data.core.data import Data
from radical.data.parser.position import Position
import json


class TokenType(Data, Enum):
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
    FUN = "fun"
    PROC = "proc"
    LET = "let"
    IN = "in"
    DATA = "data"
    CASE = "case"
    OF = "of"
    IMPORT = "import"
    AS = "as"
    CONST = "const"
    LOCAL = "local"

    TILDE = "~"
    COMMA = ","
    COLON = ":"
    PIPE = "|>"
    VARIANT = "|"
    RIGHT_ARROW = "->"
    LEFT_ARROW = "<-"
    MAPPING = "=>"
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
    SEMICOLON = ";"

    STRING_CONTENTS = "STRING_CONTENTS"

    STRING_LITERAL_START = "STRING_LITERAL_START"
    STRING_LITERAL_END = "STRING_LITERAL_END"

    REGEX_LITERAL_START = "REGEX_LITERAL_START"
    REGEX_LITERAL_END = "REGEX_LITERAL_END"

    RAW_STRING_LITERAL_START = "RAW_STRING_LITERAL_START"
    RAW_STRING_LITERAL_END = "RAW_STRING_LITERAL_END"

    MULTILINE_STRING_LITERAL_START = "MULTILINE_STRING_LITERAL_START"
    MULTILINE_STRING_LITERAL_END = "MULTILINE_STRING_LITERAL_END"

    RAW_MULTILINE_STRING_LITERAL_START = "RAW_MULTILINE_STRING_LITERAL_START"
    RAW_MULTILINE_STRING_LITERAL_END = "RAW_MULTILINE_STRING_LITERAL_END"

    # in the string f"hello {a + b} world {c + d} !" we have:
    # FORMAT_STRING_START = 'f"'
    # STRING_CONTENTS = 'hello '
    # FORMAT_STRING_EXPR_START SYMBOL, PLUS, SYMBOL, FORMAT_STRING_EXPR_END
    # STRING_CONTENTS = ' world '
    # FORMAT_STRING_EXPR_START, SYMBOL, PLUS, SYMBOL, FORMAT_STRING_EXPR_END
    # STRING_CONTENTS = ' !'
    # FORMAT_STRING_END = '"'
    FORMAT_STRING_START = "FORMAT_STRING_START"
    FORMAT_STRING_EXPR_START = "FORMAT_STRING_EXPR_START"
    FORMAT_STRING_EXPR_END = "FORMAT_STRING_EXPR_END"
    FORMAT_STRING_END = "FORMAT_STRING_END"
    MULTILINE_FORMAT_STRING_START = "MULTILINE_FORMAT_STRING_START"
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
    TYPE_APPLICATION_START = "TYPE_APPLICATION_START"
    TYPE_APPLICATION_END = "TYPE_APPLICATION_END"

    EOF = "EOF"

    def format(self, indent_level: int = 0) -> str:
        return f"'{self.value}'"


EXPR_START_TOKENS = {
    TokenType.IF,
    TokenType.NOT,
    TokenType.TRUE,
    TokenType.FALSE,
    TokenType.NULL,
    TokenType.TILDE,
    TokenType.MODULE,
    TokenType.FUN,
    TokenType.PROC,
    TokenType.LET,
    TokenType.CASE,
    TokenType.PLUS,
    TokenType.MINUS,
    TokenType.STRING_LITERAL_START,
    TokenType.RAW_STRING_LITERAL_START,
    TokenType.MULTILINE_STRING_LITERAL_START,
    TokenType.RAW_MULTILINE_STRING_LITERAL_START,
    TokenType.FORMAT_STRING_START,
    TokenType.MULTILINE_FORMAT_STRING_START,
    TokenType.INTEGER_LITERAL,
    TokenType.FLOAT_LITERAL,
    TokenType.SCI_FLOAT_LITERAL,
    TokenType.SYMBOL,
    TokenType.PARENTHESES_START,
    TokenType.LIST_START,
    TokenType.OBJECT_START,
}

EXPR_END_TOKENS = {
    TokenType.TRUE,
    TokenType.FALSE,
    TokenType.NULL,
    TokenType.TILDE,
    TokenType.STRING_LITERAL_END,
    TokenType.RAW_STRING_LITERAL_END,
    TokenType.MULTILINE_STRING_LITERAL_END,
    TokenType.RAW_MULTILINE_STRING_LITERAL_END,
    TokenType.FORMAT_STRING_END,
    TokenType.MULTILINE_FORMAT_STRING_END,
    TokenType.INTEGER_LITERAL,
    TokenType.FLOAT_LITERAL,
    TokenType.SCI_FLOAT_LITERAL,
    TokenType.SYMBOL,
    TokenType.PARENTHESES_END,
    TokenType.FUNCTION_CALL_END,
    TokenType.LIST_END,
    TokenType.INDEXING_END,
    TokenType.OBJECT_END,
    TokenType.TYPE_APPLICATION_END,
}


@dataclass(frozen=True)
class Token(Data):
    position: Position
    type: TokenType
    value: str

    def __str__(self) -> str:
        return self.pretty()

    def format(self, indent_level: int = 0) -> str:
        return f"{self.type.name}('{self.value}')"

    def pretty(self) -> str:
        return f"Token(type={self.type.name}, value={json.dumps(self.value)}, position={self.position})"
