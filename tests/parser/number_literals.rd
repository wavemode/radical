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
    top_level_nodes=[
        VariableBindingStatement(
            name=Symbol(
                name="integerLiteral"
            ),
            value=IntegerLiteral(
                value="42"
            )
        ),
        VariableBindingStatement(
            name=Symbol(
                name="negativeIntegerLiteral"
            ),
            value=UnaryOperation(
                operator="-",
                operand=IntegerLiteral(
                    value="7"
                )
            )
        ),
        VariableBindingStatement(
            name=Symbol(
                name="floatLiteral"
            ),
            value=FloatLiteral(
                value="3.1415"
            )
        ),
        VariableBindingStatement(
            name=Symbol(
                name="negativeFloatLiteral"
            ),
            value=UnaryOperation(
                operator="-",
                operand=FloatLiteral(
                    value="0.001"
                )
            )
        ),
        VariableBindingStatement(
            name=Symbol(
                name="sciFloatLiteralNoFraction"
            ),
            value=SciFloatLiteral(
                value="1e10"
            )
        ),
        VariableBindingStatement(
            name=Symbol(
                name="negativeSciFloatLiteralNoFraction"
            ),
            value=UnaryOperation(
                operator="-",
                operand=SciFloatLiteral(
                    value="2.5E8"
                )
            )
        ),
        VariableBindingStatement(
            name=Symbol(
                name="negativeSciFloatLiteralNoFractionNegativeExponent"
            ),
            value=UnaryOperation(
                operator="-",
                operand=SciFloatLiteral(
                    value="4e-3"
                )
            )
        ),
        VariableBindingStatement(
            name=Symbol(
                name="sciFloatLiteralWithFraction"
            ),
            value=SciFloatLiteral(
                value="6.022e23"
            )
        ),
        VariableBindingStatement(
            name=Symbol(
                name="negativeSciFloatLiteralWithFraction"
            ),
            value=UnaryOperation(
                operator="-",
                operand=SciFloatLiteral(
                    value="9.81E4"
                )
            )
        ),
        VariableBindingStatement(
            name=Symbol(
                name="negativeSciFloatLiteralWithFractionNegativeExponent"
            ),
            value=UnaryOperation(
                operator="-",
                operand=SciFloatLiteral(
                    value="3.0e-5"
                )
            )
        )
    ]
)
*)
