from unittest import TestCase
from radical.unit.parser.parser import Parser
from radical.unit.parser.char_stream import CharStream
import textwrap

import os


def _parser_from_text(text: str) -> Parser:
    return Parser(CharStream(textwrap.dedent(text)))


class TestParser(TestCase):
    maxDiff = None

    def _assert_matching_output(self, text: str):
        parser = _parser_from_text(text)
        module = parser.parse_module()
        formatted = module.format()
        test_case_start = text.rfind("(*")
        test_case_end = text.rfind("*)")
        test_case = text[test_case_start + 2 : test_case_end].strip()
        if formatted != test_case:
            raise AssertionError(
                f"Parsed output did not match expected output."
                f"\n\nExpected:\n{test_case}\n\n"
                f"Got:\n{formatted}"
            )

    def test_all(self):
        for root, _, files in os.walk("tests/parser"):
            for file in files:
                if file.endswith(".rd"):
                    file_path = os.path.join(root, file)
                    with open(file_path, "r") as f:
                        text = f.read()
                    with self.subTest(file_path):
                        self._assert_matching_output(text)


def fix_all_files():
    for root, _, files in os.walk("tests/parser"):
        for file in files:
            if file.endswith(".rd"):
                file_path = os.path.join(root, file)
                with open(file_path, "rw") as f:
                    text = f.read()
                    parser = _parser_from_text(text)
                    module = parser.parse_module()
                    formatted = module.format()
                    test_case_start = text.rfind("(*")
                    test_case_end = text.rfind("*)")
                    new_text = (
                        text[: test_case_start + 2]
                        + "\n"
                        + formatted
                        + "\n"
                        + text[test_case_end:]
                    )
                    f.write(new_text)
