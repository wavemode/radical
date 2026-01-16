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

treeComprehension = {
    ["a"] {
        b { 
            c
        }
    }
    for a in someSetA
    for b in someSetB
    for c in someSetC
}

(*
Module(
    position=(1, 1),
    top_level_nodes=[
        VariableBindingStatement(
            position=(1, 1),
            name=Symbol(
                position=(1, 1),
                name="singleEntryTree"
            ),
            value=TreeLiteral(
                position=(1, 19),
                entries=[
                    TreeEntry(
                        position=(1, 21),
                        key=Symbol(
                            position=(1, 21),
                            name="a"
                        ),
                        value=Symbol(
                            position=(1, 23),
                            name="b"
                        ),
                        expression_key=false
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(2, 1),
            name=Symbol(
                position=(2, 1),
                name="multiEntryTree"
            ),
            value=TreeLiteral(
                position=(2, 18),
                entries=[
                    TreeEntry(
                        position=(3, 5),
                        key=Symbol(
                            position=(3, 5),
                            name="rootLeft"
                        ),
                        value=Symbol(
                            position=(3, 14),
                            name="childLeft1"
                        ),
                        expression_key=false
                    ),
                    TreeEntry(
                        position=(4, 5),
                        key=Symbol(
                            position=(4, 5),
                            name="rootLeft"
                        ),
                        value=Symbol(
                            position=(4, 14),
                            name="childLeft2"
                        ),
                        expression_key=false
                    ),
                    TreeEntry(
                        position=(5, 5),
                        key=Symbol(
                            position=(5, 5),
                            name="rootRight"
                        ),
                        value=Symbol(
                            position=(5, 15),
                            name="childRight1"
                        ),
                        expression_key=false
                    ),
                    TreeEntry(
                        position=(6, 5),
                        key=Symbol(
                            position=(6, 5),
                            name="rootRight"
                        ),
                        value=Symbol(
                            position=(6, 15),
                            name="childRight2"
                        ),
                        expression_key=false
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(8, 1),
            name=Symbol(
                position=(8, 1),
                name="nestedTree"
            ),
            value=TreeLiteral(
                position=(8, 14),
                entries=[
                    TreeEntry(
                        position=(9, 5),
                        key=Symbol(
                            position=(9, 5),
                            name="parent1"
                        ),
                        value=TreeLiteral(
                            position=(9, 13),
                            entries=[
                                TreeEntry(
                                    position=(10, 9),
                                    key=Symbol(
                                        position=(10, 9),
                                        name="child1A"
                                    ),
                                    value=Symbol(
                                        position=(10, 17),
                                        name="grandchild1"
                                    ),
                                    expression_key=false
                                ),
                                TreeEntry(
                                    position=(11, 9),
                                    key=Symbol(
                                        position=(11, 9),
                                        name="child1B"
                                    ),
                                    value=Symbol(
                                        position=(11, 17),
                                        name="grandchild2"
                                    ),
                                    expression_key=false
                                )
                            ]
                        ),
                        expression_key=false
                    ),
                    TreeEntry(
                        position=(13, 7),
                        key=Symbol(
                            position=(13, 7),
                            name="parent2"
                        ),
                        value=TreeLiteral(
                            position=(13, 15),
                            entries=[
                                TreeEntry(
                                    position=(14, 9),
                                    key=Symbol(
                                        position=(14, 9),
                                        name="child2A"
                                    ),
                                    value=Symbol(
                                        position=(14, 17),
                                        name="grandchild3"
                                    ),
                                    expression_key=false
                                ),
                                TreeEntry(
                                    position=(15, 9),
                                    key=Symbol(
                                        position=(15, 9),
                                        name="child2B"
                                    ),
                                    value=Symbol(
                                        position=(15, 17),
                                        name="grandchild4"
                                    ),
                                    expression_key=false
                                )
                            ]
                        ),
                        expression_key=false
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(20, 1),
            name=Symbol(
                position=(20, 1),
                name="tripleNestedTreeNoCommas"
            ),
            value=TreeLiteral(
                position=(20, 28),
                entries=[
                    TreeEntry(
                        position=(21, 5),
                        key=Symbol(
                            position=(21, 5),
                            name="grandParent1"
                        ),
                        value=TreeLiteral(
                            position=(21, 18),
                            entries=[
                                TreeEntry(
                                    position=(22, 9),
                                    key=Symbol(
                                        position=(22, 9),
                                        name="parent1"
                                    ),
                                    value=TreeLiteral(
                                        position=(22, 17),
                                        entries=[
                                            TreeEntry(
                                                position=(23, 13),
                                                key=Symbol(
                                                    position=(23, 13),
                                                    name="child1A"
                                                ),
                                                value=Symbol(
                                                    position=(23, 21),
                                                    name="grandchild1"
                                                ),
                                                expression_key=false
                                            ),
                                            TreeEntry(
                                                position=(24, 13),
                                                key=Symbol(
                                                    position=(24, 13),
                                                    name="child1B"
                                                ),
                                                value=Symbol(
                                                    position=(24, 21),
                                                    name="grandchild2"
                                                ),
                                                expression_key=false
                                            )
                                        ]
                                    ),
                                    expression_key=false
                                ),
                                TreeEntry(
                                    position=(26, 9),
                                    key=Symbol(
                                        position=(26, 9),
                                        name="parent2"
                                    ),
                                    value=TreeLiteral(
                                        position=(26, 17),
                                        entries=[
                                            TreeEntry(
                                                position=(27, 13),
                                                key=Symbol(
                                                    position=(27, 13),
                                                    name="child2A"
                                                ),
                                                value=Symbol(
                                                    position=(27, 21),
                                                    name="grandchild3"
                                                ),
                                                expression_key=false
                                            ),
                                            TreeEntry(
                                                position=(28, 13),
                                                key=Symbol(
                                                    position=(28, 13),
                                                    name="child2B"
                                                ),
                                                value=Symbol(
                                                    position=(28, 21),
                                                    name="grandchild4"
                                                ),
                                                expression_key=false
                                            )
                                        ]
                                    ),
                                    expression_key=false
                                )
                            ]
                        ),
                        expression_key=false
                    ),
                    TreeEntry(
                        position=(31, 5),
                        key=Symbol(
                            position=(31, 5),
                            name="grandParent2"
                        ),
                        value=TreeLiteral(
                            position=(31, 18),
                            entries=[
                                TreeEntry(
                                    position=(32, 9),
                                    key=Symbol(
                                        position=(32, 9),
                                        name="parent3"
                                    ),
                                    value=TreeLiteral(
                                        position=(32, 17),
                                        entries=[
                                            TreeEntry(
                                                position=(33, 13),
                                                key=Symbol(
                                                    position=(33, 13),
                                                    name="child3A"
                                                ),
                                                value=Symbol(
                                                    position=(33, 21),
                                                    name="grandchild5"
                                                ),
                                                expression_key=false
                                            ),
                                            TreeEntry(
                                                position=(34, 13),
                                                key=Symbol(
                                                    position=(34, 13),
                                                    name="child3B"
                                                ),
                                                value=Symbol(
                                                    position=(34, 21),
                                                    name="grandchild6"
                                                ),
                                                expression_key=false
                                            )
                                        ]
                                    ),
                                    expression_key=false
                                )
                            ]
                        ),
                        expression_key=false
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(39, 1),
            name=Symbol(
                position=(39, 1),
                name="treeComprehension"
            ),
            value=TreeComprehension(
                position=(39, 21),
                entry=TreeEntry(
                    position=(40, 6),
                    key=StringLiteral(
                        position=(40, 6),
                        value="a"
                    ),
                    value=TreeLiteral(
                        position=(40, 11),
                        entries=[
                            TreeEntry(
                                position=(41, 9),
                                key=Symbol(
                                    position=(41, 9),
                                    name="b"
                                ),
                                value=SetLiteral(
                                    position=(41, 11),
                                    elements=[
                                        Symbol(
                                            position=(42, 13),
                                            name="c"
                                        )
                                    ]
                                ),
                                expression_key=false
                            )
                        ]
                    ),
                    expression_key=true
                ),
                clauses=[
                    ComprehensionBinding(
                        position=(45, 5),
                        variables=[
                            Symbol(
                                position=(45, 9),
                                name="a"
                            )
                        ],
                        iterable=Symbol(
                            position=(45, 14),
                            name="someSetA"
                        )
                    ),
                    ComprehensionBinding(
                        position=(46, 5),
                        variables=[
                            Symbol(
                                position=(46, 9),
                                name="b"
                            )
                        ],
                        iterable=Symbol(
                            position=(46, 14),
                            name="someSetB"
                        )
                    ),
                    ComprehensionBinding(
                        position=(47, 5),
                        variables=[
                            Symbol(
                                position=(47, 9),
                                name="c"
                            )
                        ],
                        iterable=Symbol(
                            position=(47, 14),
                            name="someSetC"
                        )
                    )
                ]
            )
        )
    ]
)
*)
