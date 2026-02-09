from dataclasses import dataclass

from radical.data.core.data import Data


@dataclass(frozen=True)
class Type(Data):
    def unify(self, other: "Type") -> str | None:
        # TODO: subtyping
        if self == other:
            return None
        else:
            return f"Type mismatch: {self} not assignable to value of type {other}"


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
class BooleanType(Type):
    pass


@dataclass(frozen=True)
class NullType(Type):
    pass


@dataclass(frozen=True)
class TypeType(Type):
    pass


@dataclass(frozen=True)
class UnionType(Type):
    types: set[Type]


TypeKinds = (
    UnknownType
    | IntType
    | FloatType
    | StringType
    | BooleanType
    | NullType
    | TypeType
    | UnionType
)
