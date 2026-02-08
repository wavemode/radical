from dataclasses import dataclass

from radical.data.core.data import Data


@dataclass(frozen=True)
class ConstRef(Data):
    module_id: int
    const_id: int
