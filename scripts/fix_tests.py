#!/usr/bin/env python3

from radical.unit.parser.lexer import Lexer
from radical.util.testutils import collect_test_cases


from radical.unit.parser.parser import Parser


def fix_parser_tests():
    for test_case in collect_test_cases("test_cases/parser"):
        try:
            with (
                Lexer(test_case.contents, filename=test_case.path) as lexer,
                Parser(lexer=lexer, filename=test_case.path) as parser,
            ):
                formatted = parser.parse_module().format()
        except Exception as e:
            formatted = f"FAIL({str(e)})"
        test_case.update_expected_output(formatted)


def fix_lexer_tests():
    for test_case in collect_test_cases("test_cases/lexer"):
        try:
            with Lexer(test_case.contents, filename=test_case.path) as lexer:
                formatted = "\n".join(str(token) for token in lexer.read_all())
        except Exception as e:
            formatted = f"FAIL({str(e)})"
        test_case.update_expected_output(formatted)


def fix_all_tests():
    fix_lexer_tests()
    fix_parser_tests()


if __name__ == "__main__":
    fix_all_tests()
    # run it again in case we messed up line/column positions
    fix_all_tests()
