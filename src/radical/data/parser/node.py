from radical.data.data import Data
from radical.data.parser.position import Position


from dataclasses import dataclass


@dataclass(frozen=True)
class Node(Data):
    position: Position

    def __str__(self) -> str:
        return self.format()
