#!/usr/bin/env python3

from radical.unit.parser.file_parser import FileParser
from radical.unit.parser.char_stream import CharStream
import textwrap

import os


def _parser_from_text(text: str, filename: str) -> FileParser:
    return FileParser(CharStream(textwrap.dedent(text)), filename=filename)


def fix_parser_tests():
    for root, _, files in os.walk("test_cases/parser"):
        for file in files:
            if file.endswith(".rd"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    text = f.read()
                parser = _parser_from_text(text, filename=file_path)
                module = parser.parse_module()
                formatted = module.format()
                test_case_start = text.rfind("(*")
                test_case_end = text.rfind("*)")

                if test_case_start == -1 or test_case_end == -1:
                    test_case_start = len(text)
                    test_case_end = len(text)

                new_text = (
                    text[:test_case_start]
                    + "(*\n"
                    + formatted
                    + "\n*)"
                    + text[test_case_end + 2 :]
                )
                with open(file_path, "w") as f:
                    f.write(new_text)


if __name__ == "__main__":
    fix_parser_tests()
