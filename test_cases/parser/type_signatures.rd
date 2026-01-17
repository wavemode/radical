myList : List[String]
myList = [ "a", "b", "c" ]

myMap : Map[String, Int]
myMap = { a = 1, ["b"] = 2, c = 3 }

(*
Module(
    position=(1, 1),
    top_level_nodes=[
        VariableTypeSignature(
            position=(1, 1),
            name=Symbol(
                position=(1, 1),
                name="myList"
            ),
            type=GenericType(
                position=(1, 10),
                base_type=TypeName(
                    position=(1, 10),
                    name=Symbol(
                        position=(1, 10),
                        name="List"
                    )
                ),
                type_arguments=[
                    TypeName(
                        position=(1, 15),
                        name=Symbol(
                            position=(1, 15),
                            name="String"
                        )
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(2, 1),
            name=Symbol(
                position=(2, 1),
                name="myList"
            ),
            value=ListLiteral(
                position=(2, 10),
                elements=[
                    StringLiteral(
                        position=(2, 12),
                        value="a"
                    ),
                    StringLiteral(
                        position=(2, 17),
                        value="b"
                    ),
                    StringLiteral(
                        position=(2, 22),
                        value="c"
                    )
                ]
            )
        ),
        VariableTypeSignature(
            position=(4, 1),
            name=Symbol(
                position=(4, 1),
                name="myMap"
            ),
            type=GenericType(
                position=(4, 9),
                base_type=TypeName(
                    position=(4, 9),
                    name=Symbol(
                        position=(4, 9),
                        name="Map"
                    )
                ),
                type_arguments=[
                    TypeName(
                        position=(4, 13),
                        name=Symbol(
                            position=(4, 13),
                            name="String"
                        )
                    ),
                    TypeName(
                        position=(4, 21),
                        name=Symbol(
                            position=(4, 21),
                            name="Int"
                        )
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(5, 1),
            name=Symbol(
                position=(5, 1),
                name="myMap"
            ),
            value=MapLiteral(
                position=(5, 9),
                entries=[
                    MapEntry(
                        position=(5, 11),
                        key=Symbol(
                            position=(5, 11),
                            name="a"
                        ),
                        value=IntegerLiteral(
                            position=(5, 15),
                            value="1"
                        ),
                        expression_key=false
                    ),
                    MapEntry(
                        position=(5, 19),
                        key=StringLiteral(
                            position=(5, 19),
                            value="b"
                        ),
                        value=IntegerLiteral(
                            position=(5, 26),
                            value="2"
                        ),
                        expression_key=true
                    ),
                    MapEntry(
                        position=(5, 29),
                        key=Symbol(
                            position=(5, 29),
                            name="c"
                        ),
                        value=IntegerLiteral(
                            position=(5, 33),
                            value="3"
                        ),
                        expression_key=false
                    )
                ]
            )
        )
    ]
)
*)
