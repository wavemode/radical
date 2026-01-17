myList : List[Int] = [1, 2, 3]
myMap : Map[String, Int] = { a = 1, b = 2, c = 3 }
myTree : Tree[String, Int] = { a 1, b 2, c 3 }

(*
Module(
    position=(1, 1),
    top_level_nodes=[
        VariableBindingStatement(
            position=(1, 1),
            name=Symbol(
                position=(1, 1),
                name="myList",
                quoted=false
            ),
            value=ListLiteral(
                position=(1, 22),
                elements=[
                    IntegerLiteral(
                        position=(1, 23),
                        value="1"
                    ),
                    IntegerLiteral(
                        position=(1, 26),
                        value="2"
                    ),
                    IntegerLiteral(
                        position=(1, 29),
                        value="3"
                    )
                ]
            ),
            type=GenericType(
                position=(1, 10),
                base_type=TypeName(
                    position=(1, 10),
                    name=Symbol(
                        position=(1, 10),
                        name="List",
                        quoted=false
                    )
                ),
                type_arguments=[
                    TypeName(
                        position=(1, 15),
                        name=Symbol(
                            position=(1, 15),
                            name="Int",
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
                name="myMap",
                quoted=false
            ),
            value=MapLiteral(
                position=(2, 28),
                entries=[
                    MapEntry(
                        position=(2, 30),
                        key=Symbol(
                            position=(2, 30),
                            name="a",
                            quoted=false
                        ),
                        value=IntegerLiteral(
                            position=(2, 34),
                            value="1"
                        ),
                        expression_key=false
                    ),
                    MapEntry(
                        position=(2, 37),
                        key=Symbol(
                            position=(2, 37),
                            name="b",
                            quoted=false
                        ),
                        value=IntegerLiteral(
                            position=(2, 41),
                            value="2"
                        ),
                        expression_key=false
                    ),
                    MapEntry(
                        position=(2, 44),
                        key=Symbol(
                            position=(2, 44),
                            name="c",
                            quoted=false
                        ),
                        value=IntegerLiteral(
                            position=(2, 48),
                            value="3"
                        ),
                        expression_key=false
                    )
                ]
            ),
            type=GenericType(
                position=(2, 9),
                base_type=TypeName(
                    position=(2, 9),
                    name=Symbol(
                        position=(2, 9),
                        name="Map",
                        quoted=false
                    )
                ),
                type_arguments=[
                    TypeName(
                        position=(2, 13),
                        name=Symbol(
                            position=(2, 13),
                            name="String",
                            quoted=false
                        )
                    ),
                    TypeName(
                        position=(2, 21),
                        name=Symbol(
                            position=(2, 21),
                            name="Int",
                            quoted=false
                        )
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(3, 1),
            name=Symbol(
                position=(3, 1),
                name="myTree",
                quoted=false
            ),
            value=TreeLiteral(
                position=(3, 30),
                entries=[
                    TreeEntry(
                        position=(3, 32),
                        key=Symbol(
                            position=(3, 32),
                            name="a",
                            quoted=false
                        ),
                        value=IntegerLiteral(
                            position=(3, 34),
                            value="1"
                        ),
                        expression_key=false
                    ),
                    TreeEntry(
                        position=(3, 37),
                        key=Symbol(
                            position=(3, 37),
                            name="b",
                            quoted=false
                        ),
                        value=IntegerLiteral(
                            position=(3, 39),
                            value="2"
                        ),
                        expression_key=false
                    ),
                    TreeEntry(
                        position=(3, 42),
                        key=Symbol(
                            position=(3, 42),
                            name="c",
                            quoted=false
                        ),
                        value=IntegerLiteral(
                            position=(3, 44),
                            value="3"
                        ),
                        expression_key=false
                    )
                ]
            ),
            type=GenericType(
                position=(3, 10),
                base_type=TypeName(
                    position=(3, 10),
                    name=Symbol(
                        position=(3, 10),
                        name="Tree",
                        quoted=false
                    )
                ),
                type_arguments=[
                    TypeName(
                        position=(3, 15),
                        name=Symbol(
                            position=(3, 15),
                            name="String",
                            quoted=false
                        )
                    ),
                    TypeName(
                        position=(3, 23),
                        name=Symbol(
                            position=(3, 23),
                            name="Int",
                            quoted=false
                        )
                    )
                ]
            )
        )
    ]
)
*)