#!/usr/bin/env python3

from radical.util.testutils import (
    collect_test_cases,
    evaluate_lexer_test_case,
    evaluate_parser_test_case,
    evaluate_sema_test_case,
)


def fix_parser_tests():
    for test_case in collect_test_cases("test_cases/parser"):
        formatted = evaluate_parser_test_case(test_case)
        if formatted != test_case.expected_output:
            print(f"Updating test case: {test_case.path}")
            test_case.update_expected_output(formatted)


def fix_lexer_tests():
    for test_case in collect_test_cases("test_cases/lexer"):
        formatted = evaluate_lexer_test_case(test_case)
        if formatted != test_case.expected_output:
            print(f"Updating test case: {test_case.path}")
            test_case.update_expected_output(formatted)


def fix_sema_tests():
    for test_case in collect_test_cases("test_cases/sema"):
        formatted = evaluate_sema_test_case(test_case)
        if formatted != test_case.expected_output:
            print(f"Updating test case: {test_case.path}")
            test_case.update_expected_output(formatted)


def fix_all_tests():
    fix_lexer_tests()
    fix_parser_tests()
    fix_sema_tests()


if __name__ == "__main__":
    fix_all_tests()
    # run it again in case we messed up line/column positions
    fix_all_tests()
