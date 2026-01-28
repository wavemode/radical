from unittest import TestCase

import os

from radical.unit.parser.lexer import Lexer
from radical.util.testutils import collect_test_cases

if os.environ.get("RAD_DEBUG"):
    import debugpy

    debugpy.listen(5678)
    debugpy.wait_for_client()


class TestLexer(TestCase):
    maxDiff = None

    def test_all(self):
        test_cases = collect_test_cases("test_cases/lexer")
        for test_case in test_cases:
            with self.subTest(test_case.path):
                try:
                    with Lexer(test_case.contents, filename=test_case.path) as lexer:
                        tokens = lexer.read_all()
                        expected_output = "\n".join(str(token) for token in tokens)
                except Exception as e:
                    expected_output = f"FAIL({str(e)})"
                self.assertEqual(
                    test_case.expected_output,
                    expected_output,
                )
