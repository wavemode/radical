emptyMap = {  }
simpleMap = { key1 = "value1"
    , key2 = 42
    , key3 = false }
mapWithoutCommas =
    {
        a = 1
        b = 2
        c = 3
    }
nestedMap = {
    outerKey1 = {
        innerKey1 = "innerValue1",
        innerKey2 = 3.14
    },
    outerKey2 = [1, 2, 3]
}
mapWithExpressions = {
    sumKey = 10 + 20
    ["concat" + "Key"] = "Hello, " + "world!"
}
mapComprehension = { k = v * 2 for k, v in someMap if v > 10 }
nestedComprehension = { k = { subK = subV for subK, subV in v } for k, v in anotherMap }

(*
Module(
    position=(1, 1),
    top_level_nodes=[
        VariableBindingStatement(
            position=(1, 1),
            name=Symbol(
                position=(1, 1),
                name="emptyMap"
            ),
            value=MapLiteral(
                position=(1, 12),
                entries=[

                ]
            )
        ),
        VariableBindingStatement(
            position=(2, 1),
            name=Symbol(
                position=(2, 1),
                name="simpleMap"
            ),
            value=MapLiteral(
                position=(2, 13),
                entries=[
                    MapEntry(
                        position=(2, 15),
                        key=Symbol(
                            position=(2, 15),
                            name="key1"
                        ),
                        value=StringLiteral(
                            position=(2, 22),
                            value="value1"
                        ),
                        expression_key=false
                    ),
                    MapEntry(
                        position=(3, 7),
                        key=Symbol(
                            position=(3, 7),
                            name="key2"
                        ),
                        value=IntegerLiteral(
                            position=(3, 16),
                            value="42"
                        ),
                        expression_key=false
                    ),
                    MapEntry(
                        position=(4, 7),
                        key=Symbol(
                            position=(4, 7),
                            name="key3"
                        ),
                        value=Symbol(
                            position=(4, 14),
                            name="false"
                        ),
                        expression_key=false
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(5, 1),
            name=Symbol(
                position=(5, 1),
                name="mapWithoutCommas"
            ),
            value=MapLiteral(
                position=(6, 5),
                entries=[
                    MapEntry(
                        position=(7, 9),
                        key=Symbol(
                            position=(7, 9),
                            name="a"
                        ),
                        value=IntegerLiteral(
                            position=(7, 14),
                            value="1"
                        ),
                        expression_key=false
                    ),
                    MapEntry(
                        position=(8, 9),
                        key=Symbol(
                            position=(8, 9),
                            name="b"
                        ),
                        value=IntegerLiteral(
                            position=(8, 14),
                            value="2"
                        ),
                        expression_key=false
                    ),
                    MapEntry(
                        position=(9, 9),
                        key=Symbol(
                            position=(9, 9),
                            name="c"
                        ),
                        value=IntegerLiteral(
                            position=(9, 14),
                            value="3"
                        ),
                        expression_key=false
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(11, 1),
            name=Symbol(
                position=(11, 1),
                name="nestedMap"
            ),
            value=MapLiteral(
                position=(11, 13),
                entries=[
                    MapEntry(
                        position=(12, 5),
                        key=Symbol(
                            position=(12, 5),
                            name="outerKey1"
                        ),
                        value=MapLiteral(
                            position=(12, 17),
                            entries=[
                                MapEntry(
                                    position=(13, 9),
                                    key=Symbol(
                                        position=(13, 9),
                                        name="innerKey1"
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
                                        name="innerKey2"
                                    ),
                                    value=FloatLiteral(
                                        position=(14, 21),
                                        value="3.14"
                                    ),
                                    expression_key=false
                                )
                            ]
                        ),
                        expression_key=false
                    ),
                    MapEntry(
                        position=(16, 5),
                        key=Symbol(
                            position=(16, 5),
                            name="outerKey2"
                        ),
                        value=ListLiteral(
                            position=(16, 17),
                            elements=[
                                IntegerLiteral(
                                    position=(16, 19),
                                    value="1"
                                ),
                                IntegerLiteral(
                                    position=(16, 22),
                                    value="2"
                                ),
                                IntegerLiteral(
                                    position=(16, 25),
                                    value="3"
                                )
                            ]
                        ),
                        expression_key=false
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(18, 1),
            name=Symbol(
                position=(18, 1),
                name="mapWithExpressions"
            ),
            value=MapLiteral(
                position=(18, 22),
                entries=[
                    MapEntry(
                        position=(19, 5),
                        key=Symbol(
                            position=(19, 5),
                            name="sumKey"
                        ),
                        value=BinaryOperation(
                            position=(19, 14),
                            left=IntegerLiteral(
                                position=(19, 16),
                                value="10"
                            ),
                            operator="+",
                            right=IntegerLiteral(
                                position=(19, 21),
                                value="20"
                            )
                        ),
                        expression_key=false
                    ),
                    MapEntry(
                        position=(20, 6),
                        key=BinaryOperation(
                            position=(20, 6),
                            left=StringLiteral(
                                position=(20, 6),
                                value="concat"
                            ),
                            operator="+",
                            right=StringLiteral(
                                position=(20, 17),
                                value="Key"
                            )
                        ),
                        value=BinaryOperation(
                            position=(20, 26),
                            left=StringLiteral(
                                position=(20, 26),
                                value="Hello, "
                            ),
                            operator="+",
                            right=StringLiteral(
                                position=(20, 38),
                                value="world!"
                            )
                        ),
                        expression_key=true
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(22, 1),
            name=Symbol(
                position=(22, 1),
                name="mapComprehension"
            ),
            value=MapComprehension(
                position=(22, 20),
                entry=MapEntry(
                    position=(22, 22),
                    key=Symbol(
                        position=(22, 22),
                        name="k"
                    ),
                    value=BinaryOperation(
                        position=(22, 26),
                        left=Symbol(
                            position=(22, 26),
                            name="v"
                        ),
                        operator="*",
                        right=IntegerLiteral(
                            position=(22, 31),
                            value="2"
                        )
                    ),
                    expression_key=false
                ),
                clauses=[
                    ComprehensionBinding(
                        position=(22, 32),
                        variables=[
                            Symbol(
                                position=(22, 36),
                                name="k"
                            ),
                            Symbol(
                                position=(22, 39),
                                name="v"
                            )
                        ],
                        iterable=Symbol(
                            position=(22, 44),
                            name="someMap"
                        )
                    ),
                    ComprehensionGuard(
                        position=(22, 52),
                        condition=BinaryOperation(
                            position=(22, 55),
                            left=Symbol(
                                position=(22, 55),
                                name="v"
                            ),
                            operator=">",
                            right=IntegerLiteral(
                                position=(22, 61),
                                value="10"
                            )
                        )
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(23, 1),
            name=Symbol(
                position=(23, 1),
                name="nestedComprehension"
            ),
            value=MapComprehension(
                position=(23, 23),
                entry=MapEntry(
                    position=(23, 25),
                    key=Symbol(
                        position=(23, 25),
                        name="k"
                    ),
                    value=MapComprehension(
                        position=(23, 29),
                        entry=MapEntry(
                            position=(23, 31),
                            key=Symbol(
                                position=(23, 31),
                                name="subK"
                            ),
                            value=Symbol(
                                position=(23, 38),
                                name="subV"
                            ),
                            expression_key=false
                        ),
                        clauses=[
                            ComprehensionBinding(
                                position=(23, 43),
                                variables=[
                                    Symbol(
                                        position=(23, 47),
                                        name="subK"
                                    ),
                                    Symbol(
                                        position=(23, 53),
                                        name="subV"
                                    )
                                ],
                                iterable=Symbol(
                                    position=(23, 61),
                                    name="v"
                                )
                            )
                        ]
                    ),
                    expression_key=false
                ),
                clauses=[
                    ComprehensionBinding(
                        position=(23, 65),
                        variables=[
                            Symbol(
                                position=(23, 69),
                                name="k"
                            ),
                            Symbol(
                                position=(23, 72),
                                name="v"
                            )
                        ],
                        iterable=Symbol(
                            position=(23, 77),
                            name="anotherMap"
                        )
                    )
                ]
            )
        )
    ]
)
*)
