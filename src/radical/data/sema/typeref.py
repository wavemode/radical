from dataclasses import dataclass

from radical.data.data import Data


@dataclass(frozen=True)
class TypeRef(Data):
    module_id: int
    type_id: int
