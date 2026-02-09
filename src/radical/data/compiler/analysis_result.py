from dataclasses import dataclass

from radical.data.core.data import Data
from radical.data.parser.node import Node
from radical.data.sema.expression import Expression
from radical.data.sema.value import Value

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from radical.unit.compiler.analysis_scope import AnalysisScope


@dataclass
class AnalysisResult(Data):
    name: str
    scope: "AnalysisScope"
    value_node: Node | None = None
    value_expr: Expression | None = None
    value: Value | None = None
    type_annotation_node: Node | None = None
    type_annotation_expr: Expression | None = None
    type_annotation: Value | None = None

    def format_field(self, name: str, indent_level: int = 0) -> str | None:
        if name != "scope":
            return super().format_field(name, indent_level=indent_level)
