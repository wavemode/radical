integerLiteral = 42
negativeIntegerLiteral = -7

floatLiteral = 3.1415
negativeFloatLiteral = -0.001

sciFloatLiteralNoFraction = 1e10
negativeSciFloatLiteralNoFraction = -2.5E8
negativeSciFloatLiteralNoFractionNegativeExponent = -4e-3
sciFloatLiteralWithFraction = 6.022e23
negativeSciFloatLiteralWithFraction = -9.81E4
negativeSciFloatLiteralWithFractionNegativeExponent = -3.0e-5

(*
Module(
    position=(1, 1),
    top_level_nodes=[
        VariableBindingStatement(
            position=(1, 1),
            name=Symbol(
                position=(1, 1),
                name="integerLiteral"
            ),
            value=IntegerLiteral(
                position=(1, 18),
                value="42"
            )
        ),
        VariableBindingStatement(
            position=(2, 1),
            name=Symbol(
                position=(2, 1),
                name="negativeIntegerLiteral"
            ),
            value=UnaryOperation(
                position=(2, 26),
                operator="-",
                operand=IntegerLiteral(
                    position=(2, 27),
                    value="7"
                )
            )
        ),
        VariableBindingStatement(
            position=(4, 1),
            name=Symbol(
                position=(4, 1),
                name="floatLiteral"
            ),
            value=FloatLiteral(
                position=(4, 16),
                value="3.1415"
            )
        ),
        VariableBindingStatement(
            position=(5, 1),
            name=Symbol(
                position=(5, 1),
                name="negativeFloatLiteral"
            ),
            value=UnaryOperation(
                position=(5, 24),
                operator="-",
                operand=FloatLiteral(
                    position=(5, 25),
                    value="0.001"
                )
            )
        ),
        VariableBindingStatement(
            position=(7, 1),
            name=Symbol(
                position=(7, 1),
                name="sciFloatLiteralNoFraction"
            ),
            value=SciFloatLiteral(
                position=(7, 29),
                value="1e10"
            )
        ),
        VariableBindingStatement(
            position=(8, 1),
            name=Symbol(
                position=(8, 1),
                name="negativeSciFloatLiteralNoFraction"
            ),
            value=UnaryOperation(
                position=(8, 37),
                operator="-",
                operand=SciFloatLiteral(
                    position=(8, 38),
                    value="2.5E8"
                )
            )
        ),
        VariableBindingStatement(
            position=(9, 1),
            name=Symbol(
                position=(9, 1),
                name="negativeSciFloatLiteralNoFractionNegativeExponent"
            ),
            value=UnaryOperation(
                position=(9, 53),
                operator="-",
                operand=SciFloatLiteral(
                    position=(9, 54),
                    value="4e-3"
                )
            )
        ),
        VariableBindingStatement(
            position=(10, 1),
            name=Symbol(
                position=(10, 1),
                name="sciFloatLiteralWithFraction"
            ),
            value=SciFloatLiteral(
                position=(10, 31),
                value="6.022e23"
            )
        ),
        VariableBindingStatement(
            position=(11, 1),
            name=Symbol(
                position=(11, 1),
                name="negativeSciFloatLiteralWithFraction"
            ),
            value=UnaryOperation(
                position=(11, 39),
                operator="-",
                operand=SciFloatLiteral(
                    position=(11, 40),
                    value="9.81E4"
                )
            )
        ),
        VariableBindingStatement(
            position=(12, 1),
            name=Symbol(
                position=(12, 1),
                name="negativeSciFloatLiteralWithFractionNegativeExponent"
            ),
            value=UnaryOperation(
                position=(12, 55),
                operator="-",
                operand=SciFloatLiteral(
                    position=(12, 56),
                    value="3.0e-5"
                )
            )
        )
    ]
)
*)
