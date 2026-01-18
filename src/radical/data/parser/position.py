from dataclasses import dataclass


@dataclass
class Position:
    line: int
    column: int
    indent_level: int
    seen_non_whitespace: bool
