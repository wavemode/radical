unaryNot = not 5
unaryMinus = - 10
unaryPlus = + 15

unaryPlusMinus = + - 20
unaryMinusPlus = - + 25
unaryNotMinusPlusPlusMinus = not - + + - 30

(*
Module(
    position=(1, 1),
    top_level_nodes=[
        VariableBindingStatement(
            position=(1, 1),
            name=Symbol(
                position=(1, 1),
                name="unaryNot",
                quoted=false
            ),
            value=UnaryOperation(
                position=(1, 12),
                operator="not",
                operand=IntegerLiteral(
                    position=(1, 16),
                    value="5"
                )
            )
        ),
        VariableBindingStatement(
            position=(2, 1),
            name=Symbol(
                position=(2, 1),
                name="unaryMinus",
                quoted=false
            ),
            value=UnaryOperation(
                position=(2, 14),
                operator="-",
                operand=IntegerLiteral(
                    position=(2, 16),
                    value="10"
                )
            )
        ),
        VariableBindingStatement(
            position=(3, 1),
            name=Symbol(
                position=(3, 1),
                name="unaryPlus",
                quoted=false
            ),
            value=UnaryOperation(
                position=(3, 13),
                operator="+",
                operand=IntegerLiteral(
                    position=(3, 15),
                    value="15"
                )
            )
        ),
        VariableBindingStatement(
            position=(5, 1),
            name=Symbol(
                position=(5, 1),
                name="unaryPlusMinus",
                quoted=false
            ),
            value=UnaryOperation(
                position=(5, 18),
                operator="+",
                operand=UnaryOperation(
                    position=(5, 20),
                    operator="-",
                    operand=IntegerLiteral(
                        position=(5, 22),
                        value="20"
                    )
                )
            )
        ),
        VariableBindingStatement(
            position=(6, 1),
            name=Symbol(
                position=(6, 1),
                name="unaryMinusPlus",
                quoted=false
            ),
            value=UnaryOperation(
                position=(6, 18),
                operator="-",
                operand=UnaryOperation(
                    position=(6, 20),
                    operator="+",
                    operand=IntegerLiteral(
                        position=(6, 22),
                        value="25"
                    )
                )
            )
        ),
        VariableBindingStatement(
            position=(7, 1),
            name=Symbol(
                position=(7, 1),
                name="unaryNotMinusPlusPlusMinus",
                quoted=false
            ),
            value=UnaryOperation(
                position=(7, 30),
                operator="not",
                operand=UnaryOperation(
                    position=(7, 34),
                    operator="-",
                    operand=UnaryOperation(
                        position=(7, 36),
                        operator="+",
                        operand=UnaryOperation(
                            position=(7, 38),
                            operator="+",
                            operand=UnaryOperation(
                                position=(7, 40),
                                operator="-",
                                operand=IntegerLiteral(
                                    position=(7, 42),
                                    value="30"
                                )
                            )
                        )
                    )
                )
            )
        )
    ]
)
*)
