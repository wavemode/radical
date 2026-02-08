from dataclasses import dataclass


@dataclass(frozen=True)
class IntValue:
    value: int


ValueType = IntValue
