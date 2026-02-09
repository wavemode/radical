from dataclasses import dataclass
from typing import Any

from radical.data.core.data import Data


@dataclass(frozen=True)
class Value(Data):
    value: Any
