from radical.data.interp.value import ValueType
from radical.data.sema.constref import ConstRef
from radical.data.sema.type import TypeType
from radical.data.sema.typeref import TypeRef
from radical.util.core.unit import Unit


class Module(Unit):
    _name: str
    _analyzed: bool
    _symbols: list[str]
    _symbol_map: dict[str, int]
    _imports: list[str]
    _constants: list[ValueType]
    _types: list[TypeType]
    _bindings: dict[int, ConstRef]
    _type_bindings: dict[int, TypeRef]

    def __init__(self, name: str) -> None:
        self._name = name
        self._analyzed = False
        self._symbols = []
        self._symbol_map = {}
        self._imports = []
        self._import_map = {}
        self._constants = []
        self._types = []
        self._bindings = {}
        self._type_bindings = {}

    def name(self) -> str:
        return self._name

    def is_analyzed(self) -> bool:
        return self._analyzed

    def mark_analyzed(self) -> None:
        self._analyzed = True

    def get_symbol(self, id: int) -> str:
        return self._symbols[id]

    def add_or_get_symbol(self, name: str) -> int:
        if name in self._symbol_map:
            return self._symbol_map[name]
        else:
            id = len(self._symbols)
            self._symbols.append(name)
            self._symbol_map[name] = id
            return id

    def add_import(self, name: str) -> int:
        id = len(self._imports)
        self._imports.append(name)
        return id

    def get_constant(self, id: int) -> ValueType:
        return self._constants[id]

    def add_constant(self, value: ValueType) -> int:
        id = len(self._constants)
        self._constants.append(value)
        return id

    def get_type(self, id: int) -> TypeType:
        return self._types[id]

    def add_type(self, type: TypeType) -> int:
        id = len(self._types)
        self._types.append(type)
        return id

    def bind_constant(self, symbol: int, const_ref: ConstRef) -> None:
        self._bindings[symbol] = const_ref

    def bind_type(self, symbol: int, type_ref: TypeRef) -> None:
        self._type_bindings[symbol] = type_ref
