from dataclasses import dataclass

from radical.data.core.data import Data


@dataclass(frozen=True)
class Type(Data):
    def name(self) -> str:
        return self.__class__.__name__.removesuffix("Type")

    def unify(self, other: "Type") -> bool:
        # TODO: subtyping
        return self == other


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
class RegexType(Type):
    pass


@dataclass(frozen=True)
class BooleanType(Type):
    pass


@dataclass(frozen=True)
class NullType(Type):
    pass


@dataclass(frozen=True)
class TypeType(Type):
    def name(self) -> str:
        return "Type"


@dataclass(frozen=True)
class UnionType(Type):
    types: set[Type]

    def name(self) -> str:
        return " | ".join(sorted(t.name() for t in self.types))


TypeKinds = (
    UnknownType
    | IntType
    | FloatType
    | StringType
    | BooleanType
    | NullType
    | TypeType
    | RegexType
    | UnionType
)
