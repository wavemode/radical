#!/usr/bin/env python3

from radical.unit.parser.lexer import Lexer
from radical.util.testutils import collect_test_cases


from radical.unit.parser.parser import Parser


def fix_parser_tests():
    for test_case in collect_test_cases("test_cases/parser"):
        with (
            Lexer(test_case.contents, filename=test_case.path) as lexer,
            Parser(lexer=lexer, filename=test_case.path) as parser,
        ):
            formatted = parser.parse_module().format()
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
