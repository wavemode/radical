intLiteralIndex = arr[0]
stringLiteralIndex = map["key"]

multipleIndices = matrix[1][2]

sliceAccess = arr[1:4]
sliceAccessNoStart = arr[:3]
sliceAccessNoEnd = arr[2:]
fullSliceAccess = arr[:]
nestedSliceAccess = matrix[0:2][1:3]

(*
Module(
    position=(1, 1),
    top_level_nodes=[
        VariableBindingStatement(
            position=(1, 1),
            name=Symbol(
                position=(1, 1),
                name="intLiteralIndex"
            ),
            value=IndexAccess(
                position=(1, 19),
                collection=Symbol(
                    position=(1, 19),
                    name="arr"
                ),
                index=IntegerLiteral(
                    position=(1, 24),
                    value="0"
                )
            )
        ),
        VariableBindingStatement(
            position=(2, 1),
            name=Symbol(
                position=(2, 1),
                name="stringLiteralIndex"
            ),
            value=IndexAccess(
                position=(2, 22),
                collection=Symbol(
                    position=(2, 22),
                    name="map"
                ),
                index=StringLiteral(
                    position=(2, 26),
                    value="key"
                )
            )
        ),
        VariableBindingStatement(
            position=(4, 1),
            name=Symbol(
                position=(4, 1),
                name="multipleIndices"
            ),
            value=IndexAccess(
                position=(4, 19),
                collection=IndexAccess(
                    position=(4, 19),
                    collection=Symbol(
                        position=(4, 19),
                        name="matrix"
                    ),
                    index=IntegerLiteral(
                        position=(4, 27),
                        value="1"
                    )
                ),
                index=IntegerLiteral(
                    position=(4, 30),
                    value="2"
                )
            )
        ),
        VariableBindingStatement(
            position=(6, 1),
            name=Symbol(
                position=(6, 1),
                name="sliceAccess"
            ),
            value=SliceAccess(
                position=(6, 15),
                collection=Symbol(
                    position=(6, 15),
                    name="arr"
                ),
                start=IntegerLiteral(
                    position=(6, 20),
                    value="1"
                ),
                end=IntegerLiteral(
                    position=(6, 22),
                    value="4"
                )
            )
        ),
        VariableBindingStatement(
            position=(7, 1),
            name=Symbol(
                position=(7, 1),
                name="sliceAccessNoStart"
            ),
            value=SliceAccess(
                position=(7, 22),
                collection=Symbol(
                    position=(7, 22),
                    name="arr"
                ),
                end=IntegerLiteral(
                    position=(7, 28),
                    value="3"
                )
            )
        ),
        VariableBindingStatement(
            position=(8, 1),
            name=Symbol(
                position=(8, 1),
                name="sliceAccessNoEnd"
            ),
            value=SliceAccess(
                position=(8, 20),
                collection=Symbol(
                    position=(8, 20),
                    name="arr"
                ),
                start=IntegerLiteral(
                    position=(8, 25),
                    value="2"
                )
            )
        ),
        VariableBindingStatement(
            position=(9, 1),
            name=Symbol(
                position=(9, 1),
                name="fullSliceAccess"
            ),
            value=SliceAccess(
                position=(9, 19),
                collection=Symbol(
                    position=(9, 19),
                    name="arr"
                )
            )
        ),
        VariableBindingStatement(
            position=(10, 1),
            name=Symbol(
                position=(10, 1),
                name="nestedSliceAccess"
            ),
            value=SliceAccess(
                position=(10, 21),
                collection=SliceAccess(
                    position=(10, 21),
                    collection=Symbol(
                        position=(10, 21),
                        name="matrix"
                    ),
                    start=IntegerLiteral(
                        position=(10, 29),
                        value="0"
                    ),
                    end=IntegerLiteral(
                        position=(10, 31),
                        value="2"
                    )
                ),
                start=IntegerLiteral(
                    position=(10, 34),
                    value="1"
                ),
                end=IntegerLiteral(
                    position=(10, 36),
                    value="3"
                )
            )
        ),
        VariableBindingStatement(
            position=(244, 1),
            name=Symbol(
                position=(244, 1),
                name="expressionSlice"
            ),
            value=SliceAccess(
                position=(244, 19),
                collection=Symbol(
                    position=(244, 19),
                    name="arr"
                ),
                start=IndexAccess(
                    position=(244, 23),
                    collection=IndexAccess(
                        position=(244, 23),
                        collection=Symbol(
                            position=(244, 23),
                            name="matrix"
                        ),
                        index=IntegerLiteral(
                            position=(244, 31),
                            value="0"
                        )
                    ),
                    index=IntegerLiteral(
                        position=(244, 34),
                        value="0"
                    )
                ),
                end=BinaryOperation(
                    position=(244, 38),
                    left=IndexAccess(
                        position=(244, 38),
                        collection=IndexAccess(
                            position=(244, 38),
                            collection=Symbol(
                                position=(244, 38),
                                name="matrix"
                            ),
                            index=IntegerLiteral(
                                position=(244, 46),
                                value="1"
                            )
                        ),
                        index=IntegerLiteral(
                            position=(244, 49),
                            value="1"
                        )
                    ),
                    operator="+",
                    right=IntegerLiteral(
                        position=(244, 54),
                        value="2"
                    )
                )
            )
        )
    ]
)
*)

expressionSlice = arr[matrix[0][0] : matrix[1][1] + 2]