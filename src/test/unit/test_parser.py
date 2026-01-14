from unittest import TestCase
from radical.unit.parser.parser import Parser
from radical.unit.parser.char_stream import CharStream
import textwrap

import os


class TestParser(TestCase):
    maxDiff = None

    def _parser_from_text(self, text: str) -> Parser:
        return Parser(CharStream(textwrap.dedent(text)))

    def _assert_matching_output(self, text: str):
        parser = self._parser_from_text(text)
        module = parser.parse_module()
        formatted = module.format()
        text_case_start = text.rfind("(*")
        test_case_end = text.rfind("*)")
        test_case = text[text_case_start + 2 : test_case_end].strip()
        self.assertEqual(formatted, test_case)

    def test_all(self):
        for root, _, files in os.walk("tests/parser"):
            for file in files:
                if file.endswith(".rd"):
                    file_path = os.path.join(root, file)
                    with open(file_path, "r") as f:
                        text = f.read()
                    with self.subTest(file_path):
                        self._assert_matching_output(text)
