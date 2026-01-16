myVar = 1 + (2 * (3 + 4))

(*
Module(
    position=(1, 1),
    top_level_nodes=[
        VariableBindingStatement(
            position=(1, 1),
            name=Symbol(
                position=(1, 1),
                name="myVar"
            ),
            value=BinaryOperation(
                position=(1, 9),
                left=IntegerLiteral(
                    position=(1, 10),
                    value="1"
                ),
                operator="+",
                right=ParenthesizedExpression(
                    position=(1, 13),
                    expression=BinaryOperation(
                        position=(1, 14),
                        left=IntegerLiteral(
                            position=(1, 15),
                            value="2"
                        ),
                        operator="*",
                        right=ParenthesizedExpression(
                            position=(1, 18),
                            expression=BinaryOperation(
                                position=(1, 19),
                                left=IntegerLiteral(
                                    position=(1, 20),
                                    value="3"
                                ),
                                operator="+",
                                right=IntegerLiteral(
                                    position=(1, 24),
                                    value="4"
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
