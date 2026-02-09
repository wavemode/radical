from pathlib import Path
from radical.data.compiler.analysis_result import AnalysisResult
from radical.data.interp.builtin_lookup import BuiltinLookup
from radical.data.parser.ast import ModuleNode
from radical.data.sema.expression import ExpressionType
from radical.data.sema.type import Type
from radical.unit.compiler.loader import Loader
from radical.unit.compiler.scope_tools import populate_decls
from radical.unit.compiler.analysis_scope import AnalysisScope
from radical.unit.interp.builtins import setup_builtins
from radical.unit.parser.lexer import Lexer
from radical.unit.parser.parser import Parser
from radical.unit.sema.namespace import Namespace
from radical.util.core.unit import Unit


class Analyzer(Unit):
    _namespace: Namespace
    _loader: Loader
    _builtin_lookup: BuiltinLookup

    def __init__(self, namespace: Namespace, loader: Loader) -> None:
        self._namespace = namespace
        self._loader = loader

    def load_module(self, module_name: str) -> None:
        module_id = self._namespace.add_or_get_module(module_name)
        if self._namespace.module_is_analyzed(module_id):
            return

        module_parts = module_name.split(".")
        module_path = Path(*module_parts).with_suffix(".rad")
        module_contents = self._loader.load_file(module_path)
        module_parser = Parser(
            Lexer(contents=module_contents, filename=str(module_path)),
            filename=str(module_path),
        )
        module_ast = module_parser.parse_module()
        self._analyze_module(module_id, module_ast)
        self._namespace.mark_module_analyzed(module_id)

    def _analyze_module(self, module_id: int, module_ast: ModuleNode) -> None:
        root_scope = AnalysisScope(
            module_id=module_id,
            namespace=self._namespace,
            parent=None,
        )
        self._builtin_lookup = setup_builtins(root_scope)
        populate_decls(root_scope, module_ast.body.declarations)

    def _check(self, result: AnalysisResult, bound: Type | None = None) -> None:
        if not result.type:
            self._infer(result)
        if bound and not result.error:
            assert result.type and isinstance(result.type.value, Type)
            result.error = result.type.value.unify(bound)

    def _infer(self, result: AnalysisResult) -> None:
        raise NotImplementedError()

    def _type_of(self, expr: ExpressionType) -> Type:
        raise NotImplementedError()
