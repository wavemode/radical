from abc import ABC
from typing import Any


class Unit(ABC):
    _children: list["Unit"]

    def __enter__(self):
        return self

    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        self.close()

    def add_child[T: "Unit"](self, child: T) -> T:
        if not hasattr(self, "_children"):
            self._children = []
        self._children.append(child)
        return child

    def close(self) -> None:
        if hasattr(self, "_children"):
            for child in reversed(self._children):
                child.close()
        self.destroy()

    def destroy(self) -> None:
        pass
