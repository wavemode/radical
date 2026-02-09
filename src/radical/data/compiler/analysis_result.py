from dataclasses import dataclass

from radical.data.parser.node import Node
from radical.data.sema.expression import Expression
from radical.data.sema.type import Type
from radical.data.sema.value import Value
from radical.unit.compiler.analysis_scope import AnalysisScope


@dataclass
class AnalysisResult:
    scope: AnalysisScope
    node: Node | None = None
    expr: Expression | None = None
    type: Type | None = None
    value: Value | None = None
    error: str | None = None
