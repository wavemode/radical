from radical.data.compiler.analysis_result import AnalysisResult
from radical.data.interp.builtin_lookup import BuiltinLookup
from radical.data.sema.type import (
    BoolType,
    FloatType,
    IntType,
    NullType,
    RationalType,
    RegexType,
    StringType,
    TypeType,
    UnknownType,
)
from radical.data.sema.value import Value
from radical.unit.compiler.scope import Scope


def setup_builtins(scope: Scope) -> BuiltinLookup:
    unknown_type = UnknownType()
    int_type = IntType()
    float_type = FloatType()
    rational_type = RationalType()
    bool_type = BoolType()
    string_type = StringType()
    null_type = NullType()
    regex_type = RegexType()
    type_type = TypeType()
    for type in (
        unknown_type,
        int_type,
        float_type,
        rational_type,
        bool_type,
        string_type,
        null_type,
        regex_type,
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
        rational_type=rational_type,
        bool_type=bool_type,
        string_type=string_type,
        null_type=null_type,
        regex_type=regex_type,
        type_type=type_type,
    )
