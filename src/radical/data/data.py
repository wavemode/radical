import json
from typing import Any, cast


class Data:
    def __str__(self) -> str:
        return self.format()

    def format(self, indent_level: int = 0) -> str:
        parts: list[str] = [self.format_name(), "(\n"]
        parts.append(self.format_fields(indent_level=indent_level))
        parts.append(f"\n{' ' * 4 * indent_level})")
        return "".join(parts)

    def format_name(self) -> str:
        return self.__class__.__name__

    def format_fields(self, indent_level: int = 0) -> str:
        parts: list[str] = []

        field_lines: list[str] = []
        for field_name, field_value in self.__dict__.items():
            if field_value is None:
                continue
            field_lines.append(
                pretty_print_field(
                    field_value, name=field_name, indent_level=indent_level + 1
                )
            )
        parts.append(",\n".join(field_lines))
        return "".join(parts)


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
