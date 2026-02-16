from dataclasses import dataclass

from radical.data.core.data import Data


@dataclass
class Position(Data):
    filename: str
    line: int
    column: int
    indent_level: int

    def format(self, indent_level: int = 0) -> str:
        return f"({self.line}, {self.column}, {self.indent_level})"
