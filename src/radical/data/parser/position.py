from dataclasses import dataclass

from radical.data.data import Data


@dataclass
class Position(Data):
    line: int
    column: int
    indent_level: int

    def format(self, indent_level: int = 0) -> str:
        return f"({self.line}, {self.column}, {self.indent_level})"
