from unittest import TestCase

import os

from radical.unit.parser.tokenizer import Tokenizer
from radical.util.testutils import collect_test_cases

if os.environ.get("RAD_DEBUG"):
    import debugpy

    debugpy.listen(5678)
    debugpy.wait_for_client()

class TestParser(TestCase):
    maxDiff = None

    def test_all(self):
        enabled_files_env = os.environ.get("RAD_TEST_FILES")
        enabled_files: list[str] | None
        if enabled_files_env:
            enabled_files = enabled_files_env.split(",")
        else:
            enabled_files = None
        test_cases = collect_test_cases("test_cases/tokenizer", enabled_files=enabled_files)
        for test_case in test_cases:
            with self.subTest(test_case.path):
                self.assertEqual(
                    test_case.expected_output,
                    "\n".join(str(t) for t in Tokenizer(test_case.contents, test_case.path).tokens())
                )
