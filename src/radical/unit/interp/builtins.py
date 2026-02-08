from radical.data.interp.builtin_lookup import BuiltinLookup
from radical.data.sema.type import (
    BoolType,
    FloatType,
    IntType,
    NullType,
    StringType,
    TypeType,
    UnknownType,
)
from radical.data.sema.typeref import TypeRef
from radical.unit.interp.namespace import Namespace


def _add_builtin_type(
    namespace: Namespace, module_id: int, type_name: str, type: TypeType
) -> TypeRef:
    type_ref = namespace.intern_type(module_id, type)
    symbol_id = namespace.intern_symbol(module_id, type_name)
    namespace.bind_type(symbol_id, type_ref)
    return type_ref


def setup_builtins(namespace: Namespace) -> BuiltinLookup:
    module_id = namespace.add_or_get_module("Core.Builtin")

    unknown_type = _add_builtin_type(namespace, module_id, "Unknown", UnknownType())
    int_type = _add_builtin_type(namespace, module_id, "Int", IntType())
    float_type = _add_builtin_type(namespace, module_id, "Float", FloatType())
    bool_type = _add_builtin_type(namespace, module_id, "Bool", BoolType())
    string_type = _add_builtin_type(namespace, module_id, "String", StringType())
    null_type = _add_builtin_type(namespace, module_id, "Null", NullType())

    namespace.mark_module_analyzed(module_id)

    return BuiltinLookup(
        unknown_type=unknown_type,
        int_type=int_type,
        float_type=float_type,
        bool_type=bool_type,
        string_type=string_type,
        null_type=null_type,
    )
