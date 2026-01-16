from radical.data.parser.position import Position


class EndOfFileError(Exception):
    """Raised when the end of the file is reached unexpectedly during parsing."""

    pass


class PositionOutOfBoundsError(Exception):
    """Raised when a position is set outside the valid range of the data."""

    pass


class ParseError(Exception):
    """Raised when a parsing error occurs."""

    def __init__(self, message: str, position: Position, filename: str) -> None:
        super().__init__(f"{message} at {filename}:{position.line}:{position.column}")
        self.message = message
        self.position = position
