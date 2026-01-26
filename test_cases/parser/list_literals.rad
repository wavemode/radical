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
                name="emptyList",
                quoted=false
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
                name="singleElementList",
                quoted=false
            ),
            value=ListLiteral(
                position=(2, 21),
                elements=[
                    IntegerLiteral(
                        position=(2, 22),
                        value="42"
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(3, 1),
            name=Symbol(
                position=(3, 1),
                name="singleElementListWithTrailingComma",
                quoted=false
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
                name="listLiteralRetrieval",
                quoted=false
            ),
            value=IndexAccess(
                position=(6, 24),
                collection=ListLiteral(
                    position=(6, 24),
                    elements=[
                        IntegerLiteral(
                            position=(7, 5),
                            value="10"
                        ),
                        IntegerLiteral(
                            position=(8, 7),
                            value="20"
                        ),
                        IntegerLiteral(
                            position=(9, 7),
                            value="30"
                        )
                    ]
                ),
                index=IntegerLiteral(
                    position=(10, 3),
                    value="1"
                )
            )
        ),
        VariableBindingStatement(
            position=(11, 1),
            name=Symbol(
                position=(11, 1),
                name="listWithoutCommas",
                quoted=false
            ),
            value=ListLiteral(
                position=(11, 21),
                elements=[
                    IntegerLiteral(
                        position=(12, 5),
                        value="1"
                    ),
                    IntegerLiteral(
                        position=(13, 5),
                        value="2"
                    ),
                    IntegerLiteral(
                        position=(14, 5),
                        value="3"
                    ),
                    IntegerLiteral(
                        position=(15, 5),
                        value="4"
                    ),
                    IntegerLiteral(
                        position=(16, 5),
                        value="5"
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(19, 1),
            name=Symbol(
                position=(19, 1),
                name="multiElementList",
                quoted=false
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
                name="nestedLists",
                quoted=false
            ),
            value=ListLiteral(
                position=(24, 15),
                elements=[
                    ListLiteral(
                        position=(25, 5),
                        elements=[
                            IntegerLiteral(
                                position=(25, 6),
                                value="1"
                            ),
                            IntegerLiteral(
                                position=(25, 9),
                                value="2"
                            ),
                            IntegerLiteral(
                                position=(25, 12),
                                value="3"
                            )
                        ]
                    ),
                    ListLiteral(
                        position=(26, 5),
                        elements=[
                            IntegerLiteral(
                                position=(26, 6),
                                value="4"
                            ),
                            IntegerLiteral(
                                position=(26, 9),
                                value="5"
                            ),
                            IntegerLiteral(
                                position=(26, 12),
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
                name="listWithExpressions",
                quoted=false
            ),
            value=ListLiteral(
                position=(28, 23),
                elements=[
                    BinaryOperation(
                        position=(29, 5),
                        left=IntegerLiteral(
                            position=(29, 5),
                            value="1"
                        ),
                        operator="+",
                        right=IntegerLiteral(
                            position=(29, 9),
                            value="2"
                        )
                    ),
                    BinaryOperation(
                        position=(30, 5),
                        left=IntegerLiteral(
                            position=(30, 5),
                            value="3"
                        ),
                        operator="*",
                        right=IntegerLiteral(
                            position=(30, 9),
                            value="4"
                        )
                    ),
                    BinaryOperation(
                        position=(31, 5),
                        left=IntegerLiteral(
                            position=(31, 5),
                            value="5"
                        ),
                        operator="-",
                        right=BinaryOperation(
                            position=(31, 9),
                            left=IntegerLiteral(
                                position=(31, 9),
                                value="6"
                            ),
                            operator="*",
                            right=ParenthesizedExpression(
                                position=(31, 13),
                                expression=BinaryOperation(
                                    position=(31, 14),
                                    left=IntegerLiteral(
                                        position=(31, 14),
                                        value="8"
                                    ),
                                    operator="/",
                                    right=IntegerLiteral(
                                        position=(31, 18),
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
                                position=(32, 5),
                                value="8"
                            ),
                            operator="+",
                            right=IndexAccess(
                                position=(32, 9),
                                collection=IndexAccess(
                                    position=(32, 9),
                                    collection=Symbol(
                                        position=(32, 9),
                                        name="matrix",
                                        quoted=false
                                    ),
                                    index=IntegerLiteral(
                                        position=(32, 16),
                                        value="0"
                                    )
                                ),
                                index=IntegerLiteral(
                                    position=(32, 19),
                                    value="1"
                                )
                            )
                        ),
                        operator="-",
                        right=AttributeAccess(
                            position=(32, 24),
                            object=Symbol(
                                position=(32, 24),
                                name="vector",
                                quoted=false
                            ),
                            attribute=Symbol(
                                position=(32, 31),
                                name="x",
                                quoted=false
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
                name="simpleComprehension",
                quoted=false
            ),
            value=ListComprehension(
                position=(35, 23),
                element=BinaryOperation(
                    position=(35, 24),
                    left=Symbol(
                        position=(35, 24),
                        name="x",
                        quoted=false
                    ),
                    operator="*",
                    right=IntegerLiteral(
                        position=(35, 28),
                        value="2"
                    )
                ),
                clauses=[
                    ComprehensionBinding(
                        position=(35, 30),
                        variables=[
                            Symbol(
                                position=(35, 34),
                                name="x",
                                quoted=false
                            )
                        ],
                        iterable=Symbol(
                            position=(35, 39),
                            name="seq",
                            quoted=false
                        )
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(36, 1),
            name=Symbol(
                position=(36, 1),
                name="keyValueComprehension",
                quoted=false
            ),
            value=ListComprehension(
                position=(36, 25),
                element=Symbol(
                    position=(36, 26),
                    name="v",
                    quoted=false
                ),
                clauses=[
                    ComprehensionBinding(
                        position=(36, 28),
                        variables=[
                            Symbol(
                                position=(36, 32),
                                name="k",
                                quoted=false
                            ),
                            Symbol(
                                position=(36, 35),
                                name="v",
                                quoted=false
                            )
                        ],
                        iterable=Symbol(
                            position=(36, 40),
                            name="mapItems",
                            quoted=false
                        )
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(37, 1),
            name=Symbol(
                position=(37, 1),
                name="comprehensionWithCondition",
                quoted=false
            ),
            value=ListComprehension(
                position=(37, 30),
                element=Symbol(
                    position=(37, 31),
                    name="x",
                    quoted=false
                ),
                clauses=[
                    ComprehensionBinding(
                        position=(37, 33),
                        variables=[
                            Symbol(
                                position=(37, 37),
                                name="x",
                                quoted=false
                            )
                        ],
                        iterable=Symbol(
                            position=(37, 42),
                            name="seq",
                            quoted=false
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
                                    name="x",
                                    quoted=false
                                ),
                                operator="%",
                                right=IntegerLiteral(
                                    position=(37, 53),
                                    value="2"
                                )
                            ),
                            operator="==",
                            right=IntegerLiteral(
                                position=(37, 58),
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
                name="multiComprehension",
                quoted=false
            ),
            value=ListComprehension(
                position=(38, 22),
                element=AttributeAccess(
                    position=(39, 5),
                    object=Symbol(
                        position=(39, 5),
                        name="x",
                        quoted=false
                    ),
                    attribute=Symbol(
                        position=(39, 7),
                        name="name",
                        quoted=false
                    )
                ),
                clauses=[
                    ComprehensionBinding(
                        position=(40, 5),
                        variables=[
                            Symbol(
                                position=(40, 9),
                                name="xs",
                                quoted=false
                            )
                        ],
                        iterable=Symbol(
                            position=(40, 15),
                            name="listOfLists",
                            quoted=false
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
                                    name="xs",
                                    quoted=false
                                ),
                                attribute=Symbol(
                                    position=(41, 11),
                                    name="length",
                                    quoted=false
                                )
                            ),
                            operator=">",
                            right=IntegerLiteral(
                                position=(41, 20),
                                value="2"
                            )
                        )
                    ),
                    ComprehensionBinding(
                        position=(42, 5),
                        variables=[
                            Symbol(
                                position=(42, 9),
                                name="x",
                                quoted=false
                            )
                        ],
                        iterable=Symbol(
                            position=(42, 14),
                            name="xs",
                            quoted=false
                        )
                    ),
                    ComprehensionGuard(
                        position=(43, 5),
                        condition=AttributeAccess(
                            position=(43, 8),
                            object=Symbol(
                                position=(43, 8),
                                name="x",
                                quoted=false
                            ),
                            attribute=Symbol(
                                position=(43, 10),
                                name="active",
                                quoted=false
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
                name="nestedComprehension",
                quoted=false
            ),
            value=ListComprehension(
                position=(45, 23),
                element=ListComprehension(
                    position=(45, 24),
                    element=Symbol(
                        position=(45, 25),
                        name="y",
                        quoted=false
                    ),
                    clauses=[
                        ComprehensionBinding(
                            position=(45, 27),
                            variables=[
                                Symbol(
                                    position=(45, 31),
                                    name="y",
                                    quoted=false
                                )
                            ],
                            iterable=Symbol(
                                position=(45, 36),
                                name="x",
                                quoted=false
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
                                name="x",
                                quoted=false
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
                                                position=(45, 48),
                                                value="1"
                                            ),
                                            IntegerLiteral(
                                                position=(45, 51),
                                                value="2"
                                            ),
                                            IntegerLiteral(
                                                position=(45, 54),
                                                value="3"
                                            )
                                        ]
                                    )
                                ]
                            ),
                            index=IntegerLiteral(
                                position=(45, 58),
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
                                    name="x",
                                    quoted=false
                                ),
                                operator="%",
                                right=IntegerLiteral(
                                    position=(45, 67),
                                    value="2"
                                )
                            ),
                            operator="==",
                            right=IntegerLiteral(
                                position=(45, 72),
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
