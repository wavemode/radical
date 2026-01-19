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
Token(type=EOF, value="", position=(36, 1, 0))
*)
