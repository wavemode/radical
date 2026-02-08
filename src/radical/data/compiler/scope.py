from dataclasses import dataclass

from radical.data.parser.node import Node
from radical.data.sema.expression import Expression
from radical.data.sema.symbolref import SymbolRef


@dataclass(frozen=True)
class Scope:
    module_id: int
    parent: "Scope | None"
    declarations: list[Node]
    bindings: dict[SymbolRef, Expression | None]
    type_bindings: dict[SymbolRef, Expression | None]
    captures: list[SymbolRef] | None
