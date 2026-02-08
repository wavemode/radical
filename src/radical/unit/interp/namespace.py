from radical.data.interp.value import ValueType
from radical.data.sema.constref import ConstRef
from radical.data.sema.symbolref import SymbolRef
from radical.data.sema.type import TypeType
from radical.data.sema.typeref import TypeRef
from radical.unit.interp.module import Module
from radical.util.core.unit import Unit


class Namespace(Unit):
    _modules: list[Module]

    def __init__(self) -> None:
        self._modules = []

    def get_module(self, id: int) -> Module:
        return self._modules[id]

    def intern_symbol(self, module_id: int, name: str) -> SymbolRef:
        module = self.get_module(module_id)
        symbol_id = module.add_symbol(name)
        return SymbolRef(module_id, symbol_id)

    def get_symbol(self, ref: SymbolRef) -> str:
        return self._modules[ref.module_id].get_symbol(ref.symbol_id)

    def intern_constant(self, module_id: int, value: ValueType) -> ConstRef:
        module = self.get_module(module_id)
        const_id = module.add_constant(value)
        return ConstRef(module_id, const_id)

    def get_constant(self, ref: ConstRef) -> ValueType:
        return self._modules[ref.module_id].get_constant(ref.const_id)

    def intern_type(self, module_id: int, type: TypeType) -> TypeRef:
        module = self.get_module(module_id)
        type_id = module.add_type(type)
        return TypeRef(module_id, type_id)

    def get_type(self, ref: TypeRef) -> TypeType:
        return self._modules[ref.module_id].get_type(ref.type_id)

    def bind_constant(self, symbol: SymbolRef, const_ref: ConstRef) -> None:
        module = self.get_module(symbol.module_id)
        module.bind_constant(symbol.symbol_id, const_ref)

    def bind_type(self, symbol: SymbolRef, type_ref: TypeRef) -> None:
        module = self.get_module(symbol.module_id)
        module.bind_type(symbol.symbol_id, type_ref)
