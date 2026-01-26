noArgs = func(    )
singleArg = func(42)
singleArgTrailingComma = func(
    42,
)

multipleArgs = func(1, 2, 3)
nestedFunctionCalls = outerFunc(innerFunc1(10), innerFunc2(20, 30))

methodCall = obj.method(100, "test")
chainedMethodCalls = obj.firstMethod().secondMethod(200).thirdMethod("chain")

namedArgs = func(arg1=10, arg2="hello", arg3=true)
mixedArgs = func(5, arg1="value", 10, arg2="another")

callOfCallOfCall = func1()(func2())(func3()(100))

(*
Module(
    position=(1, 1),
    top_level_nodes=[
        VariableBindingStatement(
            position=(1, 1),
            name=Symbol(
                position=(1, 1),
                name="noArgs",
                quoted=false
            ),
            value=FunctionCall(
                position=(1, 10),
                function=Symbol(
                    position=(1, 10),
                    name="func",
                    quoted=false
                ),
                arguments=[

                ]
            )
        ),
        VariableBindingStatement(
            position=(2, 1),
            name=Symbol(
                position=(2, 1),
                name="singleArg",
                quoted=false
            ),
            value=FunctionCall(
                position=(2, 13),
                function=Symbol(
                    position=(2, 13),
                    name="func",
                    quoted=false
                ),
                arguments=[
                    FunctionCallArgument(
                        position=(2, 18),
                        value=IntegerLiteral(
                            position=(2, 18),
                            value="42"
                        )
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(3, 1),
            name=Symbol(
                position=(3, 1),
                name="singleArgTrailingComma",
                quoted=false
            ),
            value=FunctionCall(
                position=(3, 26),
                function=Symbol(
                    position=(3, 26),
                    name="func",
                    quoted=false
                ),
                arguments=[
                    FunctionCallArgument(
                        position=(4, 5),
                        value=IntegerLiteral(
                            position=(4, 5),
                            value="42"
                        )
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(7, 1),
            name=Symbol(
                position=(7, 1),
                name="multipleArgs",
                quoted=false
            ),
            value=FunctionCall(
                position=(7, 16),
                function=Symbol(
                    position=(7, 16),
                    name="func",
                    quoted=false
                ),
                arguments=[
                    FunctionCallArgument(
                        position=(7, 21),
                        value=IntegerLiteral(
                            position=(7, 21),
                            value="1"
                        )
                    ),
                    FunctionCallArgument(
                        position=(7, 24),
                        value=IntegerLiteral(
                            position=(7, 24),
                            value="2"
                        )
                    ),
                    FunctionCallArgument(
                        position=(7, 27),
                        value=IntegerLiteral(
                            position=(7, 27),
                            value="3"
                        )
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(8, 1),
            name=Symbol(
                position=(8, 1),
                name="nestedFunctionCalls",
                quoted=false
            ),
            value=FunctionCall(
                position=(8, 23),
                function=Symbol(
                    position=(8, 23),
                    name="outerFunc",
                    quoted=false
                ),
                arguments=[
                    FunctionCallArgument(
                        position=(8, 33),
                        value=FunctionCall(
                            position=(8, 33),
                            function=Symbol(
                                position=(8, 33),
                                name="innerFunc1",
                                quoted=false
                            ),
                            arguments=[
                                FunctionCallArgument(
                                    position=(8, 44),
                                    value=IntegerLiteral(
                                        position=(8, 44),
                                        value="10"
                                    )
                                )
                            ]
                        )
                    ),
                    FunctionCallArgument(
                        position=(8, 49),
                        value=FunctionCall(
                            position=(8, 49),
                            function=Symbol(
                                position=(8, 49),
                                name="innerFunc2",
                                quoted=false
                            ),
                            arguments=[
                                FunctionCallArgument(
                                    position=(8, 60),
                                    value=IntegerLiteral(
                                        position=(8, 60),
                                        value="20"
                                    )
                                ),
                                FunctionCallArgument(
                                    position=(8, 64),
                                    value=IntegerLiteral(
                                        position=(8, 64),
                                        value="30"
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(10, 1),
            name=Symbol(
                position=(10, 1),
                name="methodCall",
                quoted=false
            ),
            value=FunctionCall(
                position=(10, 14),
                function=AttributeAccess(
                    position=(10, 14),
                    object=Symbol(
                        position=(10, 14),
                        name="obj",
                        quoted=false
                    ),
                    attribute=Symbol(
                        position=(10, 18),
                        name="method",
                        quoted=false
                    )
                ),
                arguments=[
                    FunctionCallArgument(
                        position=(10, 25),
                        value=IntegerLiteral(
                            position=(10, 25),
                            value="100"
                        )
                    ),
                    FunctionCallArgument(
                        position=(10, 30),
                        value=StringLiteral(
                            position=(10, 30),
                            value="test"
                        )
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(11, 1),
            name=Symbol(
                position=(11, 1),
                name="chainedMethodCalls",
                quoted=false
            ),
            value=FunctionCall(
                position=(11, 22),
                function=AttributeAccess(
                    position=(11, 22),
                    object=FunctionCall(
                        position=(11, 22),
                        function=AttributeAccess(
                            position=(11, 22),
                            object=FunctionCall(
                                position=(11, 22),
                                function=AttributeAccess(
                                    position=(11, 22),
                                    object=Symbol(
                                        position=(11, 22),
                                        name="obj",
                                        quoted=false
                                    ),
                                    attribute=Symbol(
                                        position=(11, 26),
                                        name="firstMethod",
                                        quoted=false
                                    )
                                ),
                                arguments=[

                                ]
                            ),
                            attribute=Symbol(
                                position=(11, 40),
                                name="secondMethod",
                                quoted=false
                            )
                        ),
                        arguments=[
                            FunctionCallArgument(
                                position=(11, 53),
                                value=IntegerLiteral(
                                    position=(11, 53),
                                    value="200"
                                )
                            )
                        ]
                    ),
                    attribute=Symbol(
                        position=(11, 58),
                        name="thirdMethod",
                        quoted=false
                    )
                ),
                arguments=[
                    FunctionCallArgument(
                        position=(11, 70),
                        value=StringLiteral(
                            position=(11, 70),
                            value="chain"
                        )
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(13, 1),
            name=Symbol(
                position=(13, 1),
                name="namedArgs",
                quoted=false
            ),
            value=FunctionCall(
                position=(13, 13),
                function=Symbol(
                    position=(13, 13),
                    name="func",
                    quoted=false
                ),
                arguments=[
                    FunctionCallArgument(
                        position=(13, 18),
                        name=Symbol(
                            position=(13, 18),
                            name="arg1",
                            quoted=false
                        ),
                        value=IntegerLiteral(
                            position=(13, 23),
                            value="10"
                        )
                    ),
                    FunctionCallArgument(
                        position=(13, 27),
                        name=Symbol(
                            position=(13, 27),
                            name="arg2",
                            quoted=false
                        ),
                        value=StringLiteral(
                            position=(13, 32),
                            value="hello"
                        )
                    ),
                    FunctionCallArgument(
                        position=(13, 41),
                        name=Symbol(
                            position=(13, 41),
                            name="arg3",
                            quoted=false
                        ),
                        value=TrueKeyword(
                            position=(13, 46)
                        )
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(14, 1),
            name=Symbol(
                position=(14, 1),
                name="mixedArgs",
                quoted=false
            ),
            value=FunctionCall(
                position=(14, 13),
                function=Symbol(
                    position=(14, 13),
                    name="func",
                    quoted=false
                ),
                arguments=[
                    FunctionCallArgument(
                        position=(14, 18),
                        value=IntegerLiteral(
                            position=(14, 18),
                            value="5"
                        )
                    ),
                    FunctionCallArgument(
                        position=(14, 21),
                        name=Symbol(
                            position=(14, 21),
                            name="arg1",
                            quoted=false
                        ),
                        value=StringLiteral(
                            position=(14, 26),
                            value="value"
                        )
                    ),
                    FunctionCallArgument(
                        position=(14, 35),
                        value=IntegerLiteral(
                            position=(14, 35),
                            value="10"
                        )
                    ),
                    FunctionCallArgument(
                        position=(14, 39),
                        name=Symbol(
                            position=(14, 39),
                            name="arg2",
                            quoted=false
                        ),
                        value=StringLiteral(
                            position=(14, 44),
                            value="another"
                        )
                    )
                ]
            )
        ),
        VariableBindingStatement(
            position=(16, 1),
            name=Symbol(
                position=(16, 1),
                name="callOfCallOfCall",
                quoted=false
            ),
            value=FunctionCall(
                position=(16, 20),
                function=FunctionCall(
                    position=(16, 20),
                    function=FunctionCall(
                        position=(16, 20),
                        function=Symbol(
                            position=(16, 20),
                            name="func1",
                            quoted=false
                        ),
                        arguments=[

                        ]
                    ),
                    arguments=[
                        FunctionCallArgument(
                            position=(16, 28),
                            value=FunctionCall(
                                position=(16, 28),
                                function=Symbol(
                                    position=(16, 28),
                                    name="func2",
                                    quoted=false
                                ),
                                arguments=[

                                ]
                            )
                        )
                    ]
                ),
                arguments=[
                    FunctionCallArgument(
                        position=(16, 37),
                        value=FunctionCall(
                            position=(16, 37),
                            function=FunctionCall(
                                position=(16, 37),
                                function=Symbol(
                                    position=(16, 37),
                                    name="func3",
                                    quoted=false
                                ),
                                arguments=[

                                ]
                            ),
                            arguments=[
                                FunctionCallArgument(
                                    position=(16, 45),
                                    value=IntegerLiteral(
                                        position=(16, 45),
                                        value="100"
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )
    ]
)
*)
