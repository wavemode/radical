from unittest import TestCase
from radical.unit.parser.parser import Parser
from radical.unit.parser.char_stream import CharStream
from radical.data.parser.ast import (
    DefinitionNode,
    Position,
    StringLiteralNode,
    MultiLineStringLiteralNode,
    RawStringLiteralNode,
    RawMultiLineStringLiteralNode
)
import textwrap


class TestParser(TestCase):
    maxDiff = None

    def _parser_from_text(self, text: str) -> Parser:
        return Parser(CharStream(textwrap.dedent(text)))

    def test_string_literal_declarations(self):
        parser = self._parser_from_text("""\
            plain_literal = "Hello, \\n\\r\\t\\\\World!"
            multiline_literal = \"\"\"This is a
            multi-line string.\\n\\r\\t\\\\\"\"\"
            raw_literal = r"Raw string literal\\n\\r\\t\\\\"
            multiline_raw_literal = r\"\"\"Raw multi-line
            string literal.\\n\\r\\t\\\\\"\"\"
        """)
        module_node = parser.parse_module()
        self.assertEqual(len(module_node.top_level_nodes), 4)
        self.assertEqual(
            module_node.top_level_nodes[0],
            DefinitionNode(
                position=Position(line=1, column=1),
                name="plain_literal",
                value=StringLiteralNode(
                    position=Position(line=1, column=17),
                    value="Hello, \n\r\t\\World!",
                ),
            ),
        )
        self.assertEqual(
            module_node.top_level_nodes[1],
            DefinitionNode(
                position=Position(line=2, column=1),
                name="multiline_literal",
                value=MultiLineStringLiteralNode(
                    position=Position(line=2, column=21),
                    value="This is a\nmulti-line string.\n\r\t\\",
                ),
            ),
        )
        self.assertEqual(
            module_node.top_level_nodes[2],
            DefinitionNode(
                position=Position(line=4, column=1),
                name="raw_literal",
                value=RawStringLiteralNode(
                    position=Position(line=4, column=15),
                    value="Raw string literal\\n\\r\\t\\\\",
                ),
            ),
        )
        self.assertEqual(
            module_node.top_level_nodes[3],
            DefinitionNode(
                position=Position(line=5, column=1),
                name="multiline_raw_literal",
                value=RawMultiLineStringLiteralNode(
                    position=Position(line=5, column=25),
                    value="Raw multi-line\nstring literal.\\n\\r\\t\\\\",
                ),
            ),
        )
