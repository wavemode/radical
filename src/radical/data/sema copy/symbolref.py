from dataclasses import dataclass

from radical.data.core.data import Data


@dataclass(frozen=True)
class SymbolRef(Data):
    moduleId: int
    symbolId: int
