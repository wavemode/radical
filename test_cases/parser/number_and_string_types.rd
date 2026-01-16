five : 5 = 5
six : 5.5 = 5.5
sci : 1.2e3 = 1.2e3

basicStringType : "hello" = "hello"
rawStringType : r"raw\nstring" = r"raw\nstring"
multiLineStringType : """multi
line
string""" = """multi
line
string"""

rawMultiLineStringType : r"""raw
multi
line
string""" = r"""raw
multi
line
string"""

(*
Module(
    position=(1, 1),
    top_level_nodes=[
        VariableBindingStatement(
            position=(1, 1),
            name=Symbol(
                position=(1, 1),
                name="five"
            ),
            value=IntegerLiteral(
                position=(1, 12),
                value="5"
            ),
            type=NumberLiteralType(
                position=(1, 8),
                value=IntegerLiteral(
                    position=(1, 8),
                    value="5"
                )
            )
        ),
        VariableBindingStatement(
            position=(2, 1),
            name=Symbol(
                position=(2, 1),
                name="six"
            ),
            value=FloatLiteral(
                position=(2, 13),
                value="5.5"
            ),
            type=NumberLiteralType(
                position=(2, 7),
                value=FloatLiteral(
                    position=(2, 7),
                    value="5.5"
                )
            )
        ),
        VariableBindingStatement(
            position=(3, 1),
            name=Symbol(
                position=(3, 1),
                name="sci"
            ),
            value=SciFloatLiteral(
                position=(3, 15),
                value="1.2e3"
            ),
            type=NumberLiteralType(
                position=(3, 7),
                value=SciFloatLiteral(
                    position=(3, 7),
                    value="1.2e3"
                )
            )
        ),
        VariableBindingStatement(
            position=(5, 1),
            name=Symbol(
                position=(5, 1),
                name="basicStringType"
            ),
            value=StringLiteral(
                position=(5, 29),
                value="hello"
            ),
            type=StringLiteralType(
                position=(5, 19),
                value=StringLiteral(
                    position=(5, 19),
                    value="hello"
                )
            )
        ),
        VariableBindingStatement(
            position=(6, 1),
            name=Symbol(
                position=(6, 1),
                name="rawStringType"
            ),
            value=RawStringLiteral(
                position=(6, 34),
                value="raw\\nstring"
            ),
            type=StringLiteralType(
                position=(6, 17),
                value=RawStringLiteral(
                    position=(6, 17),
                    value="raw\\nstring"
                )
            )
        ),
        VariableBindingStatement(
            position=(7, 1),
            name=Symbol(
                position=(7, 1),
                name="multiLineStringType"
            ),
            value=MultiLineStringLiteral(
                position=(9, 13),
                value="multi\nline\nstring"
            ),
            type=StringLiteralType(
                position=(7, 23),
                value=MultiLineStringLiteral(
                    position=(7, 23),
                    value="multi\nline\nstring"
                )
            )
        ),
        VariableBindingStatement(
            position=(13, 1),
            name=Symbol(
                position=(13, 1),
                name="rawMultiLineStringType"
            ),
            value=RawMultiLineStringLiteral(
                position=(16, 13),
                value="raw\nmulti\nline\nstring"
            ),
            type=StringLiteralType(
                position=(13, 26),
                value=RawMultiLineStringLiteral(
                    position=(13, 26),
                    value="raw\nmulti\nline\nstring"
                )
            )
        )
    ]
)
*)