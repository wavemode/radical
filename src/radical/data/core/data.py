import json
from typing import Any, cast


class Data:
    def __str__(self) -> str:
        return self.format()

    def format(self, indent_level: int = 0) -> str:
        parts: list[str] = [self.format_name(), "("]
        field_lines = self.format_fields(indent_level=indent_level + 1)
        if field_lines:
            parts.append("\n")
            parts.append(",\n".join(field_lines))
            parts.append(f"\n{' ' * 4 * indent_level}")
        parts.append(")")
        return "".join(parts)

    def format_name(self) -> str:
        return self.__class__.__name__

    def format_field(self, name: str, indent_level: int = 0) -> str | None:
        value = getattr(self, name)
        if value is not None:
            return pretty_print_field(value, name=name, indent_level=indent_level)

    def format_fields(self, indent_level: int = 0) -> list[str]:
        field_lines: list[str] = []
        for field_name in self.__dict__.keys():
            field_line = self.format_field(field_name, indent_level=indent_level)
            if field_line is not None:
                field_lines.append(field_line)
        return field_lines


def pretty_print_field(
    value: Any, name: str | None = None, indent_level: int = 0
) -> str:
    indent = " " * 4 * indent_level
    parts: list[str] = [indent]
    if name is not None:
        parts.append(f"{name}=")
    if isinstance(value, Data):
        parts.append(value.format(indent_level=indent_level))
    elif isinstance(value, list):
        parts.append("[\n")
        element_lines: list[str] = []
        for element in cast(list[Any], value):
            element_lines.append(
                pretty_print_field(element, indent_level=indent_level + 1)
            )
        parts.append(",\n".join(element_lines))
        parts.append(f"\n{indent}]")
    else:
        parts.append(json.dumps(value))
    return "".join(parts)
