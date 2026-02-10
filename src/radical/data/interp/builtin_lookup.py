from dataclasses import dataclass

from radical.data.sema.type import (
    BooleanType,
    FloatType,
    IntType,
    NullType,
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
    bool_type: BooleanType
    string_type: StringType
    null_type: NullType
    regex_type: RegexType
    type_type: TypeType
