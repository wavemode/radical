plainLiteral = "Hello, \n\r\t\\\"World!" -- end of line comment

multLineLiteral = """This is a
multi-line string.\n\r\t\\\""""

(* multiline
comment *)

rawLiteral = r"Raw string literal\n\r\t\\"

multiLineRawLiteral = r"""Raw multi-line
string literal.\n\r\t\\\"""

(*
Module(
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
)
*)
