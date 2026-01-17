(*
Module(
    position=(1, 1),
    top_level_nodes=[
        VariableBindingStatement(
            position=(34, 1),
            name=Symbol(
                position=(34, 1),
                name="var1",
                quoted=false
            ),
            value=StringLiteral(
                position=(34, 8),
                value="value"
            )
        ),
        VariableBindingStatement(
            position=(35, 1),
            name=Symbol(
                position=(35, 1),
                name="var2",
                quoted=false
            ),
            value=Symbol(
                position=(35, 8),
                name="var1",
                quoted=false
            )
        )
    ]
)
*)

var1 = "value"
var2 = var1