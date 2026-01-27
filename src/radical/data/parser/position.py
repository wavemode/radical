from dataclasses import dataclass


@dataclass
class Position:
    line: int
    column: int
    indent_level: int
