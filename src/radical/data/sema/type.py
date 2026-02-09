from dataclasses import dataclass
from enum import Enum

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
    kind: "TypeKind"


@dataclass(frozen=True)
class UnionType(Type):
    types: set[Type]


class TypeKind(Data, Enum):
    UNKNOWN = "Unknown"
    INT = "Int"
    FLOAT = "Float"
    STRING = "String"
    BOOL = "Bool"
    NULL = "Null"
    TYPE = "Type"
    UNION = "Union"

    def format(self, indent_level: int = 0) -> str:
        return self.value


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
