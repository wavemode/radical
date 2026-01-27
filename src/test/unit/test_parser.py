from unittest import TestCase

import os

from radical.unit.parser.lexer import Lexer
from radical.unit.parser.parser import Parser
from radical.util.testutils import collect_test_cases

if os.environ.get("RAD_DEBUG"):
    import debugpy

    debugpy.listen(5678)
    debugpy.wait_for_client()


class TestParser(TestCase):
    maxDiff = None

    def test_all(self):
        test_cases = collect_test_cases("test_cases/parser")
        for test_case in test_cases:
            with self.subTest(test_case.path):
                self.assertEqual(
                    test_case.expected_output,
                    Parser(
                        lexer=Lexer(
                            contents=test_case.contents,
                            filename=test_case.path,
                        ),
                        filename=test_case.path,
                    )
                    .parse_module()
                    .format(),
                )
