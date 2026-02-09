from pathlib import Path
from radical.effect.filesystem.file_reader import FileReader
from radical.util.core.unit import Unit


class Loader(Unit):
    _file_reader: FileReader
    _loaded_files: dict[Path, str]

    def __init__(self, file_reader: FileReader) -> None:
        self._file_reader = file_reader
        self._loaded_files = {}
        self._resolved_modules = {}

    def file_is_loaded(self, path: Path) -> bool:
        return path in self._loaded_files

    def load_file(self, path: Path) -> str:
        if path in self._loaded_files:
            return self._loaded_files[path]

        contents = self._file_reader.read_contents(path)
        self._loaded_files[path] = contents
        return contents
