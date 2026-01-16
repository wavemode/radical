singleAttributeAccess = obj.attribute
chainedAttributeAccess = obj.first.second.third

(*
Module(
    position=(1, 1),
    top_level_nodes=[
        VariableBindingStatement(
            position=(1, 1),
            name=Symbol(
                position=(1, 1),
                name="singleAttributeAccess"
            ),
            value=AttributeAccess(
                position=(1, 25),
                object=Symbol(
                    position=(1, 25),
                    name="obj"
                ),
                attribute=Symbol(
                    position=(1, 29),
                    name="attribute"
                )
            )
        ),
        VariableBindingStatement(
            position=(2, 1),
            name=Symbol(
                position=(2, 1),
                name="chainedAttributeAccess"
            ),
            value=AttributeAccess(
                position=(2, 26),
                object=AttributeAccess(
                    position=(2, 26),
                    object=AttributeAccess(
                        position=(2, 26),
                        object=Symbol(
                            position=(2, 26),
                            name="obj"
                        ),
                        attribute=Symbol(
                            position=(2, 30),
                            name="first"
                        )
                    ),
                    attribute=Symbol(
                        position=(2, 36),
                        name="second"
                    )
                ),
                attribute=Symbol(
                    position=(2, 43),
                    name="third"
                )
            )
        )
    ]
)
*)
