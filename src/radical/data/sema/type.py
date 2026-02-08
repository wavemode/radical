from dataclasses import dataclass

from radical.data.data import Data


@dataclass(frozen=True)
class UnknownType(Data):
    pass


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


TypeType = UnknownType | IntType | FloatType | StringType | BoolType | NullType
