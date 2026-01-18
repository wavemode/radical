#!/usr/bin/env python3

from radical.unit.parser.file_parser import FileParser
from radical.unit.parser.char_stream import CharStream
import textwrap

from radical.util.testutils import collect_test_cases


def _parser_from_text(text: str, filename: str) -> FileParser:
    return FileParser(CharStream(textwrap.dedent(text)), filename=filename)


def fix_parser_tests():
    for test_case in collect_test_cases("test_cases/parser"):
        parser = _parser_from_text(test_case.contents, filename=test_case.path)
        module = parser.parse_module()
        formatted = module.format()
        test_case.update_expected_output(formatted)


if __name__ == "__main__":
    fix_parser_tests()
    # run it again in case we messed up line/column positions
    fix_parser_tests()
