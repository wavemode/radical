from dataclasses import dataclass

from radical.data.sema.typeref import TypeRef


@dataclass(frozen=True)
class BuiltinLookup:
    unknown_type: TypeRef
    int_type: TypeRef
    float_type: TypeRef
    bool_type: TypeRef
    string_type: TypeRef
    null_type: TypeRef
