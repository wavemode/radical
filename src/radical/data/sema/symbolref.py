from dataclasses import dataclass

from radical.data.data import Data


@dataclass(frozen=True)
class SymbolRef(Data):
    module_id: int
    symbol_id: int
