from dataclasses import dataclass

from radical.data.core.data import Data


@dataclass(frozen=True)
class ConstRef(Data):
    moduleId: int
    constId: int
