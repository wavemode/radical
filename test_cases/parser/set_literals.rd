simpleSet = { value1, "value1", value2, 42, value3, false }
setWithoutCommas =
    {
        a
        1
        b
        2
        c
        3
    }
nestedSet = {
    {
        innerKey1 = "innerValue1",
        innerKey2 = 3.14
    }
    [1, 2, 3]
}
setWithExpressions = {
    10 + 20,
    ["concat" + "Value"],
    "Hello, " + "world!",
}
setComprehension = { v * 2 for k, v in someMap if v > 10 }
nestedComprehension = { { subK = subV for subK, subV in v } for k, v in anotherMap }

(*
Module(
    position=(1, 1),
    top_level_nodes=[
        VariableBindingStatement(
            position=(1, 1),
            name=Symbol(
                position=(1, 1),
                name="simpleSet",
                quoted=false
            ),
            value=SetLiteral(
                position=(1, 13),
                elements=[
                    Symbol(
                        position=(1, 15),
                        name="value1",
                        quoted=false
                    ),
                    StringLiteral(
                        position=(1, 23),
                        value="value1"
                    ),
                    Symbol(
                        position=(1, 33),
                        name="value2",
                        quoted=false
                    ),
                    IntegerLiteral(
                        position=(1, 41),
                        value="42"
                    ),
                    Symbol(
                        position=(1, 45),
                        name="value3",
                        quoted=false
                    ),
                    FalseKeyword(
                        position=(1, 53)
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(2, 1),
            name=Symbol(
                position=(2, 1),
                name="setWithoutCommas",
                quoted=false
            ),
            value=SetLiteral(
                position=(3, 5),
                elements=[
                    Symbol(
                        position=(4, 9),
                        name="a",
                        quoted=false
                    ),
                    IntegerLiteral(
                        position=(5, 9),
                        value="1"
                    ),
                    Symbol(
                        position=(6, 9),
                        name="b",
                        quoted=false
                    ),
                    IntegerLiteral(
                        position=(7, 9),
                        value="2"
                    ),
                    Symbol(
                        position=(8, 9),
                        name="c",
                        quoted=false
                    ),
                    IntegerLiteral(
                        position=(9, 9),
                        value="3"
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(11, 1),
            name=Symbol(
                position=(11, 1),
                name="nestedSet",
                quoted=false
            ),
            value=SetLiteral(
                position=(11, 13),
                elements=[
                    MapLiteral(
                        position=(12, 5),
                        entries=[
                            MapEntry(
                                position=(13, 9),
                                key=Symbol(
                                    position=(13, 9),
                                    name="innerKey1",
                                    quoted=false
                                ),
                                value=StringLiteral(
                                    position=(13, 21),
                                    value="innerValue1"
                                ),
                                expression_key=false
                            ),
                            MapEntry(
                                position=(14, 9),
                                key=Symbol(
                                    position=(14, 9),
                                    name="innerKey2",
                                    quoted=false
                                ),
                                value=FloatLiteral(
                                    position=(14, 21),
                                    value="3.14"
                                ),
                                expression_key=false
                            )
                        ]
                    ),
                    ListLiteral(
                        position=(16, 5),
                        elements=[
                            IntegerLiteral(
                                position=(16, 6),
                                value="1"
                            ),
                            IntegerLiteral(
                                position=(16, 9),
                                value="2"
                            ),
                            IntegerLiteral(
                                position=(16, 12),
                                value="3"
                            )
                        ]
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(18, 1),
            name=Symbol(
                position=(18, 1),
                name="setWithExpressions",
                quoted=false
            ),
            value=SetLiteral(
                position=(18, 22),
                elements=[
                    BinaryOperation(
                        position=(19, 5),
                        left=IntegerLiteral(
                            position=(19, 5),
                            value="10"
                        ),
                        operator="+",
                        right=IntegerLiteral(
                            position=(19, 10),
                            value="20"
                        )
                    ),
                    ListLiteral(
                        position=(20, 5),
                        elements=[
                            BinaryOperation(
                                position=(20, 6),
                                left=StringLiteral(
                                    position=(20, 6),
                                    value="concat"
                                ),
                                operator="+",
                                right=StringLiteral(
                                    position=(20, 17),
                                    value="Value"
                                )
                            )
                        ]
                    ),
                    BinaryOperation(
                        position=(21, 5),
                        left=StringLiteral(
                            position=(21, 5),
                            value="Hello, "
                        ),
                        operator="+",
                        right=StringLiteral(
                            position=(21, 17),
                            value="world!"
                        )
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(23, 1),
            name=Symbol(
                position=(23, 1),
                name="setComprehension",
                quoted=false
            ),
            value=SetComprehension(
                position=(23, 20),
                element=BinaryOperation(
                    position=(23, 22),
                    left=Symbol(
                        position=(23, 22),
                        name="v",
                        quoted=false
                    ),
                    operator="*",
                    right=IntegerLiteral(
                        position=(23, 26),
                        value="2"
                    )
                ),
                clauses=[
                    ComprehensionBinding(
                        position=(23, 28),
                        variables=[
                            Symbol(
                                position=(23, 32),
                                name="k",
                                quoted=false
                            ),
                            Symbol(
                                position=(23, 35),
                                name="v",
                                quoted=false
                            )
                        ],
                        iterable=Symbol(
                            position=(23, 40),
                            name="someMap",
                            quoted=false
                        )
                    ),
                    ComprehensionGuard(
                        position=(23, 48),
                        condition=BinaryOperation(
                            position=(23, 51),
                            left=Symbol(
                                position=(23, 51),
                                name="v",
                                quoted=false
                            ),
                            operator=">",
                            right=IntegerLiteral(
                                position=(23, 55),
                                value="10"
                            )
                        )
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(24, 1),
            name=Symbol(
                position=(24, 1),
                name="nestedComprehension",
                quoted=false
            ),
            value=SetComprehension(
                position=(24, 23),
                element=MapComprehension(
                    position=(24, 25),
                    entry=MapEntry(
                        position=(24, 27),
                        key=Symbol(
                            position=(24, 27),
                            name="subK",
                            quoted=false
                        ),
                        value=Symbol(
                            position=(24, 34),
                            name="subV",
                            quoted=false
                        ),
                        expression_key=false
                    ),
                    clauses=[
                        ComprehensionBinding(
                            position=(24, 39),
                            variables=[
                                Symbol(
                                    position=(24, 43),
                                    name="subK",
                                    quoted=false
                                ),
                                Symbol(
                                    position=(24, 49),
                                    name="subV",
                                    quoted=false
                                )
                            ],
                            iterable=Symbol(
                                position=(24, 57),
                                name="v",
                                quoted=false
                            )
                        )
                    ]
                ),
                clauses=[
                    ComprehensionBinding(
                        position=(24, 61),
                        variables=[
                            Symbol(
                                position=(24, 65),
                                name="k",
                                quoted=false
                            ),
                            Symbol(
                                position=(24, 68),
                                name="v",
                                quoted=false
                            )
                        ],
                        iterable=Symbol(
                            position=(24, 73),
                            name="anotherMap",
                            quoted=false
                        )
                    )
                ]
            )
        )
    ]
)
*)
