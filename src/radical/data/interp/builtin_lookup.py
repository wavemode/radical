from dataclasses import dataclass

from radical.data.sema.type import (
    BoolType,
    FloatType,
    IntType,
    NullType,
    RationalType,
    StringType,
    TypeType,
    UnknownType,
    RegexType,
)


@dataclass(frozen=True)
class BuiltinLookup:
    unknown_type: UnknownType
    int_type: IntType
    float_type: FloatType
    rational_type: RationalType
    bool_type: BoolType
    string_type: StringType
    null_type: NullType
    regex_type: RegexType
    type_type: TypeType
