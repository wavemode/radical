from typing import Iterable
from radical.data.compiler.analysis_result import AnalysisResult
from radical.unit.sema.namespace import Namespace
from radical.util.core.unit import Unit


class AnalysisScope(Unit):
    _module_id: int
    _namespace: Namespace
    _parent: "AnalysisScope | None"
    _bindings: dict[int, AnalysisResult]
    _type_bindings: dict[int, AnalysisResult]
    _captures: list[int] | None

    def __init__(
        self,
        module_id: int,
        namespace: Namespace,
        parent: "AnalysisScope | None",
    ) -> None:
        self._module_id = module_id
        self._namespace = namespace
        self._parent = parent
        self._bindings = {}
        self._type_bindings = {}
        self._value_decls = {}
        self._type_decls = {}
        self._captures = None

    def module_id(self) -> int:
        return self._module_id

    def intern_symbol(self, name: str) -> int:
        return self._namespace.intern_symbol(self._module_id, name)

    def add_binding(
        self, symbol_ref: int, value: AnalysisResult | None = None
    ) -> AnalysisResult:
        result = value or AnalysisResult(scope=self)
        self._bindings[symbol_ref] = result
        return result

    def lookup_binding(self, symbol_ref: int) -> AnalysisResult | None:
        if symbol_ref in self._bindings:
            return self._bindings[symbol_ref]
        elif self._parent is not None:
            return self._parent.lookup_binding(symbol_ref)

    def bindings(self) -> Iterable[AnalysisResult]:
        return self._bindings.values()

    def add_type_binding(
        self, symbol_ref: int, value: AnalysisResult | None = None
    ) -> AnalysisResult:
        result = value or AnalysisResult(scope=self)
        self._type_bindings[symbol_ref] = result
        return result

    def lookup_type_binding(self, symbol_ref: int) -> AnalysisResult | None:
        if symbol_ref in self._type_bindings:
            return self._type_bindings[symbol_ref]
        elif self._parent is not None:
            return self._parent.lookup_type_binding(symbol_ref)

    def type_bindings(self) -> Iterable[AnalysisResult]:
        return self._type_bindings.values()
