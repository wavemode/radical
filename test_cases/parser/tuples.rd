singleElementTuple = (element,)
multiElementTuple = (element1, element2, element3)
multiElementTupleWithTrailingComma = (
    element1, 
    element2, 
    element3,
)
nestedTuples = ((element1, element2), (element3, element4), (element5,))

(*
Module(
    position=(1, 1),
    top_level_nodes=[
        VariableBindingStatement(
            position=(1, 1),
            name=Symbol(
                position=(1, 1),
                name="singleElementTuple"
            ),
            value=TupleLiteral(
                position=(1, 22),
                elements=[
                    Symbol(
                        position=(1, 23),
                        name="element"
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(2, 1),
            name=Symbol(
                position=(2, 1),
                name="multiElementTuple"
            ),
            value=TupleLiteral(
                position=(2, 21),
                elements=[
                    Symbol(
                        position=(2, 22),
                        name="element1"
                    ),
                    Symbol(
                        position=(2, 32),
                        name="element2"
                    ),
                    Symbol(
                        position=(2, 42),
                        name="element3"
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(3, 1),
            name=Symbol(
                position=(3, 1),
                name="multiElementTupleWithTrailingComma"
            ),
            value=TupleLiteral(
                position=(3, 38),
                elements=[
                    Symbol(
                        position=(4, 5),
                        name="element1"
                    ),
                    Symbol(
                        position=(5, 5),
                        name="element2"
                    ),
                    Symbol(
                        position=(6, 5),
                        name="element3"
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(8, 1),
            name=Symbol(
                position=(8, 1),
                name="nestedTuples"
            ),
            value=TupleLiteral(
                position=(8, 16),
                elements=[
                    TupleLiteral(
                        position=(8, 17),
                        elements=[
                            Symbol(
                                position=(8, 18),
                                name="element1"
                            ),
                            Symbol(
                                position=(8, 28),
                                name="element2"
                            )
                        ]
                    ),
                    TupleLiteral(
                        position=(8, 39),
                        elements=[
                            Symbol(
                                position=(8, 40),
                                name="element3"
                            ),
                            Symbol(
                                position=(8, 50),
                                name="element4"
                            )
                        ]
                    ),
                    TupleLiteral(
                        position=(8, 61),
                        elements=[
                            Symbol(
                                position=(8, 62),
                                name="element5"
                            )
                        ]
                    )
                ]
            )
        )
    ]
)
*)
