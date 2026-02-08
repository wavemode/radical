from radical.data.parser.node import Node
from radical.data.sema.expression import Expression
from radical.data.sema.symbolref import SymbolRef
from radical.unit.sema.namespace import Namespace
from radical.util.core.unit import Unit


class AnalysisScope(Unit):
    _module_id: int
    _namespace: Namespace
    _parent: "AnalysisScope | None"
    _declarations: list[Node]
    _bindings: dict[SymbolRef, Expression | None]
    _type_bindings: dict[SymbolRef, Expression | None]
    _captures: list[SymbolRef] | None

    def __init__(
        self,
        module_id: int,
        namespace: Namespace,
        parent: "AnalysisScope | None",
        declarations: list[Node],
    ) -> None:
        self._module_id = module_id
        self._namespace = namespace
        self._parent = parent
        self._declarations = declarations
        self._bindings = {}
        self._type_bindings = {}
        self._captures = None

    def module_id(self) -> int:
        return self._module_id
