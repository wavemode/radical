from radical.util.core.unit import Unit
from radical.unit.interp.namespace import Namespace


class Interpreter(Unit):
    _namespace: Namespace

    def __init__(self, namespace: Namespace) -> None:
        self._namespace = namespace
