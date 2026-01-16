a : List[Int]
    | Map[String, Int]
    | Set[Int] = { a = 1 }

(*
Module(
    position=(1, 1),
    top_level_nodes=[
        VariableBindingStatement(
            position=(1, 1),
            name=Symbol(
                position=(1, 1),
                name="a"
            ),
            value=MapLiteral(
                position=(3, 18),
                entries=[
                    MapEntry(
                        position=(3, 20),
                        key=Symbol(
                            position=(3, 20),
                            name="a"
                        ),
                        value=IntegerLiteral(
                            position=(3, 24),
                            value="1"
                        ),
                        expression_key=false
                    )
                ]
            ),
            type=UnionType(
                position=(3, 5),
                left=UnionType(
                    position=(2, 5),
                    left=GenericType(
                        position=(1, 5),
                        base_type=TypeName(
                            position=(1, 5),
                            name=Symbol(
                                position=(1, 5),
                                name="List"
                            )
                        ),
                        type_arguments=[
                            TypeName(
                                position=(1, 10),
                                name=Symbol(
                                    position=(1, 10),
                                    name="Int"
                                )
                            )
                        ]
                    ),
                    right=GenericType(
                        position=(2, 7),
                        base_type=TypeName(
                            position=(2, 7),
                            name=Symbol(
                                position=(2, 7),
                                name="Map"
                            )
                        ),
                        type_arguments=[
                            TypeName(
                                position=(2, 11),
                                name=Symbol(
                                    position=(2, 11),
                                    name="String"
                                )
                            ),
                            TypeName(
                                position=(2, 19),
                                name=Symbol(
                                    position=(2, 19),
                                    name="Int"
                                )
                            )
                        ]
                    )
                ),
                right=GenericType(
                    position=(3, 7),
                    base_type=TypeName(
                        position=(3, 7),
                        name=Symbol(
                            position=(3, 7),
                            name="Set"
                        )
                    ),
                    type_arguments=[
                        TypeName(
                            position=(3, 11),
                            name=Symbol(
                                position=(3, 11),
                                name="Int"
                            )
                        )
                    ]
                )
            )
        )
    ]
)
*)
