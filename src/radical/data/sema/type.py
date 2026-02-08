from dataclasses import dataclass

from radical.data.core.data import Data


@dataclass(frozen=True)
class Type(Data):
    pass


@dataclass(frozen=True)
class UnknownType(Type):
    pass


@dataclass(frozen=True)
class IntType(Type):
    pass


@dataclass(frozen=True)
class FloatType(Type):
    pass


@dataclass(frozen=True)
class StringType(Type):
    pass


@dataclass(frozen=True)
class BoolType(Type):
    pass


@dataclass(frozen=True)
class NullType(Type):
    pass


TypeType = UnknownType | IntType | FloatType | StringType | BoolType | NullType
