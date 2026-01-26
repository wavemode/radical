#!/usr/bin/env python3

from radical.unit.parser.lexer import Lexer
from radical.unit.parser.file_parser import FileParser
from radical.unit.parser.char_stream import CharStream

from radical.util.testutils import collect_test_cases


def _parser_from_text(text: str, filename: str) -> FileParser:
    return FileParser(CharStream(text), filename=filename)


def fix_parser_tests():
    for test_case in collect_test_cases("test_cases/parser"):
        with _parser_from_text(test_case.contents, filename=test_case.path) as parser:
            module = parser.parse_module()
            formatted = module.format()
            test_case.update_expected_output(formatted)


def fix_lexer_tests():
    for test_case in collect_test_cases("test_cases/lexer"):
        with Lexer(test_case.contents, filename=test_case.path) as lexer:
            formatted = "\n".join(str(token) for token in lexer.read_all())
            test_case.update_expected_output(formatted)


if __name__ == "__main__":
    fix_lexer_tests()
    fix_parser_tests()
    # run it again in case we messed up line/column positions
    fix_lexer_tests()
    fix_parser_tests()
