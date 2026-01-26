intValue : ( Int ) = 5
intTupleValue : (Int,Int,Int) = (1, 2, 3)

listMapAndSetTuple : ( List[String], Map[String, Int], Set[Int] ) = (
    ["a", "b"],
    { key1 = 1, key2 = 2 },
    {1, 2, 3}
)


simpleFunctionType : (Int) -> Int
multipleArgumentsFunctionType : (String, Int, Bool) -> String
namedArgumentsFunctionType : (name: String, age: List[Int]) -> Bool

optionalFunctionArgumentType : (name?: String, age?: Int, active?: Bool) -> Bool
variadicFunctionArgumentType : (...tags: String) -> Int

mixedNamedAndUnnamed : (String, age: Int, Bool) -> String

nestedFunctionType : (
    (f1: (Int, String) -> Bool, f2: (List[Int], Map[String, Int]) -> Set[String])
    -> Map[
        String,
        (arg1: Int, arg2: Int,) -> List[Bool],
    ],
    Null,
)

curriedFunctionType : (Int) -> (String) -> (Bool) -> (Int)

implicitUnnamedArgumentsFunctionType : (&Int, &String) -> Bool
implicitNamedArgumentsFunctionType : (   &    name: String, &    age: List[Int]
    ,   ) -> Bool

