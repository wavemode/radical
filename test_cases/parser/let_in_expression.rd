value = let
    a : Int
    a = 1
    
    b : Int
    b = 2

    c : List[Int]
    c = [3, 4, 5]
  in
    a + b + c[3]

(*
Module(
    position=(1, 1),
    top_level_nodes=[
        VariableBindingStatement(
            position=(1, 1),
            name=Symbol(
                position=(1, 1),
                name="value",
                quoted=false
            ),
            value=LetIn(
                position=(1, 9),
                bindings=[
                    VariableTypeSignature(
                        position=(2, 5),
                        name=Symbol(
                            position=(2, 5),
                            name="a",
                            quoted=false
                        ),
                        type=TypeName(
                            position=(2, 9),
                            name=Symbol(
                                position=(2, 9),
                                name="Int",
                                quoted=false
                            )
                        )
                    ),
                    VariableBindingStatement(
                        position=(3, 5),
                        name=Symbol(
                            position=(3, 5),
                            name="a",
                            quoted=false
                        ),
                        value=IntegerLiteral(
                            position=(3, 9),
                            value="1"
                        )
                    ),
                    VariableTypeSignature(
                        position=(5, 5),
                        name=Symbol(
                            position=(5, 5),
                            name="b",
                            quoted=false
                        ),
                        type=TypeName(
                            position=(5, 9),
                            name=Symbol(
                                position=(5, 9),
                                name="Int",
                                quoted=false
                            )
                        )
                    ),
                    VariableBindingStatement(
                        position=(6, 5),
                        name=Symbol(
                            position=(6, 5),
                            name="b",
                            quoted=false
                        ),
                        value=IntegerLiteral(
                            position=(6, 9),
                            value="2"
                        )
                    ),
                    VariableTypeSignature(
                        position=(8, 5),
                        name=Symbol(
                            position=(8, 5),
                            name="c",
                            quoted=false
                        ),
                        type=GenericType(
                            position=(8, 9),
                            base_type=TypeName(
                                position=(8, 9),
                                name=Symbol(
                                    position=(8, 9),
                                    name="List",
                                    quoted=false
                                )
                            ),
                            type_arguments=[
                                TypeName(
                                    position=(8, 14),
                                    name=Symbol(
                                        position=(8, 14),
                                        name="Int",
                                        quoted=false
                                    )
                                )
                            ]
                        )
                    ),
                    VariableBindingStatement(
                        position=(9, 5),
                        name=Symbol(
                            position=(9, 5),
                            name="c",
                            quoted=false
                        ),
                        value=ListLiteral(
                            position=(9, 9),
                            elements=[
                                IntegerLiteral(
                                    position=(9, 10),
                                    value="3"
                                ),
                                IntegerLiteral(
                                    position=(9, 13),
                                    value="4"
                                ),
                                IntegerLiteral(
                                    position=(9, 16),
                                    value="5"
                                )
                            ]
                        )
                    )
                ],
                body=BinaryOperation(
                    position=(11, 5),
                    left=BinaryOperation(
                        position=(11, 5),
                        left=Symbol(
                            position=(11, 5),
                            name="a",
                            quoted=false
                        ),
                        operator="+",
                        right=Symbol(
                            position=(11, 9),
                            name="b",
                            quoted=false
                        )
                    ),
                    operator="+",
                    right=IndexAccess(
                        position=(11, 13),
                        collection=Symbol(
                            position=(11, 13),
                            name="c",
                            quoted=false
                        ),
                        index=IntegerLiteral(
                            position=(11, 15),
                            value="3"
                        )
                    )
                )
            )
        )
    ]
)
*)