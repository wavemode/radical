binaryAnd = true and false
binaryAndOr = true and false or true
binaryOrAnd = false or true and false

plusMinus = 1 + 2 - 3
minusPlus = 4 - 5 + 6
mixedArithmetic = 7 + 8 - 9 * 10 / 11 + 12 // 13 % 14 ** 15 ** 16

allOperators =
    1 * 2 + 3 - 4 / 5 == 6 != 7 < 8 <= 9 > 10 and 
    11 or 12 |> 13 |> 15 // 16 % 17 ** 18  ** 19 >= 20 or
    not not
    not notand and
    not - 22 - -23 +-+-+-24

(*
allOperators =
    ((((((((((((1 * 2) + 3) - (4 / 5)) == 6) != 7) < 8) <= 9) > 10) and 
    11) or 12) |> 13) |> ((((15 // 16) % (17 ** (18  ** 19))) >= 20) or
    ((not (not
    (not notand))) and
    (not (((- 22) - (-23)) +(-(+(-(+(-24))))))))))
*)

(*
Module(
    position=(1, 1),
    top_level_nodes=[
        VariableBindingStatement(
            position=(1, 1),
            name=Symbol(
                position=(1, 1),
                name="binaryAnd"
            ),
            value=BinaryOperation(
                position=(1, 13),
                left=TrueKeyword(
                    position=(1, 13)
                ),
                operator="and",
                right=FalseKeyword(
                    position=(1, 22)
                )
            )
        ),
        VariableBindingStatement(
            position=(2, 1),
            name=Symbol(
                position=(2, 1),
                name="binaryAndOr"
            ),
            value=BinaryOperation(
                position=(2, 15),
                left=BinaryOperation(
                    position=(2, 15),
                    left=TrueKeyword(
                        position=(2, 15)
                    ),
                    operator="and",
                    right=FalseKeyword(
                        position=(2, 24)
                    )
                ),
                operator="or",
                right=TrueKeyword(
                    position=(2, 33)
                )
            )
        ),
        VariableBindingStatement(
            position=(3, 1),
            name=Symbol(
                position=(3, 1),
                name="binaryOrAnd"
            ),
            value=BinaryOperation(
                position=(3, 15),
                left=FalseKeyword(
                    position=(3, 15)
                ),
                operator="or",
                right=BinaryOperation(
                    position=(3, 24),
                    left=TrueKeyword(
                        position=(3, 24)
                    ),
                    operator="and",
                    right=FalseKeyword(
                        position=(3, 33)
                    )
                )
            )
        ),
        VariableBindingStatement(
            position=(5, 1),
            name=Symbol(
                position=(5, 1),
                name="plusMinus"
            ),
            value=BinaryOperation(
                position=(5, 13),
                left=BinaryOperation(
                    position=(5, 13),
                    left=IntegerLiteral(
                        position=(5, 13),
                        value="1"
                    ),
                    operator="+",
                    right=IntegerLiteral(
                        position=(5, 17),
                        value="2"
                    )
                ),
                operator="-",
                right=IntegerLiteral(
                    position=(5, 21),
                    value="3"
                )
            )
        ),
        VariableBindingStatement(
            position=(6, 1),
            name=Symbol(
                position=(6, 1),
                name="minusPlus"
            ),
            value=BinaryOperation(
                position=(6, 13),
                left=BinaryOperation(
                    position=(6, 13),
                    left=IntegerLiteral(
                        position=(6, 13),
                        value="4"
                    ),
                    operator="-",
                    right=IntegerLiteral(
                        position=(6, 17),
                        value="5"
                    )
                ),
                operator="+",
                right=IntegerLiteral(
                    position=(6, 21),
                    value="6"
                )
            )
        ),
        VariableBindingStatement(
            position=(7, 1),
            name=Symbol(
                position=(7, 1),
                name="mixedArithmetic"
            ),
            value=BinaryOperation(
                position=(7, 19),
                left=BinaryOperation(
                    position=(7, 19),
                    left=BinaryOperation(
                        position=(7, 19),
                        left=IntegerLiteral(
                            position=(7, 19),
                            value="7"
                        ),
                        operator="+",
                        right=IntegerLiteral(
                            position=(7, 23),
                            value="8"
                        )
                    ),
                    operator="-",
                    right=BinaryOperation(
                        position=(7, 27),
                        left=BinaryOperation(
                            position=(7, 27),
                            left=IntegerLiteral(
                                position=(7, 27),
                                value="9"
                            ),
                            operator="*",
                            right=IntegerLiteral(
                                position=(7, 31),
                                value="10"
                            )
                        ),
                        operator="/",
                        right=IntegerLiteral(
                            position=(7, 36),
                            value="11"
                        )
                    )
                ),
                operator="+",
                right=BinaryOperation(
                    position=(7, 41),
                    left=BinaryOperation(
                        position=(7, 41),
                        left=IntegerLiteral(
                            position=(7, 41),
                            value="12"
                        ),
                        operator="//",
                        right=IntegerLiteral(
                            position=(7, 47),
                            value="13"
                        )
                    ),
                    operator="%",
                    right=BinaryOperation(
                        position=(7, 52),
                        left=IntegerLiteral(
                            position=(7, 52),
                            value="14"
                        ),
                        operator="**",
                        right=BinaryOperation(
                            position=(7, 58),
                            left=IntegerLiteral(
                                position=(7, 58),
                                value="15"
                            ),
                            operator="**",
                            right=IntegerLiteral(
                                position=(7, 64),
                                value="16"
                            )
                        )
                    )
                )
            )
        ),
        VariableBindingStatement(
            position=(9, 1),
            name=Symbol(
                position=(9, 1),
                name="allOperators"
            ),
            value=BinaryOperation(
                position=(10, 5),
                left=BinaryOperation(
                    position=(10, 5),
                    left=BinaryOperation(
                        position=(10, 5),
                        left=BinaryOperation(
                            position=(10, 5),
                            left=BinaryOperation(
                                position=(10, 5),
                                left=BinaryOperation(
                                    position=(10, 5),
                                    left=BinaryOperation(
                                        position=(10, 5),
                                        left=BinaryOperation(
                                            position=(10, 5),
                                            left=BinaryOperation(
                                                position=(10, 5),
                                                left=BinaryOperation(
                                                    position=(10, 5),
                                                    left=BinaryOperation(
                                                        position=(10, 5),
                                                        left=BinaryOperation(
                                                            position=(10, 5),
                                                            left=IntegerLiteral(
                                                                position=(10, 5),
                                                                value="1"
                                                            ),
                                                            operator="*",
                                                            right=IntegerLiteral(
                                                                position=(10, 9),
                                                                value="2"
                                                            )
                                                        ),
                                                        operator="+",
                                                        right=IntegerLiteral(
                                                            position=(10, 13),
                                                            value="3"
                                                        )
                                                    ),
                                                    operator="-",
                                                    right=BinaryOperation(
                                                        position=(10, 17),
                                                        left=IntegerLiteral(
                                                            position=(10, 17),
                                                            value="4"
                                                        ),
                                                        operator="/",
                                                        right=IntegerLiteral(
                                                            position=(10, 21),
                                                            value="5"
                                                        )
                                                    )
                                                ),
                                                operator="==",
                                                right=IntegerLiteral(
                                                    position=(10, 26),
                                                    value="6"
                                                )
                                            ),
                                            operator="!=",
                                            right=IntegerLiteral(
                                                position=(10, 31),
                                                value="7"
                                            )
                                        ),
                                        operator="<",
                                        right=IntegerLiteral(
                                            position=(10, 35),
                                            value="8"
                                        )
                                    ),
                                    operator="<=",
                                    right=IntegerLiteral(
                                        position=(10, 40),
                                        value="9"
                                    )
                                ),
                                operator=">",
                                right=IntegerLiteral(
                                    position=(10, 44),
                                    value="10"
                                )
                            ),
                            operator="and",
                            right=IntegerLiteral(
                                position=(11, 5),
                                value="11"
                            )
                        ),
                        operator="or",
                        right=IntegerLiteral(
                            position=(11, 11),
                            value="12"
                        )
                    ),
                    operator="|>",
                    right=IntegerLiteral(
                        position=(11, 17),
                        value="13"
                    )
                ),
                operator="|>",
                right=BinaryOperation(
                    position=(11, 23),
                    left=BinaryOperation(
                        position=(11, 23),
                        left=BinaryOperation(
                            position=(11, 23),
                            left=BinaryOperation(
                                position=(11, 23),
                                left=IntegerLiteral(
                                    position=(11, 23),
                                    value="15"
                                ),
                                operator="//",
                                right=IntegerLiteral(
                                    position=(11, 29),
                                    value="16"
                                )
                            ),
                            operator="%",
                            right=BinaryOperation(
                                position=(11, 34),
                                left=IntegerLiteral(
                                    position=(11, 34),
                                    value="17"
                                ),
                                operator="**",
                                right=BinaryOperation(
                                    position=(11, 40),
                                    left=IntegerLiteral(
                                        position=(11, 40),
                                        value="18"
                                    ),
                                    operator="**",
                                    right=IntegerLiteral(
                                        position=(11, 47),
                                        value="19"
                                    )
                                )
                            )
                        ),
                        operator=">=",
                        right=IntegerLiteral(
                            position=(11, 53),
                            value="20"
                        )
                    ),
                    operator="or",
                    right=BinaryOperation(
                        position=(12, 5),
                        left=UnaryOperation(
                            position=(12, 5),
                            operator="not",
                            operand=UnaryOperation(
                                position=(12, 9),
                                operator="not",
                                operand=UnaryOperation(
                                    position=(13, 5),
                                    operator="not",
                                    operand=Symbol(
                                        position=(13, 9),
                                        name="notand"
                                    )
                                )
                            )
                        ),
                        operator="and",
                        right=UnaryOperation(
                            position=(14, 5),
                            operator="not",
                            operand=BinaryOperation(
                                position=(14, 9),
                                left=BinaryOperation(
                                    position=(14, 9),
                                    left=UnaryOperation(
                                        position=(14, 9),
                                        operator="-",
                                        operand=IntegerLiteral(
                                            position=(14, 11),
                                            value="22"
                                        )
                                    ),
                                    operator="-",
                                    right=UnaryOperation(
                                        position=(14, 16),
                                        operator="-",
                                        operand=IntegerLiteral(
                                            position=(14, 17),
                                            value="23"
                                        )
                                    )
                                ),
                                operator="+",
                                right=UnaryOperation(
                                    position=(14, 21),
                                    operator="-",
                                    operand=UnaryOperation(
                                        position=(14, 22),
                                        operator="+",
                                        operand=UnaryOperation(
                                            position=(14, 23),
                                            operator="-",
                                            operand=UnaryOperation(
                                                position=(14, 24),
                                                operator="+",
                                                operand=UnaryOperation(
                                                    position=(14, 25),
                                                    operator="-",
                                                    operand=IntegerLiteral(
                                                        position=(14, 26),
                                                        value="24"
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
        ),
        VariableBindingStatement(
            position=(501, 1),
            name=Symbol(
                position=(501, 1),
                name="plusMinusPlus"
            ),
            value=BinaryOperation(
                position=(501, 17),
                left=BinaryOperation(
                    position=(501, 17),
                    left=BinaryOperation(
                        position=(501, 17),
                        left=IntegerLiteral(
                            position=(501, 17),
                            value="1"
                        ),
                        operator="+",
                        right=IntegerLiteral(
                            position=(501, 21),
                            value="2"
                        )
                    ),
                    operator="-",
                    right=IntegerLiteral(
                        position=(501, 25),
                        value="3"
                    )
                ),
                operator="+",
                right=IntegerLiteral(
                    position=(501, 29),
                    value="4"
                )
            )
        )
    ]
)
*)

plusMinusPlus = 1 + 2 - 3 + 4