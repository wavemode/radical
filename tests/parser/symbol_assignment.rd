(*
Module(
    top_level_nodes=[
        VariableBindingStatement(
            name=Symbol(
                name="var1"
            ),
            value=StringLiteral(
                value="value"
            )
        ),
        VariableBindingStatement(
            name=Symbol(
                name="var2"
            ),
            value=Symbol(
                name="var1"
            )
        )
    ]
)
*)

var1 = "value"
var2 = var1