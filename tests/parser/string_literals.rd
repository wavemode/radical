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
    top_level_nodes=[
        VariableBindingStatement(
            name=Symbol(
                name="plainLiteral"
            ),
            value=StringLiteral(
                value="Hello, \n\r\t\\\"World!"
            )
        ),
        VariableBindingStatement(
            name=Symbol(
                name="PLAIN_LITERAL_WITH_UPPERCASE_NAME"
            ),
            value=StringLiteral(
                value="This is a test string."
            )
        ),
        VariableBindingStatement(
            name=Symbol(
                name="_PLAIN_LITERAL_WITH_UNDERSCORE"
            ),
            value=StringLiteral(
                value="Another test string."
            )
        ),
        VariableBindingStatement(
            name=Symbol(
                name="multLineLiteral"
            ),
            value=MultiLineStringLiteral(
                value="This is a\nmulti-line string.\n\r\t\\\""
            )
        ),
        VariableBindingStatement(
            name=Symbol(
                name="rawLiteral"
            ),
            value=RawStringLiteral(
                value="Raw string literal\\n\\r\\t\\\\"
            )
        ),
        VariableBindingStatement(
            name=Symbol(
                name="multiLineRawLiteral"
            ),
            value=RawMultiLineStringLiteral(
                value="Raw multi-line\nstring literal.\\n\\r\\t\\\\\\"
            )
        )
    ]
)
*)
