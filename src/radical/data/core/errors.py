from radical.data.parser.position import Position


class ErrorAtCodeLocation(Exception):
    """Raised when a parsing error occurs."""

    def __init__(self, message: str, position: Position, filename: str) -> None:
        super().__init__(f"{message} at {filename}:{position.line}:{position.column}")
        self.message = message
        self.position = position
