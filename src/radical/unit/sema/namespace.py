from radical.unit.sema.module import Module
from radical.util.core.unit import Unit


class Namespace(Unit):
    _modules: list[Module]
    _module_id_by_name: dict[str, int]

    def __init__(self) -> None:
        self._modules = []
        self._module_id_by_name = {}
        self._imports = {}

    def add_or_get_module(self, name: str) -> int:
        if name in self._module_id_by_name:
            return self._module_id_by_name[name]
        else:
            id = len(self._modules)
            self._modules.append(Module(name))
            self._module_id_by_name[name] = id
            return id

    def module_is_analyzed(self, module_id: int) -> bool:
        return self._modules[module_id].is_analyzed()

    def mark_module_analyzed(self, module_id: int) -> None:
        self._modules[module_id].mark_analyzed()

    def intern_symbol(self, module_id: int, name: str) -> int:
        module = self._get_module(module_id)
        symbol_id = module.intern_symbol(name)
        return symbol_id

    def get_symbol(self, module_id: int, symbol_id: int) -> str:
        module = self._get_module(module_id)
        return module.get_symbol(symbol_id)

    def _get_module(self, id: int) -> Module:
        return self._modules[id]
