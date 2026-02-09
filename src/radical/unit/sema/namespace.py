from radical.data.sema.value import Value
from radical.data.sema.constref import ConstRef
from radical.data.sema.symbolref import SymbolRef
from radical.data.sema.type import TypeKinds
from radical.data.sema.typeref import TypeRef
from radical.unit.sema.module import Module
from radical.util.core.unit import Unit


class Namespace(Unit):
    _modules: list[Module]
    _module_id_by_name: dict[str, int]
    _imports: dict[tuple[int, int], int]

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

    def add_or_get_import(self, from_module_id: int, to_module_id: int) -> int:
        if (from_module_id, to_module_id) in self._imports:
            return self._imports[(from_module_id, to_module_id)]
        to_module = self._modules[to_module_id]
        from_module = self._modules[from_module_id]
        import_id = from_module.add_import(to_module.name())
        self._imports[(from_module_id, to_module_id)] = import_id
        return import_id

    def module_is_analyzed(self, module_id: int) -> bool:
        return self._modules[module_id].is_analyzed()

    def mark_module_analyzed(self, module_id: int) -> None:
        self._modules[module_id].mark_analyzed()

    def intern_symbol(self, module_id: int, name: str) -> SymbolRef:
        module = self._get_module(module_id)
        symbol_id = module.add_or_get_symbol(name)
        return SymbolRef(module_id, symbol_id)

    def get_symbol(self, ref: SymbolRef) -> str:
        return self._modules[ref.module_id].get_symbol(ref.symbol_id)

    def intern_constant(self, module_id: int, value: Value) -> ConstRef:
        module = self._get_module(module_id)
        const_id = module.add_constant(value)
        return ConstRef(module_id, const_id)

    def get_constant(self, ref: ConstRef) -> Value:
        return self._modules[ref.module_id].get_constant(ref.const_id)

    def intern_type(self, module_id: int, type: TypeKinds) -> TypeRef:
        module = self._get_module(module_id)
        type_id = module.add_type(type)
        return TypeRef(module_id, type_id)

    def get_type(self, ref: TypeRef) -> TypeKinds:
        return self._modules[ref.module_id].get_type(ref.type_id)

    def lookup_binding(self, symbol: SymbolRef) -> ConstRef:
        module = self._get_module(symbol.module_id)
        return module.lookup_binding(symbol.symbol_id)

    def bind_constant(self, symbol: SymbolRef, const_ref: ConstRef) -> None:
        module = self._get_module(symbol.module_id)
        module.bind_constant(symbol.symbol_id, const_ref)

    def lookup_type_binding(self, symbol: SymbolRef) -> TypeRef:
        module = self._get_module(symbol.module_id)
        return module.lookup_type_binding(symbol.symbol_id)

    def bind_type(self, symbol: SymbolRef, type_ref: TypeRef) -> None:
        module = self._get_module(symbol.module_id)
        module.bind_type(symbol.symbol_id, type_ref)

    def _get_module(self, id: int) -> Module:
        return self._modules[id]
