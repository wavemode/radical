from enum import Enum


class NumberFormat(Enum):
    DECIMAL = "decimal"
    BINARY = "binary"
    OCTAL = "octal"
    HEXADECIMAL = "hexadecimal"
    FLOAT = "float"
    SCI_FLOAT = "sci_float"
    UNKNOWN = "unknown"


def identify_number_literal(number: str) -> NumberFormat:
    if "." in number or "e" in number or "E" in number:
        try:
            float(number)
        except ValueError:
            return NumberFormat.UNKNOWN
        else:
            if "e" in number or "E" in number:
                return NumberFormat.SCI_FLOAT
            else:
                return NumberFormat.FLOAT

    if number.startswith("0b") or number.startswith("0B"):
        try:
            int(number, 2)
        except ValueError:
            return NumberFormat.UNKNOWN
        else:
            return NumberFormat.BINARY

    if number.startswith("0o") or number.startswith("0O"):
        try:
            int(number, 8)
        except ValueError:
            return NumberFormat.UNKNOWN
        else:
            return NumberFormat.OCTAL

    if number.startswith("0x") or number.startswith("0X"):
        try:
            int(number, 16)
        except ValueError:
            return NumberFormat.UNKNOWN
        else:
            return NumberFormat.HEXADECIMAL

    try:
        int(number, 10)
    except ValueError:
        return NumberFormat.UNKNOWN
    else:
        return NumberFormat.DECIMAL
