(*
Module(
    position=(1, 1),
    top_level_nodes=[
        VariableBindingStatement(
            position=(31, 1),
            name=Symbol(
                position=(31, 1),
                name="var1"
            ),
            value=StringLiteral(
                position=(31, 8),
                value="value"
            )
        ),
        VariableBindingStatement(
            position=(32, 1),
            name=Symbol(
                position=(32, 1),
                name="var2"
            ),
            value=Symbol(
                position=(32, 8),
                name="var1"
            )
        )
    ]
)
*)

var1 = "value"
var2 = var1