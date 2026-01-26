from unittest import TestCase
from radical.unit.parser.file_parser import FileParser
from radical.unit.parser.char_stream import CharStream
import textwrap

import os

if os.environ.get("RAD_DEBUG"):
    import debugpy

    debugpy.listen(5678)
    debugpy.wait_for_client()


def _parser_from_text(text: str, filename: str) -> FileParser:
    return FileParser(CharStream(textwrap.dedent(text)), filename=filename)


class TestParser(TestCase):
    maxDiff = None

    def _assert_matching_output(self, text: str, filename: str):
        parser = _parser_from_text(text, filename=filename)
        module = parser.parse_module()
        formatted = module.format()
        test_case_start = text.rfind("(*")
        test_case_end = text.rfind("*)")
        if test_case_start == -1 or test_case_end == -1:
            raise ValueError(
                "Test case must contain expected output enclosed in (* ... *)"
            )
        test_case = text[test_case_start + 2 : test_case_end].strip()
        if formatted != test_case:
            raise AssertionError(
                f"Parsed output did not match expected output."
                f"\n\nExpected:\n{test_case}\n\n"
                f"Got:\n{formatted}"
            )

    def test_all(self):
        enabled_files_env = os.environ.get("RAD_TEST_FILES")
        enabled_files: list[str] | None
        if enabled_files_env:
            enabled_files = enabled_files_env.split(",")
        else:
            enabled_files = None

        for root, _, files in os.walk("test_cases/parser"):
            for file in files:
                if not file.endswith(".rad"):
                    continue
                file_path = os.path.join(root, file)
                if enabled_files is not None and file_path not in enabled_files:
                    continue
                with open(file_path, "r") as f:
                    text = f.read()
                with self.subTest(file_path):
                    self._assert_matching_output(text, filename=file_path)
