from unittest import TestCase

import os

from radical.unit.parser.lexer import Lexer
from radical.unit.parser.parser import Parser
from radical.util.testutils import collect_test_cases
import json

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
                try:
                    with (
                        Lexer(test_case.contents, filename=test_case.path) as lexer,
                        Parser(lexer=lexer, filename=test_case.path) as parser,
                    ):
                        expected_output = parser.parse_module().format()
                except Exception as e:
                    expected_output = f"FAIL({json.dumps(str(e))})"
                self.assertEqual(
                    test_case.expected_output,
                    expected_output,
                )
