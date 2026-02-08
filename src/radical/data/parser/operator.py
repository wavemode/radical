from enum import Enum

from radical.data.core.data import Data


class Operator(Data, Enum):
    """
    Grouped by precedence level.

    Exponentiation is the only binary operator which is right-associative.
    """

    COLON = ":"

    EXPONENTIATION = "**"

    POSITIVE = "+x"
    NEGATIVE = "-x"

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

    NOT = "not"

    AND = "and"

    OR = "or"

    PIPE = "|>"

    def format(self, indent_level: int = 0) -> str:
        return f"'{self.value}'"
