from pathlib import Path
from radical.util.core.unit import Unit


class FileReader(Unit):
    def read_contents(self, path: Path) -> str:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
