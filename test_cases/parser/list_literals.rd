emptyList = [    ]
singleElementList = [42]
singleElementListWithTrailingComma = [
    3.14, 
]
listLiteralRetrieval = [
    10
    , 20
    , 30
][1]
listWithoutCommas = [
    1
    2
    3
    4
    5
]

multiElementList = [
    "apple",
    "banana",
    "cherry",
]
nestedLists = [
    [1, 2, 3],
    [4, 5, 6],
]
listWithExpressions = [
    1 + 2,
    3 * 4,
    5 - 6 * (8 / 2),
    8 + matrix[0][1] - vector.x,
]

simpleComprehension = [x * 2 for x in seq]
keyValueComprehension = [v for k, v in mapItems]
comprehensionWithCondition = [x for x in seq if x % 2 == 0]
multiComprehension = [
    x.name
    for xs in listOfLists
    if xs.length > 2
    for x in xs
    if x.active
]
nestedComprehension = [[y for y in x]for x in[[1, 2, 3]][0]if x % 2 == 1]

(*
Module(
    position=(1, 1),
    top_level_nodes=[
        VariableBindingStatement(
            position=(1, 1),
            name=Symbol(
                position=(1, 1),
                name="emptyList"
            ),
            value=ListLiteral(
                position=(1, 13),
                elements=[

                ]
            )
        ),
        VariableBindingStatement(
            position=(2, 1),
            name=Symbol(
                position=(2, 1),
                name="singleElementList"
            ),
            value=ListLiteral(
                position=(2, 21),
                elements=[
                    IntegerLiteral(
                        position=(2, 24),
                        value="42"
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(3, 1),
            name=Symbol(
                position=(3, 1),
                name="singleElementListWithTrailingComma"
            ),
            value=ListLiteral(
                position=(3, 38),
                elements=[
                    FloatLiteral(
                        position=(4, 5),
                        value="3.14"
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(6, 1),
            name=Symbol(
                position=(6, 1),
                name="listLiteralRetrieval"
            ),
            value=IndexAccess(
                position=(6, 24),
                collection=ListLiteral(
                    position=(6, 24),
                    elements=[
                        IntegerLiteral(
                            position=(7, 7),
                            value="10"
                        ),
                        IntegerLiteral(
                            position=(8, 9),
                            value="20"
                        ),
                        IntegerLiteral(
                            position=(9, 9),
                            value="30"
                        )
                    ]
                ),
                index=IntegerLiteral(
                    position=(10, 4),
                    value="1"
                )
            )
        ),
        VariableBindingStatement(
            position=(11, 1),
            name=Symbol(
                position=(11, 1),
                name="listWithoutCommas"
            ),
            value=ListLiteral(
                position=(11, 21),
                elements=[
                    IntegerLiteral(
                        position=(12, 6),
                        value="1"
                    ),
                    IntegerLiteral(
                        position=(13, 6),
                        value="2"
                    ),
                    IntegerLiteral(
                        position=(14, 6),
                        value="3"
                    ),
                    IntegerLiteral(
                        position=(15, 6),
                        value="4"
                    ),
                    IntegerLiteral(
                        position=(16, 6),
                        value="5"
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(19, 1),
            name=Symbol(
                position=(19, 1),
                name="multiElementList"
            ),
            value=ListLiteral(
                position=(19, 20),
                elements=[
                    StringLiteral(
                        position=(20, 5),
                        value="apple"
                    ),
                    StringLiteral(
                        position=(21, 5),
                        value="banana"
                    ),
                    StringLiteral(
                        position=(22, 5),
                        value="cherry"
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(24, 1),
            name=Symbol(
                position=(24, 1),
                name="nestedLists"
            ),
            value=ListLiteral(
                position=(24, 15),
                elements=[
                    ListLiteral(
                        position=(25, 5),
                        elements=[
                            IntegerLiteral(
                                position=(25, 7),
                                value="1"
                            ),
                            IntegerLiteral(
                                position=(25, 10),
                                value="2"
                            ),
                            IntegerLiteral(
                                position=(25, 13),
                                value="3"
                            )
                        ]
                    ),
                    ListLiteral(
                        position=(26, 5),
                        elements=[
                            IntegerLiteral(
                                position=(26, 7),
                                value="4"
                            ),
                            IntegerLiteral(
                                position=(26, 10),
                                value="5"
                            ),
                            IntegerLiteral(
                                position=(26, 13),
                                value="6"
                            )
                        ]
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(28, 1),
            name=Symbol(
                position=(28, 1),
                name="listWithExpressions"
            ),
            value=ListLiteral(
                position=(28, 23),
                elements=[
                    BinaryOperation(
                        position=(29, 5),
                        left=IntegerLiteral(
                            position=(29, 6),
                            value="1"
                        ),
                        operator="+",
                        right=IntegerLiteral(
                            position=(29, 10),
                            value="2"
                        )
                    ),
                    BinaryOperation(
                        position=(30, 5),
                        left=IntegerLiteral(
                            position=(30, 6),
                            value="3"
                        ),
                        operator="*",
                        right=IntegerLiteral(
                            position=(30, 10),
                            value="4"
                        )
                    ),
                    BinaryOperation(
                        position=(31, 5),
                        left=IntegerLiteral(
                            position=(31, 6),
                            value="5"
                        ),
                        operator="-",
                        right=BinaryOperation(
                            position=(31, 9),
                            left=IntegerLiteral(
                                position=(31, 10),
                                value="6"
                            ),
                            operator="*",
                            right=ParenthesizedExpression(
                                position=(31, 13),
                                expression=BinaryOperation(
                                    position=(31, 14),
                                    left=IntegerLiteral(
                                        position=(31, 15),
                                        value="8"
                                    ),
                                    operator="/",
                                    right=IntegerLiteral(
                                        position=(31, 19),
                                        value="2"
                                    )
                                )
                            )
                        )
                    ),
                    BinaryOperation(
                        position=(32, 5),
                        left=BinaryOperation(
                            position=(32, 5),
                            left=IntegerLiteral(
                                position=(32, 6),
                                value="8"
                            ),
                            operator="+",
                            right=IndexAccess(
                                position=(32, 9),
                                collection=IndexAccess(
                                    position=(32, 9),
                                    collection=Symbol(
                                        position=(32, 9),
                                        name="matrix"
                                    ),
                                    index=IntegerLiteral(
                                        position=(32, 17),
                                        value="0"
                                    )
                                ),
                                index=IntegerLiteral(
                                    position=(32, 20),
                                    value="1"
                                )
                            )
                        ),
                        operator="-",
                        right=AttributeAccess(
                            position=(32, 24),
                            object=Symbol(
                                position=(32, 24),
                                name="vector"
                            ),
                            attribute=Symbol(
                                position=(32, 31),
                                name="x"
                            )
                        )
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(35, 1),
            name=Symbol(
                position=(35, 1),
                name="simpleComprehension"
            ),
            value=ListComprehension(
                position=(35, 23),
                element=BinaryOperation(
                    position=(35, 24),
                    left=Symbol(
                        position=(35, 24),
                        name="x"
                    ),
                    operator="*",
                    right=IntegerLiteral(
                        position=(35, 29),
                        value="2"
                    )
                ),
                clauses=[
                    ComprehensionBinding(
                        position=(35, 30),
                        variables=[
                            Symbol(
                                position=(35, 34),
                                name="x"
                            )
                        ],
                        iterable=Symbol(
                            position=(35, 39),
                            name="seq"
                        )
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(36, 1),
            name=Symbol(
                position=(36, 1),
                name="keyValueComprehension"
            ),
            value=ListComprehension(
                position=(36, 25),
                element=Symbol(
                    position=(36, 26),
                    name="v"
                ),
                clauses=[
                    ComprehensionBinding(
                        position=(36, 28),
                        variables=[
                            Symbol(
                                position=(36, 32),
                                name="k"
                            ),
                            Symbol(
                                position=(36, 35),
                                name="v"
                            )
                        ],
                        iterable=Symbol(
                            position=(36, 40),
                            name="mapItems"
                        )
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(37, 1),
            name=Symbol(
                position=(37, 1),
                name="comprehensionWithCondition"
            ),
            value=ListComprehension(
                position=(37, 30),
                element=Symbol(
                    position=(37, 31),
                    name="x"
                ),
                clauses=[
                    ComprehensionBinding(
                        position=(37, 33),
                        variables=[
                            Symbol(
                                position=(37, 37),
                                name="x"
                            )
                        ],
                        iterable=Symbol(
                            position=(37, 42),
                            name="seq"
                        )
                    ),
                    ComprehensionGuard(
                        position=(37, 46),
                        condition=BinaryOperation(
                            position=(37, 49),
                            left=BinaryOperation(
                                position=(37, 49),
                                left=Symbol(
                                    position=(37, 49),
                                    name="x"
                                ),
                                operator="%",
                                right=IntegerLiteral(
                                    position=(37, 54),
                                    value="2"
                                )
                            ),
                            operator="==",
                            right=IntegerLiteral(
                                position=(37, 59),
                                value="0"
                            )
                        )
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(38, 1),
            name=Symbol(
                position=(38, 1),
                name="multiComprehension"
            ),
            value=ListComprehension(
                position=(38, 22),
                element=AttributeAccess(
                    position=(39, 5),
                    object=Symbol(
                        position=(39, 5),
                        name="x"
                    ),
                    attribute=Symbol(
                        position=(39, 7),
                        name="name"
                    )
                ),
                clauses=[
                    ComprehensionBinding(
                        position=(40, 5),
                        variables=[
                            Symbol(
                                position=(40, 9),
                                name="xs"
                            )
                        ],
                        iterable=Symbol(
                            position=(40, 15),
                            name="listOfLists"
                        )
                    ),
                    ComprehensionGuard(
                        position=(41, 5),
                        condition=BinaryOperation(
                            position=(41, 8),
                            left=AttributeAccess(
                                position=(41, 8),
                                object=Symbol(
                                    position=(41, 8),
                                    name="xs"
                                ),
                                attribute=Symbol(
                                    position=(41, 11),
                                    name="length"
                                )
                            ),
                            operator=">",
                            right=IntegerLiteral(
                                position=(41, 21),
                                value="2"
                            )
                        )
                    ),
                    ComprehensionBinding(
                        position=(42, 5),
                        variables=[
                            Symbol(
                                position=(42, 9),
                                name="x"
                            )
                        ],
                        iterable=Symbol(
                            position=(42, 14),
                            name="xs"
                        )
                    ),
                    ComprehensionGuard(
                        position=(43, 5),
                        condition=AttributeAccess(
                            position=(43, 8),
                            object=Symbol(
                                position=(43, 8),
                                name="x"
                            ),
                            attribute=Symbol(
                                position=(43, 10),
                                name="active"
                            )
                        )
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(45, 1),
            name=Symbol(
                position=(45, 1),
                name="nestedComprehension"
            ),
            value=ListComprehension(
                position=(45, 23),
                element=ListComprehension(
                    position=(45, 24),
                    element=Symbol(
                        position=(45, 25),
                        name="y"
                    ),
                    clauses=[
                        ComprehensionBinding(
                            position=(45, 27),
                            variables=[
                                Symbol(
                                    position=(45, 31),
                                    name="y"
                                )
                            ],
                            iterable=Symbol(
                                position=(45, 36),
                                name="x"
                            )
                        )
                    ]
                ),
                clauses=[
                    ComprehensionBinding(
                        position=(45, 38),
                        variables=[
                            Symbol(
                                position=(45, 42),
                                name="x"
                            )
                        ],
                        iterable=IndexAccess(
                            position=(45, 46),
                            collection=ListLiteral(
                                position=(45, 46),
                                elements=[
                                    ListLiteral(
                                        position=(45, 47),
                                        elements=[
                                            IntegerLiteral(
                                                position=(45, 49),
                                                value="1"
                                            ),
                                            IntegerLiteral(
                                                position=(45, 52),
                                                value="2"
                                            ),
                                            IntegerLiteral(
                                                position=(45, 55),
                                                value="3"
                                            )
                                        ]
                                    )
                                ]
                            ),
                            index=IntegerLiteral(
                                position=(45, 59),
                                value="0"
                            )
                        )
                    ),
                    ComprehensionGuard(
                        position=(45, 60),
                        condition=BinaryOperation(
                            position=(45, 63),
                            left=BinaryOperation(
                                position=(45, 63),
                                left=Symbol(
                                    position=(45, 63),
                                    name="x"
                                ),
                                operator="%",
                                right=IntegerLiteral(
                                    position=(45, 68),
                                    value="2"
                                )
                            ),
                            operator="==",
                            right=IntegerLiteral(
                                position=(45, 73),
                                value="1"
                            )
                        )
                    )
                ]
            )
        )
    ]
)
*)
