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
                left=Symbol(
                    position=(1, 13),
                    name="true"
                ),
                operator="and",
                right=Symbol(
                    position=(1, 22),
                    name="false"
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
                    left=Symbol(
                        position=(2, 15),
                        name="true"
                    ),
                    operator="and",
                    right=Symbol(
                        position=(2, 24),
                        name="false"
                    )
                ),
                operator="or",
                right=Symbol(
                    position=(2, 33),
                    name="true"
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
                left=Symbol(
                    position=(3, 15),
                    name="false"
                ),
                operator="or",
                right=BinaryOperation(
                    position=(3, 24),
                    left=Symbol(
                        position=(3, 24),
                        name="true"
                    ),
                    operator="and",
                    right=Symbol(
                        position=(3, 33),
                        name="false"
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
                        position=(5, 14),
                        value="1"
                    ),
                    operator="+",
                    right=IntegerLiteral(
                        position=(5, 18),
                        value="2"
                    )
                ),
                operator="-",
                right=IntegerLiteral(
                    position=(5, 22),
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
                        position=(6, 14),
                        value="4"
                    ),
                    operator="-",
                    right=IntegerLiteral(
                        position=(6, 18),
                        value="5"
                    )
                ),
                operator="+",
                right=IntegerLiteral(
                    position=(6, 22),
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
                            position=(7, 20),
                            value="7"
                        ),
                        operator="+",
                        right=IntegerLiteral(
                            position=(7, 24),
                            value="8"
                        )
                    ),
                    operator="-",
                    right=BinaryOperation(
                        position=(7, 27),
                        left=BinaryOperation(
                            position=(7, 27),
                            left=IntegerLiteral(
                                position=(7, 28),
                                value="9"
                            ),
                            operator="*",
                            right=IntegerLiteral(
                                position=(7, 33),
                                value="10"
                            )
                        ),
                        operator="/",
                        right=IntegerLiteral(
                            position=(7, 38),
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
                            position=(7, 43),
                            value="12"
                        ),
                        operator="//",
                        right=IntegerLiteral(
                            position=(7, 49),
                            value="13"
                        )
                    ),
                    operator="%",
                    right=BinaryOperation(
                        position=(7, 52),
                        left=IntegerLiteral(
                            position=(7, 54),
                            value="14"
                        ),
                        operator="**",
                        right=BinaryOperation(
                            position=(7, 58),
                            left=IntegerLiteral(
                                position=(7, 60),
                                value="15"
                            ),
                            operator="**",
                            right=IntegerLiteral(
                                position=(7, 66),
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
                                                                position=(10, 6),
                                                                value="1"
                                                            ),
                                                            operator="*",
                                                            right=IntegerLiteral(
                                                                position=(10, 10),
                                                                value="2"
                                                            )
                                                        ),
                                                        operator="+",
                                                        right=IntegerLiteral(
                                                            position=(10, 14),
                                                            value="3"
                                                        )
                                                    ),
                                                    operator="-",
                                                    right=BinaryOperation(
                                                        position=(10, 17),
                                                        left=IntegerLiteral(
                                                            position=(10, 18),
                                                            value="4"
                                                        ),
                                                        operator="/",
                                                        right=IntegerLiteral(
                                                            position=(10, 22),
                                                            value="5"
                                                        )
                                                    )
                                                ),
                                                operator="==",
                                                right=IntegerLiteral(
                                                    position=(10, 27),
                                                    value="6"
                                                )
                                            ),
                                            operator="!=",
                                            right=IntegerLiteral(
                                                position=(10, 32),
                                                value="7"
                                            )
                                        ),
                                        operator="<",
                                        right=IntegerLiteral(
                                            position=(10, 36),
                                            value="8"
                                        )
                                    ),
                                    operator="<=",
                                    right=IntegerLiteral(
                                        position=(10, 41),
                                        value="9"
                                    )
                                ),
                                operator=">",
                                right=IntegerLiteral(
                                    position=(10, 46),
                                    value="10"
                                )
                            ),
                            operator="and",
                            right=IntegerLiteral(
                                position=(11, 7),
                                value="11"
                            )
                        ),
                        operator="or",
                        right=IntegerLiteral(
                            position=(11, 13),
                            value="12"
                        )
                    ),
                    operator="|>",
                    right=IntegerLiteral(
                        position=(11, 19),
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
                                    position=(11, 25),
                                    value="15"
                                ),
                                operator="//",
                                right=IntegerLiteral(
                                    position=(11, 31),
                                    value="16"
                                )
                            ),
                            operator="%",
                            right=BinaryOperation(
                                position=(11, 34),
                                left=IntegerLiteral(
                                    position=(11, 36),
                                    value="17"
                                ),
                                operator="**",
                                right=BinaryOperation(
                                    position=(11, 40),
                                    left=IntegerLiteral(
                                        position=(11, 42),
                                        value="18"
                                    ),
                                    operator="**",
                                    right=IntegerLiteral(
                                        position=(11, 49),
                                        value="19"
                                    )
                                )
                            )
                        ),
                        operator=">=",
                        right=IntegerLiteral(
                            position=(11, 55),
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
                                            position=(14, 13),
                                            value="22"
                                        )
                                    ),
                                    operator="-",
                                    right=UnaryOperation(
                                        position=(14, 16),
                                        operator="-",
                                        operand=IntegerLiteral(
                                            position=(14, 19),
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
                                                        position=(14, 28),
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
            position=(509, 1),
            name=Symbol(
                position=(509, 1),
                name="plusMinusPlus"
            ),
            value=BinaryOperation(
                position=(509, 17),
                left=BinaryOperation(
                    position=(509, 17),
                    left=BinaryOperation(
                        position=(509, 17),
                        left=IntegerLiteral(
                            position=(509, 18),
                            value="1"
                        ),
                        operator="+",
                        right=IntegerLiteral(
                            position=(509, 22),
                            value="2"
                        )
                    ),
                    operator="-",
                    right=IntegerLiteral(
                        position=(509, 26),
                        value="3"
                    )
                ),
                operator="+",
                right=IntegerLiteral(
                    position=(510, 1),
                    value="4"
                )
            )
        )
    ]
)
*)

plusMinusPlus = 1 + 2 - 3 + 4