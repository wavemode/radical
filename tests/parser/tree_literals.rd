singleEntryTree = { a b, }
multiEntryTree = {
    rootLeft childLeft1,
    rootLeft childLeft2,
    rootRight childRight1,
    rootRight childRight2,
}
nestedTree = {
    parent1 {
        child1A grandchild1
        child1B grandchild2
    }
    , parent2 {
        child2A grandchild3
        child2B grandchild4
    }
}


tripleNestedTreeNoCommas = {
    grandParent1 {
        parent1 {
            child1A grandchild1
            child1B grandchild2
        }
        parent2 {
            child2A grandchild3
            child2B grandchild4
        }
    }
    grandParent2 {
        parent3 {
            child3A grandchild5
            child3B grandchild6
        }
    }
}

(*
Module(
    top_level_nodes=[
        VariableBindingStatement(
            name=Symbol(
                name="singleEntryTree"
            ),
            value=TreeLiteral(
                entries=[
                    Entry(
                        key=Symbol(
                            name="a"
                        ),
                        value=Symbol(
                            name="b"
                        )
                    )
                ]
            )
        ),
        VariableBindingStatement(
            name=Symbol(
                name="multiEntryTree"
            ),
            value=TreeLiteral(
                entries=[
                    Entry(
                        key=Symbol(
                            name="rootLeft"
                        ),
                        value=Symbol(
                            name="childLeft1"
                        )
                    ),
                    Entry(
                        key=Symbol(
                            name="rootLeft"
                        ),
                        value=Symbol(
                            name="childLeft2"
                        )
                    ),
                    Entry(
                        key=Symbol(
                            name="rootRight"
                        ),
                        value=Symbol(
                            name="childRight1"
                        )
                    ),
                    Entry(
                        key=Symbol(
                            name="rootRight"
                        ),
                        value=Symbol(
                            name="childRight2"
                        )
                    )
                ]
            )
        ),
        VariableBindingStatement(
            name=Symbol(
                name="nestedTree"
            ),
            value=TreeLiteral(
                entries=[
                    Entry(
                        key=Symbol(
                            name="parent1"
                        ),
                        value=TreeLiteral(
                            entries=[
                                Entry(
                                    key=Symbol(
                                        name="child1A"
                                    ),
                                    value=Symbol(
                                        name="grandchild1"
                                    )
                                ),
                                Entry(
                                    key=Symbol(
                                        name="child1B"
                                    ),
                                    value=Symbol(
                                        name="grandchild2"
                                    )
                                )
                            ]
                        )
                    ),
                    Entry(
                        key=Symbol(
                            name="parent2"
                        ),
                        value=TreeLiteral(
                            entries=[
                                Entry(
                                    key=Symbol(
                                        name="child2A"
                                    ),
                                    value=Symbol(
                                        name="grandchild3"
                                    )
                                ),
                                Entry(
                                    key=Symbol(
                                        name="child2B"
                                    ),
                                    value=Symbol(
                                        name="grandchild4"
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        ),
        VariableBindingStatement(
            name=Symbol(
                name="tripleNestedTreeNoCommas"
            ),
            value=TreeLiteral(
                entries=[
                    Entry(
                        key=Symbol(
                            name="grandParent1"
                        ),
                        value=TreeLiteral(
                            entries=[
                                Entry(
                                    key=Symbol(
                                        name="parent1"
                                    ),
                                    value=TreeLiteral(
                                        entries=[
                                            Entry(
                                                key=Symbol(
                                                    name="child1A"
                                                ),
                                                value=Symbol(
                                                    name="grandchild1"
                                                )
                                            ),
                                            Entry(
                                                key=Symbol(
                                                    name="child1B"
                                                ),
                                                value=Symbol(
                                                    name="grandchild2"
                                                )
                                            )
                                        ]
                                    )
                                ),
                                Entry(
                                    key=Symbol(
                                        name="parent2"
                                    ),
                                    value=TreeLiteral(
                                        entries=[
                                            Entry(
                                                key=Symbol(
                                                    name="child2A"
                                                ),
                                                value=Symbol(
                                                    name="grandchild3"
                                                )
                                            ),
                                            Entry(
                                                key=Symbol(
                                                    name="child2B"
                                                ),
                                                value=Symbol(
                                                    name="grandchild4"
                                                )
                                            )
                                        ]
                                    )
                                )
                            ]
                        )
                    ),
                    Entry(
                        key=Symbol(
                            name="grandParent2"
                        ),
                        value=TreeLiteral(
                            entries=[
                                Entry(
                                    key=Symbol(
                                        name="parent3"
                                    ),
                                    value=TreeLiteral(
                                        entries=[
                                            Entry(
                                                key=Symbol(
                                                    name="child3A"
                                                ),
                                                value=Symbol(
                                                    name="grandchild5"
                                                )
                                            ),
                                            Entry(
                                                key=Symbol(
                                                    name="child3B"
                                                ),
                                                value=Symbol(
                                                    name="grandchild6"
                                                )
                                            )
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )
    ]
)
*)
