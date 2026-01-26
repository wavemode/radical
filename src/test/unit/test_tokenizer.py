from unittest import TestCase

import os

from radical.unit.parser.lexer import Lexer
from radical.util.testutils import collect_test_cases

if os.environ.get("RAD_DEBUG"):
    import debugpy

    debugpy.listen(5678)
    debugpy.wait_for_client()


class TestParser(TestCase):
    maxDiff = None

    def test_all(self):
        test_cases = collect_test_cases("test_cases/tokenizer")
        for test_case in test_cases:
            with self.subTest(test_case.path):
                self.assertEqual(
                    test_case.expected_output,
                    "\n".join(
                        str(t)
                        for t in Lexer(
                            test_case.contents, test_case.path
                        ).read_all()
                    ),
                )
