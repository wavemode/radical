from radical.data.sema.value import Value
from radical.util.core.unit import Unit


class Module(Unit):
    _name: str
    _analyzed: bool
    _symbols: list[str]
    _symbol_map: dict[str, int]
    _bindings: dict[int, Value]
    _type_bindings: dict[int, Value]

    def __init__(self, name: str) -> None:
        self._name = name
        self._analyzed = False
        self._symbols = []
        self._symbol_map = {}
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

    def intern_symbol(self, name: str) -> int:
        if name in self._symbol_map:
            return self._symbol_map[name]
        else:
            id = len(self._symbols)
            self._symbols.append(name)
            self._symbol_map[name] = id
            return id
