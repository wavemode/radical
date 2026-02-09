from radical.data.compiler.analysis_result import AnalysisResult
from radical.data.interp.builtin_lookup import BuiltinLookup
from radical.data.sema.type import (
    BooleanType,
    FloatType,
    IntType,
    NullType,
    StringType,
    TypeKinds,
    TypeType,
    UnknownType,
)
from radical.data.sema.value import Value
from radical.unit.compiler.analysis_scope import AnalysisScope

from typing import TypeVar

T = TypeVar("T", bound=TypeKinds)


def setup_builtins(scope: AnalysisScope) -> BuiltinLookup:
    unknown_type = UnknownType()
    int_type = IntType()
    float_type = FloatType()
    bool_type = BooleanType()
    string_type = StringType()
    null_type = NullType()
    type_type = TypeType()
    for type in (
        unknown_type,
        int_type,
        float_type,
        bool_type,
        string_type,
        null_type,
        type_type,
    ):
        type_name = type.__class__.__name__.removesuffix("Type")
        scope.add_type_binding(
            type_name,
            AnalysisResult(
                name=type_name,
                scope=scope,
                type_annotation=Value(type_type),
                value=Value(type),
            ),
            local=True,
        )

    return BuiltinLookup(
        unknown_type=unknown_type,
        int_type=int_type,
        float_type=float_type,
        bool_type=bool_type,
        string_type=string_type,
        null_type=null_type,
        type_type=type_type,
    )
