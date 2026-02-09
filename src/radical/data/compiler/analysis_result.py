from dataclasses import dataclass

from radical.data.parser.node import Node
from radical.data.sema.expression import Expression
from radical.data.sema.value import Value

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from radical.unit.compiler.analysis_scope import AnalysisScope


@dataclass
class AnalysisResult:
    scope: "AnalysisScope"
    node: Node | None = None
    expr: Expression | None = None
    type: Value | None = None
    value: Value | None = None
    error: str | None = None
