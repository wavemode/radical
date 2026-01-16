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
    top_level_nodes=[
        VariableBindingStatement(
            name=Symbol(
                name="singleEntryTree"
            ),
            value=TreeLiteral(
                entries=[
                    TreeEntry(
                        key=Symbol(
                            name="a"
                        ),
                        value=Symbol(
                            name="b"
                        ),
                        expression_key=false
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
                    TreeEntry(
                        key=Symbol(
                            name="rootLeft"
                        ),
                        value=Symbol(
                            name="childLeft1"
                        ),
                        expression_key=false
                    ),
                    TreeEntry(
                        key=Symbol(
                            name="rootLeft"
                        ),
                        value=Symbol(
                            name="childLeft2"
                        ),
                        expression_key=false
                    ),
                    TreeEntry(
                        key=Symbol(
                            name="rootRight"
                        ),
                        value=Symbol(
                            name="childRight1"
                        ),
                        expression_key=false
                    ),
                    TreeEntry(
                        key=Symbol(
                            name="rootRight"
                        ),
                        value=Symbol(
                            name="childRight2"
                        ),
                        expression_key=false
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
                    TreeEntry(
                        key=Symbol(
                            name="parent1"
                        ),
                        value=TreeLiteral(
                            entries=[
                                TreeEntry(
                                    key=Symbol(
                                        name="child1A"
                                    ),
                                    value=Symbol(
                                        name="grandchild1"
                                    ),
                                    expression_key=false
                                ),
                                TreeEntry(
                                    key=Symbol(
                                        name="child1B"
                                    ),
                                    value=Symbol(
                                        name="grandchild2"
                                    ),
                                    expression_key=false
                                )
                            ]
                        ),
                        expression_key=false
                    ),
                    TreeEntry(
                        key=Symbol(
                            name="parent2"
                        ),
                        value=TreeLiteral(
                            entries=[
                                TreeEntry(
                                    key=Symbol(
                                        name="child2A"
                                    ),
                                    value=Symbol(
                                        name="grandchild3"
                                    ),
                                    expression_key=false
                                ),
                                TreeEntry(
                                    key=Symbol(
                                        name="child2B"
                                    ),
                                    value=Symbol(
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
            name=Symbol(
                name="tripleNestedTreeNoCommas"
            ),
            value=TreeLiteral(
                entries=[
                    TreeEntry(
                        key=Symbol(
                            name="grandParent1"
                        ),
                        value=TreeLiteral(
                            entries=[
                                TreeEntry(
                                    key=Symbol(
                                        name="parent1"
                                    ),
                                    value=TreeLiteral(
                                        entries=[
                                            TreeEntry(
                                                key=Symbol(
                                                    name="child1A"
                                                ),
                                                value=Symbol(
                                                    name="grandchild1"
                                                ),
                                                expression_key=false
                                            ),
                                            TreeEntry(
                                                key=Symbol(
                                                    name="child1B"
                                                ),
                                                value=Symbol(
                                                    name="grandchild2"
                                                ),
                                                expression_key=false
                                            )
                                        ]
                                    ),
                                    expression_key=false
                                ),
                                TreeEntry(
                                    key=Symbol(
                                        name="parent2"
                                    ),
                                    value=TreeLiteral(
                                        entries=[
                                            TreeEntry(
                                                key=Symbol(
                                                    name="child2A"
                                                ),
                                                value=Symbol(
                                                    name="grandchild3"
                                                ),
                                                expression_key=false
                                            ),
                                            TreeEntry(
                                                key=Symbol(
                                                    name="child2B"
                                                ),
                                                value=Symbol(
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
                        key=Symbol(
                            name="grandParent2"
                        ),
                        value=TreeLiteral(
                            entries=[
                                TreeEntry(
                                    key=Symbol(
                                        name="parent3"
                                    ),
                                    value=TreeLiteral(
                                        entries=[
                                            TreeEntry(
                                                key=Symbol(
                                                    name="child3A"
                                                ),
                                                value=Symbol(
                                                    name="grandchild5"
                                                ),
                                                expression_key=false
                                            ),
                                            TreeEntry(
                                                key=Symbol(
                                                    name="child3B"
                                                ),
                                                value=Symbol(
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
            name=Symbol(
                name="treeComprehension"
            ),
            value=TreeComprehension(
                entry=TreeEntry(
                    key=StringLiteral(
                        value="a"
                    ),
                    value=TreeLiteral(
                        entries=[
                            TreeEntry(
                                key=Symbol(
                                    name="b"
                                ),
                                value=SetLiteral(
                                    elements=[
                                        Symbol(
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
                        variables=[
                            Symbol(
                                name="a"
                            )
                        ],
                        iterable=Symbol(
                            name="someSetA"
                        )
                    ),
                    ComprehensionBinding(
                        variables=[
                            Symbol(
                                name="b"
                            )
                        ],
                        iterable=Symbol(
                            name="someSetB"
                        )
                    ),
                    ComprehensionBinding(
                        variables=[
                            Symbol(
                                name="c"
                            )
                        ],
                        iterable=Symbol(
                            name="someSetC"
                        )
                    )
                ]
            )
        )
    ]
)
*)
