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
Module(
    position=(1, 1),
    top_level_nodes=[
        VariableBindingStatement(
            position=(1, 1),
            name=Symbol(
                position=(1, 1),
                name="plainLiteral"
            ),
            value=StringLiteral(
                position=(1, 16),
                value="Hello, \n\r\t\\\"World!"
            )
        ),
        VariableBindingStatement(
            position=(3, 1),
            name=Symbol(
                position=(3, 1),
                name="PLAIN_LITERAL_WITH_UPPERCASE_NAME"
            ),
            value=StringLiteral(
                position=(3, 37),
                value="This is a test string."
            )
        ),
        VariableBindingStatement(
            position=(4, 1),
            name=Symbol(
                position=(4, 1),
                name="_PLAIN_LITERAL_WITH_UNDERSCORE"
            ),
            value=StringLiteral(
                position=(4, 34),
                value="Another test string."
            )
        ),
        VariableBindingStatement(
            position=(6, 1),
            name=Symbol(
                position=(6, 1),
                name="multLineLiteral"
            ),
            value=MultiLineStringLiteral(
                position=(6, 19),
                value="This is a\nmulti-line string.\n\r\t\\\""
            )
        ),
        VariableBindingStatement(
            position=(12, 1),
            name=Symbol(
                position=(12, 1),
                name="rawLiteral"
            ),
            value=RawStringLiteral(
                position=(12, 14),
                value="Raw string literal\\n\\r\\t\\\\"
            )
        ),
        VariableBindingStatement(
            position=(14, 1),
            name=Symbol(
                position=(14, 1),
                name="multiLineRawLiteral"
            ),
            value=RawMultiLineStringLiteral(
                position=(14, 23),
                value="Raw multi-line\nstring literal.\\n\\r\\t\\\\\\"
            )
        )
    ]
)
*)
