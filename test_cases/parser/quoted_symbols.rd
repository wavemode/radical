`my quoted var` = 10

`my
varname
can
contain
anything` = 20

`var name with a backtick `` inside` = 30

(*
Module(
    position=(1, 1),
    top_level_nodes=[
        VariableBindingStatement(
            position=(1, 1),
            name=Symbol(
                position=(1, 1),
                name="my quoted var",
                quoted=true
            ),
            value=IntegerLiteral(
                position=(1, 19),
                value="10"
            )
        ),
        VariableBindingStatement(
            position=(3, 1),
            name=Symbol(
                position=(3, 1),
                name="my\nvarname\ncan\ncontain\nanything",
                quoted=true
            ),
            value=IntegerLiteral(
                position=(7, 13),
                value="20"
            )
        ),
        VariableBindingStatement(
            position=(9, 1),
            name=Symbol(
                position=(9, 1),
                name="var name with a backtick ` inside",
                quoted=true
            ),
            value=IntegerLiteral(
                position=(9, 40),
                value="30"
            )
        )
    ]
)
*)
