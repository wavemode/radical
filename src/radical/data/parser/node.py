from radical.data.data import Data
from radical.data.parser.position import Position


from dataclasses import dataclass


@dataclass(frozen=True)
class Node(Data):
    position: Position

    def __str__(self) -> str:
        return self.format()

    def format_name(self) -> str:
        return (
            self.__class__.__name__[:-4]
            if self.__class__.__name__.endswith("Node")
            else self.__class__.__name__
        )
