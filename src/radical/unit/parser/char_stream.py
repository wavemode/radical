from radical.data.parser.errors import EndOfFileError, PositionOutOfBoundsError
from radical.data.parser.position import Position
from radical.util.core.unit import Unit


class CharStream(Unit):
    _data: list[str]
    _position: Position

    def __init__(self, data: str) -> None:
        super().__init__()
        self._data = data.splitlines(keepends=True)
        self._position = Position(line=1, column=1)

    def at_end(self) -> bool:
        return self._position.line > len(self._data)

    def advance(self, n: int = 1) -> None:
        for _ in range(n):
            self._advance()

    def read_char(self) -> str:
        char = self.peek_char()
        self._advance()
        return char

    def read_chars(self, n: int) -> str:
        chars: list[str] = []
        for _ in range(n):
            chars.append(self.read_char())
        return "".join(chars)

    def peek_char(self) -> str:
        return self._char_at(self._position.line, self._position.column)

    def peek_chars(self, n: int) -> str:
        current_position = self.get_position()
        chars = self.read_chars(n)
        self.reset_position(current_position)
        return chars

    def get_position(self) -> Position:
        return Position(line=self._position.line, column=self._position.column)

    def reset_position(self, position: Position) -> None:
        self._position.line = position.line
        self._position.column = position.column

    def _char_at(self, line: int, column: int) -> str:
        if line < 1 or line > len(self._data):
            raise PositionOutOfBoundsError()
        line_content = self._data[line - 1]
        if column < 1 or column > len(line_content) + 1:
            raise PositionOutOfBoundsError()
        return line_content[column - 1]

    def _advance(self) -> None:
        if self.at_end():
            raise EndOfFileError()
        current_line_content = self._data[self._position.line - 1]
        if self._position.column == len(current_line_content):
            self._position.line += 1
            self._position.column = 1
        else:
            self._position.column += 1
