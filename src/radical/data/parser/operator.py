from enum import Enum


class Operator(Enum):
    """
    Grouped by precedence level.

    Exponentiation is the only binary operator which is right-associative.
    """

    AS_TYPE = "::"

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