(*
Module(
    position=(1, 1),
    top_level_nodes=[
        VariableBindingStatement(
            position=(1, 1),
            name=Symbol(
                position=(1, 1),
                name="intValue",
                quoted=false
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
                        name="Int",
                        quoted=false
                    )
                )
            )
        ),
        VariableBindingStatement(
            position=(2, 1),
            name=Symbol(
                position=(2, 1),
                name="intTupleValue",
                quoted=false
            ),
            value=TupleLiteral(
                position=(2, 33),
                elements=[
                    IntegerLiteral(
                        position=(2, 34),
                        value="1"
                    ),
                    IntegerLiteral(
                        position=(2, 37),
                        value="2"
                    ),
                    IntegerLiteral(
                        position=(2, 40),
                        value="3"
                    )
                ]
            ),
            type=TupleType(
                position=(2, 17),
                element_types=[
                    TypeName(
                        position=(2, 18),
                        name=Symbol(
                            position=(2, 18),
                            name="Int",
                            quoted=false
                        )
                    ),
                    TypeName(
                        position=(2, 22),
                        name=Symbol(
                            position=(2, 22),
                            name="Int",
                            quoted=false
                        )
                    ),
                    TypeName(
                        position=(2, 26),
                        name=Symbol(
                            position=(2, 26),
                            name="Int",
                            quoted=false
                        )
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(4, 1),
            name=Symbol(
                position=(4, 1),
                name="listMapAndSetTuple",
                quoted=false
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
                                    name="key1",
                                    quoted=false
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
                                    name="key2",
                                    quoted=false
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
                                name="List",
                                quoted=false
                            )
                        ),
                        type_arguments=[
                            TypeName(
                                position=(4, 29),
                                name=Symbol(
                                    position=(4, 29),
                                    name="String",
                                    quoted=false
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
                                name="Map",
                                quoted=false
                            )
                        ),
                        type_arguments=[
                            TypeName(
                                position=(4, 42),
                                name=Symbol(
                                    position=(4, 42),
                                    name="String",
                                    quoted=false
                                )
                            ),
                            TypeName(
                                position=(4, 50),
                                name=Symbol(
                                    position=(4, 50),
                                    name="Int",
                                    quoted=false
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
                                name="Set",
                                quoted=false
                            )
                        ),
                        type_arguments=[
                            TypeName(
                                position=(4, 60),
                                name=Symbol(
                                    position=(4, 60),
                                    name="Int",
                                    quoted=false
                                )
                            )
                        ]
                    )
                ]
            )
        ),
        VariableTypeSignature(
            position=(11, 1),
            name=Symbol(
                position=(11, 1),
                name="simpleFunctionType",
                quoted=false
            ),
            type=FunctionType(
                position=(11, 22),
                argument_types=[
                    FunctionArgumentType(
                        position=(11, 23),
                        type=TypeName(
                            position=(11, 23),
                            name=Symbol(
                                position=(11, 23),
                                name="Int",
                                quoted=false
                            )
                        ),
                        variadic=false,
                        optional=false,
                        implicit=false
                    )
                ],
                return_type=TypeName(
                    position=(11, 31),
                    name=Symbol(
                        position=(11, 31),
                        name="Int",
                        quoted=false
                    )
                )
            )
        ),
        VariableTypeSignature(
            position=(12, 1),
            name=Symbol(
                position=(12, 1),
                name="multipleArgumentsFunctionType",
                quoted=false
            ),
            type=FunctionType(
                position=(12, 33),
                argument_types=[
                    FunctionArgumentType(
                        position=(12, 34),
                        type=TypeName(
                            position=(12, 34),
                            name=Symbol(
                                position=(12, 34),
                                name="String",
                                quoted=false
                            )
                        ),
                        variadic=false,
                        optional=false,
                        implicit=false
                    ),
                    FunctionArgumentType(
                        position=(12, 42),
                        type=TypeName(
                            position=(12, 42),
                            name=Symbol(
                                position=(12, 42),
                                name="Int",
                                quoted=false
                            )
                        ),
                        variadic=false,
                        optional=false,
                        implicit=false
                    ),
                    FunctionArgumentType(
                        position=(12, 47),
                        type=TypeName(
                            position=(12, 47),
                            name=Symbol(
                                position=(12, 47),
                                name="Bool",
                                quoted=false
                            )
                        ),
                        variadic=false,
                        optional=false,
                        implicit=false
                    )
                ],
                return_type=TypeName(
                    position=(12, 56),
                    name=Symbol(
                        position=(12, 56),
                        name="String",
                        quoted=false
                    )
                )
            )
        ),
        VariableTypeSignature(
            position=(13, 1),
            name=Symbol(
                position=(13, 1),
                name="namedArgumentsFunctionType",
                quoted=false
            ),
            type=FunctionType(
                position=(13, 30),
                argument_types=[
                    FunctionArgumentType(
                        position=(13, 31),
                        name=Symbol(
                            position=(13, 31),
                            name="name",
                            quoted=false
                        ),
                        type=TypeName(
                            position=(13, 37),
                            name=Symbol(
                                position=(13, 37),
                                name="String",
                                quoted=false
                            )
                        ),
                        variadic=false,
                        optional=false,
                        implicit=false
                    ),
                    FunctionArgumentType(
                        position=(13, 45),
                        name=Symbol(
                            position=(13, 45),
                            name="age",
                            quoted=false
                        ),
                        type=GenericType(
                            position=(13, 50),
                            base_type=TypeName(
                                position=(13, 50),
                                name=Symbol(
                                    position=(13, 50),
                                    name="List",
                                    quoted=false
                                )
                            ),
                            type_arguments=[
                                TypeName(
                                    position=(13, 55),
                                    name=Symbol(
                                        position=(13, 55),
                                        name="Int",
                                        quoted=false
                                    )
                                )
                            ]
                        ),
                        variadic=false,
                        optional=false,
                        implicit=false
                    )
                ],
                return_type=TypeName(
                    position=(13, 64),
                    name=Symbol(
                        position=(13, 64),
                        name="Bool",
                        quoted=false
                    )
                )
            )
        ),
        VariableTypeSignature(
            position=(15, 1),
            name=Symbol(
                position=(15, 1),
                name="optionalFunctionArgumentType",
                quoted=false
            ),
            type=FunctionType(
                position=(15, 32),
                argument_types=[
                    FunctionArgumentType(
                        position=(15, 33),
                        name=Symbol(
                            position=(15, 33),
                            name="name",
                            quoted=false
                        ),
                        type=TypeName(
                            position=(15, 40),
                            name=Symbol(
                                position=(15, 40),
                                name="String",
                                quoted=false
                            )
                        ),
                        variadic=false,
                        optional=true,
                        implicit=false
                    ),
                    FunctionArgumentType(
                        position=(15, 48),
                        name=Symbol(
                            position=(15, 48),
                            name="age",
                            quoted=false
                        ),
                        type=TypeName(
                            position=(15, 54),
                            name=Symbol(
                                position=(15, 54),
                                name="Int",
                                quoted=false
                            )
                        ),
                        variadic=false,
                        optional=true,
                        implicit=false
                    ),
                    FunctionArgumentType(
                        position=(15, 59),
                        name=Symbol(
                            position=(15, 59),
                            name="active",
                            quoted=false
                        ),
                        type=TypeName(
                            position=(15, 68),
                            name=Symbol(
                                position=(15, 68),
                                name="Bool",
                                quoted=false
                            )
                        ),
                        variadic=false,
                        optional=true,
                        implicit=false
                    )
                ],
                return_type=TypeName(
                    position=(15, 77),
                    name=Symbol(
                        position=(15, 77),
                        name="Bool",
                        quoted=false
                    )
                )
            )
        ),
        VariableTypeSignature(
            position=(16, 1),
            name=Symbol(
                position=(16, 1),
                name="variadicFunctionArgumentType",
                quoted=false
            ),
            type=FunctionType(
                position=(16, 32),
                argument_types=[
                    FunctionArgumentType(
                        position=(16, 33),
                        name=Symbol(
                            position=(16, 36),
                            name="tags",
                            quoted=false
                        ),
                        type=TypeName(
                            position=(16, 42),
                            name=Symbol(
                                position=(16, 42),
                                name="String",
                                quoted=false
                            )
                        ),
                        variadic=true,
                        optional=false,
                        implicit=false
                    )
                ],
                return_type=TypeName(
                    position=(16, 53),
                    name=Symbol(
                        position=(16, 53),
                        name="Int",
                        quoted=false
                    )
                )
            )
        ),
        VariableTypeSignature(
            position=(18, 1),
            name=Symbol(
                position=(18, 1),
                name="mixedNamedAndUnnamed",
                quoted=false
            ),
            type=FunctionType(
                position=(18, 24),
                argument_types=[
                    FunctionArgumentType(
                        position=(18, 25),
                        type=TypeName(
                            position=(18, 25),
                            name=Symbol(
                                position=(18, 25),
                                name="String",
                                quoted=false
                            )
                        ),
                        variadic=false,
                        optional=false,
                        implicit=false
                    ),
                    FunctionArgumentType(
                        position=(18, 33),
                        name=Symbol(
                            position=(18, 33),
                            name="age",
                            quoted=false
                        ),
                        type=TypeName(
                            position=(18, 38),
                            name=Symbol(
                                position=(18, 38),
                                name="Int",
                                quoted=false
                            )
                        ),
                        variadic=false,
                        optional=false,
                        implicit=false
                    ),
                    FunctionArgumentType(
                        position=(18, 43),
                        type=TypeName(
                            position=(18, 43),
                            name=Symbol(
                                position=(18, 43),
                                name="Bool",
                                quoted=false
                            )
                        ),
                        variadic=false,
                        optional=false,
                        implicit=false
                    )
                ],
                return_type=TypeName(
                    position=(18, 52),
                    name=Symbol(
                        position=(18, 52),
                        name="String",
                        quoted=false
                    )
                )
            )
        ),
        VariableTypeSignature(
            position=(20, 1),
            name=Symbol(
                position=(20, 1),
                name="nestedFunctionType",
                quoted=false
            ),
            type=TupleType(
                position=(20, 22),
                element_types=[
                    FunctionType(
                        position=(21, 5),
                        argument_types=[
                            FunctionArgumentType(
                                position=(21, 6),
                                name=Symbol(
                                    position=(21, 6),
                                    name="f1",
                                    quoted=false
                                ),
                                type=FunctionType(
                                    position=(21, 10),
                                    argument_types=[
                                        FunctionArgumentType(
                                            position=(21, 11),
                                            type=TypeName(
                                                position=(21, 11),
                                                name=Symbol(
                                                    position=(21, 11),
                                                    name="Int",
                                                    quoted=false
                                                )
                                            ),
                                            variadic=false,
                                            optional=false,
                                            implicit=false
                                        ),
                                        FunctionArgumentType(
                                            position=(21, 16),
                                            type=TypeName(
                                                position=(21, 16),
                                                name=Symbol(
                                                    position=(21, 16),
                                                    name="String",
                                                    quoted=false
                                                )
                                            ),
                                            variadic=false,
                                            optional=false,
                                            implicit=false
                                        )
                                    ],
                                    return_type=TypeName(
                                        position=(21, 27),
                                        name=Symbol(
                                            position=(21, 27),
                                            name="Bool",
                                            quoted=false
                                        )
                                    )
                                ),
                                variadic=false,
                                optional=false,
                                implicit=false
                            ),
                            FunctionArgumentType(
                                position=(21, 33),
                                name=Symbol(
                                    position=(21, 33),
                                    name="f2",
                                    quoted=false
                                ),
                                type=FunctionType(
                                    position=(21, 37),
                                    argument_types=[
                                        FunctionArgumentType(
                                            position=(21, 38),
                                            type=GenericType(
                                                position=(21, 38),
                                                base_type=TypeName(
                                                    position=(21, 38),
                                                    name=Symbol(
                                                        position=(21, 38),
                                                        name="List",
                                                        quoted=false
                                                    )
                                                ),
                                                type_arguments=[
                                                    TypeName(
                                                        position=(21, 43),
                                                        name=Symbol(
                                                            position=(21, 43),
                                                            name="Int",
                                                            quoted=false
                                                        )
                                                    )
                                                ]
                                            ),
                                            variadic=false,
                                            optional=false,
                                            implicit=false
                                        ),
                                        FunctionArgumentType(
                                            position=(21, 49),
                                            type=GenericType(
                                                position=(21, 49),
                                                base_type=TypeName(
                                                    position=(21, 49),
                                                    name=Symbol(
                                                        position=(21, 49),
                                                        name="Map",
                                                        quoted=false
                                                    )
                                                ),
                                                type_arguments=[
                                                    TypeName(
                                                        position=(21, 53),
                                                        name=Symbol(
                                                            position=(21, 53),
                                                            name="String",
                                                            quoted=false
                                                        )
                                                    ),
                                                    TypeName(
                                                        position=(21, 61),
                                                        name=Symbol(
                                                            position=(21, 61),
                                                            name="Int",
                                                            quoted=false
                                                        )
                                                    )
                                                ]
                                            ),
                                            variadic=false,
                                            optional=false,
                                            implicit=false
                                        )
                                    ],
                                    return_type=GenericType(
                                        position=(21, 70),
                                        base_type=TypeName(
                                            position=(21, 70),
                                            name=Symbol(
                                                position=(21, 70),
                                                name="Set",
                                                quoted=false
                                            )
                                        ),
                                        type_arguments=[
                                            TypeName(
                                                position=(21, 74),
                                                name=Symbol(
                                                    position=(21, 74),
                                                    name="String",
                                                    quoted=false
                                                )
                                            )
                                        ]
                                    )
                                ),
                                variadic=false,
                                optional=false,
                                implicit=false
                            )
                        ],
                        return_type=GenericType(
                            position=(22, 8),
                            base_type=TypeName(
                                position=(22, 8),
                                name=Symbol(
                                    position=(22, 8),
                                    name="Map",
                                    quoted=false
                                )
                            ),
                            type_arguments=[
                                TypeName(
                                    position=(23, 9),
                                    name=Symbol(
                                        position=(23, 9),
                                        name="String",
                                        quoted=false
                                    )
                                ),
                                FunctionType(
                                    position=(24, 9),
                                    argument_types=[
                                        FunctionArgumentType(
                                            position=(24, 10),
                                            name=Symbol(
                                                position=(24, 10),
                                                name="arg1",
                                                quoted=false
                                            ),
                                            type=TypeName(
                                                position=(24, 16),
                                                name=Symbol(
                                                    position=(24, 16),
                                                    name="Int",
                                                    quoted=false
                                                )
                                            ),
                                            variadic=false,
                                            optional=false,
                                            implicit=false
                                        ),
                                        FunctionArgumentType(
                                            position=(24, 21),
                                            name=Symbol(
                                                position=(24, 21),
                                                name="arg2",
                                                quoted=false
                                            ),
                                            type=TypeName(
                                                position=(24, 27),
                                                name=Symbol(
                                                    position=(24, 27),
                                                    name="Int",
                                                    quoted=false
                                                )
                                            ),
                                            variadic=false,
                                            optional=false,
                                            implicit=false
                                        )
                                    ],
                                    return_type=GenericType(
                                        position=(24, 36),
                                        base_type=TypeName(
                                            position=(24, 36),
                                            name=Symbol(
                                                position=(24, 36),
                                                name="List",
                                                quoted=false
                                            )
                                        ),
                                        type_arguments=[
                                            TypeName(
                                                position=(24, 41),
                                                name=Symbol(
                                                    position=(24, 41),
                                                    name="Bool",
                                                    quoted=false
                                                )
                                            )
                                        ]
                                    )
                                )
                            ]
                        )
                    ),
                    TypeName(
                        position=(26, 5),
                        name=Symbol(
                            position=(26, 5),
                            name="Null",
                            quoted=false
                        )
                    )
                ]
            )
        ),
        VariableTypeSignature(
            position=(29, 1),
            name=Symbol(
                position=(29, 1),
                name="curriedFunctionType",
                quoted=false
            ),
            type=FunctionType(
                position=(29, 23),
                argument_types=[
                    FunctionArgumentType(
                        position=(29, 24),
                        type=TypeName(
                            position=(29, 24),
                            name=Symbol(
                                position=(29, 24),
                                name="Int",
                                quoted=false
                            )
                        ),
                        variadic=false,
                        optional=false,
                        implicit=false
                    )
                ],
                return_type=FunctionType(
                    position=(29, 32),
                    argument_types=[
                        FunctionArgumentType(
                            position=(29, 33),
                            type=TypeName(
                                position=(29, 33),
                                name=Symbol(
                                    position=(29, 33),
                                    name="String",
                                    quoted=false
                                )
                            ),
                            variadic=false,
                            optional=false,
                            implicit=false
                        )
                    ],
                    return_type=FunctionType(
                        position=(29, 44),
                        argument_types=[
                            FunctionArgumentType(
                                position=(29, 45),
                                type=TypeName(
                                    position=(29, 45),
                                    name=Symbol(
                                        position=(29, 45),
                                        name="Bool",
                                        quoted=false
                                    )
                                ),
                                variadic=false,
                                optional=false,
                                implicit=false
                            )
                        ],
                        return_type=ParenthesizedType(
                            position=(29, 54),
                            type=TypeName(
                                position=(29, 55),
                                name=Symbol(
                                    position=(29, 55),
                                    name="Int",
                                    quoted=false
                                )
                            )
                        )
                    )
                )
            )
        ),
        VariableTypeSignature(
            position=(31, 1),
            name=Symbol(
                position=(31, 1),
                name="implicitUnnamedArgumentsFunctionType",
                quoted=false
            ),
            type=FunctionType(
                position=(31, 40),
                argument_types=[
                    FunctionArgumentType(
                        position=(31, 41),
                        type=TypeName(
                            position=(31, 42),
                            name=Symbol(
                                position=(31, 42),
                                name="Int",
                                quoted=false
                            )
                        ),
                        variadic=false,
                        optional=false,
                        implicit=true
                    ),
                    FunctionArgumentType(
                        position=(31, 47),
                        type=TypeName(
                            position=(31, 48),
                            name=Symbol(
                                position=(31, 48),
                                name="String",
                                quoted=false
                            )
                        ),
                        variadic=false,
                        optional=false,
                        implicit=true
                    )
                ],
                return_type=TypeName(
                    position=(31, 59),
                    name=Symbol(
                        position=(31, 59),
                        name="Bool",
                        quoted=false
                    )
                )
            )
        ),
        VariableTypeSignature(
            position=(32, 1),
            name=Symbol(
                position=(32, 1),
                name="implicitNamedArgumentsFunctionType",
                quoted=false
            ),
            type=FunctionType(
                position=(32, 38),
                argument_types=[
                    FunctionArgumentType(
                        position=(32, 42),
                        name=Symbol(
                            position=(32, 47),
                            name="name",
                            quoted=false
                        ),
                        type=TypeName(
                            position=(32, 53),
                            name=Symbol(
                                position=(32, 53),
                                name="String",
                                quoted=false
                            )
                        ),
                        variadic=false,
                        optional=false,
                        implicit=true
                    ),
                    FunctionArgumentType(
                        position=(32, 61),
                        name=Symbol(
                            position=(32, 66),
                            name="age",
                            quoted=false
                        ),
                        type=GenericType(
                            position=(32, 71),
                            base_type=TypeName(
                                position=(32, 71),
                                name=Symbol(
                                    position=(32, 71),
                                    name="List",
                                    quoted=false
                                )
                            ),
                            type_arguments=[
                                TypeName(
                                    position=(32, 76),
                                    name=Symbol(
                                        position=(32, 76),
                                        name="Int",
                                        quoted=false
                                    )
                                )
                            ]
                        ),
                        variadic=false,
                        optional=false,
                        implicit=true
                    )
                ],
                return_type=TypeName(
                    position=(33, 14),
                    name=Symbol(
                        position=(33, 14),
                        name="Bool",
                        quoted=false
                    )
                )
            )
        )
    ]
)
*)