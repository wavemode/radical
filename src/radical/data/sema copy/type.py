from dataclasses import dataclass

from radical.data.core.data import Data


@dataclass(frozen=True)
class IntType(Data):
    pass


@dataclass(frozen=True)
class FloatType(Data):
    pass


@dataclass(frozen=True)
class StringType(Data):
    pass


@dataclass(frozen=True)
class BoolType(Data):
    pass


@dataclass(frozen=True)
class NullType(Data):
    pass


TypeType = IntType | FloatType | StringType | BoolType | NullType
