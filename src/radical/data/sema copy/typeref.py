from dataclasses import dataclass

from radical.data.core.data import Data


@dataclass(frozen=True)
class TypeRef(Data):
    moduleId: int
    typeId: int
