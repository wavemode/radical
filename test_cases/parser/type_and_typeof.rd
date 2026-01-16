myValue = 5

otherValue : typeof myValue = 10

option1 = "A"
option2 = "B"
option3 = "C"

enumValue :
    type option1
    | type option2
    | type option3
    = "C"

(*
Module(
    position=(1, 1),
    top_level_nodes=[
        VariableBindingStatement(
            position=(1, 1),
            name=Symbol(
                position=(1, 1),
                name="myValue"
            ),
            value=IntegerLiteral(
                position=(1, 11),
                value="5"
            )
        ),
        VariableBindingStatement(
            position=(3, 1),
            name=Symbol(
                position=(3, 1),
                name="otherValue"
            ),
            value=IntegerLiteral(
                position=(3, 31),
                value="10"
            ),
            type=TypeOfExpression(
                position=(3, 14),
                value=Symbol(
                    position=(3, 21),
                    name="myValue"
                )
            )
        ),
        VariableBindingStatement(
            position=(5, 1),
            name=Symbol(
                position=(5, 1),
                name="option1"
            ),
            value=StringLiteral(
                position=(5, 11),
                value="A"
            )
        ),
        VariableBindingStatement(
            position=(6, 1),
            name=Symbol(
                position=(6, 1),
                name="option2"
            ),
            value=StringLiteral(
                position=(6, 11),
                value="B"
            )
        ),
        VariableBindingStatement(
            position=(7, 1),
            name=Symbol(
                position=(7, 1),
                name="option3"
            ),
            value=StringLiteral(
                position=(7, 11),
                value="C"
            )
        ),
        VariableBindingStatement(
            position=(9, 1),
            name=Symbol(
                position=(9, 1),
                name="enumValue"
            ),
            value=StringLiteral(
                position=(13, 7),
                value="C"
            ),
            type=UnionType(
                position=(12, 5),
                left=UnionType(
                    position=(11, 5),
                    left=TypeExpression(
                        position=(10, 5),
                        value=Symbol(
                            position=(10, 10),
                            name="option1"
                        )
                    ),
                    right=TypeExpression(
                        position=(11, 7),
                        value=Symbol(
                            position=(11, 12),
                            name="option2"
                        )
                    )
                ),
                right=TypeExpression(
                    position=(12, 7),
                    value=Symbol(
                        position=(12, 12),
                        name="option3"
                    )
                )
            )
        )
    ]
)
*)
