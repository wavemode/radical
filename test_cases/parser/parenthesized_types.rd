intValue : ( Int ) = 5
intTupleValue : ( Int, Int, Int ) = (1, 2, 3)

listMapAndSetTuple : ( List[String], Map[String, Int], Set[Int] ) = (
    ["a", "b"],
    { key1 = 1, key2 = 2 },
    {1, 2, 3}
)

(*
Module(
    position=(1, 1),
    top_level_nodes=[
        VariableBindingStatement(
            position=(1, 1),
            name=Symbol(
                position=(1, 1),
                name="intValue"
            ),
            value=IntegerLiteral(
                position=(1, 22),
                value="5"
            ),
            type=ParenthesizedType(
                position=(1, 12),
                type=TypeName(
                    position=(1, 14),
                    name=Symbol(
                        position=(1, 14),
                        name="Int"
                    )
                )
            )
        ),
        VariableBindingStatement(
            position=(2, 1),
            name=Symbol(
                position=(2, 1),
                name="intTupleValue"
            ),
            value=TupleLiteral(
                position=(2, 37),
                elements=[
                    IntegerLiteral(
                        position=(2, 38),
                        value="1"
                    ),
                    IntegerLiteral(
                        position=(2, 41),
                        value="2"
                    ),
                    IntegerLiteral(
                        position=(2, 44),
                        value="3"
                    )
                ]
            ),
            type=TupleType(
                position=(2, 17),
                element_types=[
                    TypeName(
                        position=(2, 19),
                        name=Symbol(
                            position=(2, 19),
                            name="Int"
                        )
                    ),
                    TypeName(
                        position=(2, 24),
                        name=Symbol(
                            position=(2, 24),
                            name="Int"
                        )
                    ),
                    TypeName(
                        position=(2, 29),
                        name=Symbol(
                            position=(2, 29),
                            name="Int"
                        )
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(4, 1),
            name=Symbol(
                position=(4, 1),
                name="listMapAndSetTuple"
            ),
            value=TupleLiteral(
                position=(4, 69),
                elements=[
                    ListLiteral(
                        position=(5, 5),
                        elements=[
                            StringLiteral(
                                position=(5, 6),
                                value="a"
                            ),
                            StringLiteral(
                                position=(5, 11),
                                value="b"
                            )
                        ]
                    ),
                    MapLiteral(
                        position=(6, 5),
                        entries=[
                            MapEntry(
                                position=(6, 7),
                                key=Symbol(
                                    position=(6, 7),
                                    name="key1"
                                ),
                                value=IntegerLiteral(
                                    position=(6, 14),
                                    value="1"
                                ),
                                expression_key=false
                            ),
                            MapEntry(
                                position=(6, 17),
                                key=Symbol(
                                    position=(6, 17),
                                    name="key2"
                                ),
                                value=IntegerLiteral(
                                    position=(6, 24),
                                    value="2"
                                ),
                                expression_key=false
                            )
                        ]
                    ),
                    SetLiteral(
                        position=(7, 5),
                        elements=[
                            IntegerLiteral(
                                position=(7, 6),
                                value="1"
                            ),
                            IntegerLiteral(
                                position=(7, 9),
                                value="2"
                            ),
                            IntegerLiteral(
                                position=(7, 12),
                                value="3"
                            )
                        ]
                    )
                ]
            ),
            type=TupleType(
                position=(4, 22),
                element_types=[
                    GenericType(
                        position=(4, 24),
                        base_type=TypeName(
                            position=(4, 24),
                            name=Symbol(
                                position=(4, 24),
                                name="List"
                            )
                        ),
                        type_arguments=[
                            TypeName(
                                position=(4, 29),
                                name=Symbol(
                                    position=(4, 29),
                                    name="String"
                                )
                            )
                        ]
                    ),
                    GenericType(
                        position=(4, 38),
                        base_type=TypeName(
                            position=(4, 38),
                            name=Symbol(
                                position=(4, 38),
                                name="Map"
                            )
                        ),
                        type_arguments=[
                            TypeName(
                                position=(4, 42),
                                name=Symbol(
                                    position=(4, 42),
                                    name="String"
                                )
                            ),
                            TypeName(
                                position=(4, 50),
                                name=Symbol(
                                    position=(4, 50),
                                    name="Int"
                                )
                            )
                        ]
                    ),
                    GenericType(
                        position=(4, 56),
                        base_type=TypeName(
                            position=(4, 56),
                            name=Symbol(
                                position=(4, 56),
                                name="Set"
                            )
                        ),
                        type_arguments=[
                            TypeName(
                                position=(4, 60),
                                name=Symbol(
                                    position=(4, 60),
                                    name="Int"
                                )
                            )
                        ]
                    )
                ]
            )
        )
    ]
)
*)