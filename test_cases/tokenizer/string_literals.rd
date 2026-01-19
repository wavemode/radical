plainLiteral = "Hello, \n\r\t\\\"World!" -- end of line comment

PLAIN_LITERAL_WITH_UPPERCASE_NAME = "This is a test string."
_PLAIN_LITERAL_WITH_UNDERSCORE = "Another test string."

multLineLiteral = """This is a
multi-line string.\n\r\t\\\""""

(* multiline
comment *)

rawLiteral = r"Raw string literal\n\r\t\\"

multiLineRawLiteral = r"""Raw multi-line
string literal.\n\r\t\\\"""

formatStringNoExpression = f"This is a format string with no expressions!"
formatStringEntirelyExpression = f"{1 + 2 + 3}"
formatStringMixed = f"This is a format string with a value: {1 + 2 - 3 / abc} and another: { abc+def }!"
nestedFormatString = f"Outer {f"Inner {f"even more inner {42}"}"} string!"

multilineFormatString = f"""This is a
multi-line format string with an expression: {10 * 2} and more text."""

(*
Token(type=SYMBOL, value="plainLiteral", position=(1, 1, 0))
Token(type=ASSIGN, value="=", position=(1, 14, 0))
Token(type=STRING_LITERAL, value="Hello, \n\r\t\\\"World!", position=(1, 16, 0))
Token(type=SYMBOL, value="PLAIN_LITERAL_WITH_UPPERCASE_NAME", position=(3, 1, 0))
Token(type=ASSIGN, value="=", position=(3, 35, 0))
Token(type=STRING_LITERAL, value="This is a test string.", position=(3, 37, 0))
Token(type=SYMBOL, value="_PLAIN_LITERAL_WITH_UNDERSCORE", position=(4, 1, 0))
Token(type=ASSIGN, value="=", position=(4, 32, 0))
Token(type=STRING_LITERAL, value="Another test string.", position=(4, 34, 0))
Token(type=SYMBOL, value="multLineLiteral", position=(6, 1, 0))
Token(type=ASSIGN, value="=", position=(6, 17, 0))
Token(type=MULTILINE_STRING_LITERAL, value="This is a\nmulti-line string.\n\r\t\\\"", position=(6, 19, 0))
Token(type=SYMBOL, value="rawLiteral", position=(11, 1, 0))
Token(type=ASSIGN, value="=", position=(11, 12, 0))
Token(type=RAW_STRING_LITERAL, value="Raw string literal\\n\\r\\t\\\\", position=(11, 14, 0))
Token(type=SYMBOL, value="multiLineRawLiteral", position=(13, 1, 0))
Token(type=ASSIGN, value="=", position=(13, 21, 0))
Token(type=RAW_MULTILINE_STRING_LITERAL, value="Raw multi-line\nstring literal.\\n\\r\\t\\\\\\", position=(13, 23, 0))
Token(type=SYMBOL, value="formatStringNoExpression", position=(15, 1, 0))
Token(type=ASSIGN, value="=", position=(15, 26, 0))
Token(type=FORMAT_STRING_START, value="f\"", position=(15, 28, 0))
Token(type=FORMAT_STRING_SECTION, value="This is a format string with no expressions!", position=(15, 30, 0))
Token(type=FORMAT_STRING_END, value="\"", position=(15, 74, 0))
Token(type=SYMBOL, value="formatStringEntirelyExpression", position=(16, 1, 0))
Token(type=ASSIGN, value="=", position=(16, 32, 0))
Token(type=FORMAT_STRING_START, value="f\"", position=(16, 34, 0))
Token(type=FORMAT_STRING_EXPR_START, value="{", position=(16, 36, 0))
Token(type=INTEGER_LITERAL, value="1", position=(16, 37, 0))
Token(type=PLUS, value="+", position=(16, 39, 0))
Token(type=INTEGER_LITERAL, value="2", position=(16, 41, 0))
Token(type=PLUS, value="+", position=(16, 43, 0))
Token(type=INTEGER_LITERAL, value="3", position=(16, 45, 0))
Token(type=FORMAT_STRING_EXPR_END, value="}", position=(16, 46, 0))
Token(type=FORMAT_STRING_END, value="\"", position=(16, 47, 0))
Token(type=SYMBOL, value="formatStringMixed", position=(17, 1, 0))
Token(type=ASSIGN, value="=", position=(17, 19, 0))
Token(type=FORMAT_STRING_START, value="f\"", position=(17, 21, 0))
Token(type=FORMAT_STRING_SECTION, value="This is a format string with a value: ", position=(17, 23, 0))
Token(type=FORMAT_STRING_EXPR_START, value="{", position=(17, 61, 0))
Token(type=INTEGER_LITERAL, value="1", position=(17, 62, 0))
Token(type=PLUS, value="+", position=(17, 64, 0))
Token(type=INTEGER_LITERAL, value="2", position=(17, 66, 0))
Token(type=MINUS, value="-", position=(17, 68, 0))
Token(type=INTEGER_LITERAL, value="3", position=(17, 70, 0))
Token(type=DIVIDE, value="/", position=(17, 72, 0))
Token(type=SYMBOL, value="abc", position=(17, 74, 0))
Token(type=FORMAT_STRING_EXPR_END, value="}", position=(17, 77, 0))
Token(type=FORMAT_STRING_SECTION, value=" and another: ", position=(17, 78, 0))
Token(type=FORMAT_STRING_EXPR_START, value="{", position=(17, 92, 0))
Token(type=SYMBOL, value="abc", position=(17, 94, 0))
Token(type=PLUS, value="+", position=(17, 97, 0))
Token(type=SYMBOL, value="def", position=(17, 98, 0))
Token(type=FORMAT_STRING_EXPR_END, value="}", position=(17, 102, 0))
Token(type=FORMAT_STRING_SECTION, value="!", position=(17, 103, 0))
Token(type=FORMAT_STRING_END, value="\"", position=(17, 104, 0))
Token(type=SYMBOL, value="nestedFormatString", position=(18, 1, 0))
Token(type=ASSIGN, value="=", position=(18, 20, 0))
Token(type=FORMAT_STRING_START, value="f\"", position=(18, 22, 0))
Token(type=FORMAT_STRING_SECTION, value="Outer ", position=(18, 24, 0))
Token(type=FORMAT_STRING_EXPR_START, value="{", position=(18, 30, 0))
Token(type=FORMAT_STRING_START, value="f\"", position=(18, 31, 0))
Token(type=FORMAT_STRING_SECTION, value="Inner ", position=(18, 33, 0))
Token(type=FORMAT_STRING_EXPR_START, value="{", position=(18, 39, 0))
Token(type=FORMAT_STRING_START, value="f\"", position=(18, 40, 0))
Token(type=FORMAT_STRING_SECTION, value="even more inner ", position=(18, 42, 0))
Token(type=FORMAT_STRING_EXPR_START, value="{", position=(18, 58, 0))
Token(type=INTEGER_LITERAL, value="42", position=(18, 59, 0))
Token(type=FORMAT_STRING_EXPR_END, value="}", position=(18, 61, 0))
Token(type=FORMAT_STRING_END, value="\"", position=(18, 62, 0))
Token(type=FORMAT_STRING_EXPR_END, value="}", position=(18, 63, 0))
Token(type=FORMAT_STRING_END, value="\"", position=(18, 64, 0))
Token(type=FORMAT_STRING_EXPR_END, value="}", position=(18, 65, 0))
Token(type=FORMAT_STRING_SECTION, value=" string!", position=(18, 66, 0))
Token(type=FORMAT_STRING_END, value="\"", position=(18, 74, 0))
Token(type=SYMBOL, value="multilineFormatString", position=(20, 1, 0))
Token(type=ASSIGN, value="=", position=(20, 23, 0))
Token(type=MULTILINE_FORMAT_STRING_START, value="f\"\"\"", position=(20, 25, 0))
Token(type=MULTILINE_FORMAT_STRING_SECTION, value="This is a\nmulti-line format string with an expression: ", position=(20, 29, 0))
Token(type=FORMAT_STRING_EXPR_START, value="{", position=(20, 84, 0))
Token(type=INTEGER_LITERAL, value="10", position=(20, 85, 0))
Token(type=MULTIPLY, value="*", position=(20, 88, 0))
Token(type=INTEGER_LITERAL, value="2", position=(20, 90, 0))
Token(type=FORMAT_STRING_EXPR_END, value="}", position=(20, 91, 0))
Token(type=MULTILINE_FORMAT_STRING_SECTION, value=" and more text.", position=(20, 92, 0))
Token(type=MULTILINE_FORMAT_STRING_END, value="\"\"\"", position=(20, 107, 0))
Token(type=EOF, value="", position=(110, 1, 0))
*)
