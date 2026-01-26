listWithSingleSpread = [...otherList]
mapWithSingleSpread = {
    ...otherMap
}

listWithMultipleSpreads = [
    1
    ...listA
    2
    ...listB
    3
]

mapWithMultipleSpreads = {
    key1 = "value1"
    ...mapA
    key2 = "value2"
    ...mapB
    key3 = "value3"
}

setWithMultipleSpreads = {
    1
    ...setA
    2
    ...setB
    3
}

treeWithMultipleSpreads = {
    name "value"
    ...treeA
    otherName {
        child1 10
        child2 20.0
    }
    ...treeB
}

(*
Module(
    position=(1, 1),
    top_level_nodes=[
        VariableBindingStatement(
            position=(1, 1),
            name=Symbol(
                position=(1, 1),
                name="listWithSingleSpread",
                quoted=false
            ),
            value=ListLiteral(
                position=(1, 24),
                elements=[
                    SpreadOperation(
                        position=(1, 25),
                        collection=Symbol(
                            position=(1, 28),
                            name="otherList",
                            quoted=false
                        )
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(2, 1),
            name=Symbol(
                position=(2, 1),
                name="mapWithSingleSpread",
                quoted=false
            ),
            value=MapLiteral(
                position=(2, 23),
                entries=[
                    SpreadOperation(
                        position=(3, 5),
                        collection=Symbol(
                            position=(3, 8),
                            name="otherMap",
                            quoted=false
                        )
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(6, 1),
            name=Symbol(
                position=(6, 1),
                name="listWithMultipleSpreads",
                quoted=false
            ),
            value=ListLiteral(
                position=(6, 27),
                elements=[
                    IntegerLiteral(
                        position=(7, 5),
                        value="1"
                    ),
                    SpreadOperation(
                        position=(8, 5),
                        collection=Symbol(
                            position=(8, 8),
                            name="listA",
                            quoted=false
                        )
                    ),
                    IntegerLiteral(
                        position=(9, 5),
                        value="2"
                    ),
                    SpreadOperation(
                        position=(10, 5),
                        collection=Symbol(
                            position=(10, 8),
                            name="listB",
                            quoted=false
                        )
                    ),
                    IntegerLiteral(
                        position=(11, 5),
                        value="3"
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(14, 1),
            name=Symbol(
                position=(14, 1),
                name="mapWithMultipleSpreads",
                quoted=false
            ),
            value=MapLiteral(
                position=(14, 26),
                entries=[
                    MapEntry(
                        position=(15, 5),
                        key=Symbol(
                            position=(15, 5),
                            name="key1",
                            quoted=false
                        ),
                        value=StringLiteral(
                            position=(15, 12),
                            value="value1"
                        ),
                        expression_key=false
                    ),
                    SpreadOperation(
                        position=(16, 5),
                        collection=Symbol(
                            position=(16, 8),
                            name="mapA",
                            quoted=false
                        )
                    ),
                    MapEntry(
                        position=(17, 5),
                        key=Symbol(
                            position=(17, 5),
                            name="key2",
                            quoted=false
                        ),
                        value=StringLiteral(
                            position=(17, 12),
                            value="value2"
                        ),
                        expression_key=false
                    ),
                    SpreadOperation(
                        position=(18, 5),
                        collection=Symbol(
                            position=(18, 8),
                            name="mapB",
                            quoted=false
                        )
                    ),
                    MapEntry(
                        position=(19, 5),
                        key=Symbol(
                            position=(19, 5),
                            name="key3",
                            quoted=false
                        ),
                        value=StringLiteral(
                            position=(19, 12),
                            value="value3"
                        ),
                        expression_key=false
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(22, 1),
            name=Symbol(
                position=(22, 1),
                name="setWithMultipleSpreads",
                quoted=false
            ),
            value=SetLiteral(
                position=(22, 26),
                elements=[
                    IntegerLiteral(
                        position=(23, 5),
                        value="1"
                    ),
                    SpreadOperation(
                        position=(24, 5),
                        collection=Symbol(
                            position=(24, 8),
                            name="setA",
                            quoted=false
                        )
                    ),
                    IntegerLiteral(
                        position=(25, 5),
                        value="2"
                    ),
                    SpreadOperation(
                        position=(26, 5),
                        collection=Symbol(
                            position=(26, 8),
                            name="setB",
                            quoted=false
                        )
                    ),
                    IntegerLiteral(
                        position=(27, 5),
                        value="3"
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(30, 1),
            name=Symbol(
                position=(30, 1),
                name="treeWithMultipleSpreads",
                quoted=false
            ),
            value=TreeLiteral(
                position=(30, 27),
                entries=[
                    TreeEntry(
                        position=(31, 5),
                        key=Symbol(
                            position=(31, 5),
                            name="name",
                            quoted=false
                        ),
                        value=StringLiteral(
                            position=(31, 10),
                            value="value"
                        ),
                        expression_key=false
                    ),
                    SpreadOperation(
                        position=(32, 5),
                        collection=Symbol(
                            position=(32, 8),
                            name="treeA",
                            quoted=false
                        )
                    ),
                    TreeEntry(
                        position=(33, 5),
                        key=Symbol(
                            position=(33, 5),
                            name="otherName",
                            quoted=false
                        ),
                        value=TreeLiteral(
                            position=(33, 15),
                            entries=[
                                TreeEntry(
                                    position=(34, 9),
                                    key=Symbol(
                                        position=(34, 9),
                                        name="child1",
                                        quoted=false
                                    ),
                                    value=IntegerLiteral(
                                        position=(34, 16),
                                        value="10"
                                    ),
                                    expression_key=false
                                ),
                                TreeEntry(
                                    position=(35, 9),
                                    key=Symbol(
                                        position=(35, 9),
                                        name="child2",
                                        quoted=false
                                    ),
                                    value=FloatLiteral(
                                        position=(35, 16),
                                        value="20.0"
                                    ),
                                    expression_key=false
                                )
                            ]
                        ),
                        expression_key=false
                    ),
                    SpreadOperation(
                        position=(37, 5),
                        collection=Symbol(
                            position=(37, 8),
                            name="treeB",
                            quoted=false
                        )
                    )
                ]
            )
        )
    ]
)
*)
