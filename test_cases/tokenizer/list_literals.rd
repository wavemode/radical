emptyList = [    ]
singleElementList = [42]
singleElementListWithTrailingComma = [
    3.14, 
]
listLiteralRetrieval = [
    10
    , 20
    , 30
][1]
listWithoutCommas = [
    1
    2
    3
    4
    5
]

multiElementList = [
    "apple",
    "banana",
    "cherry",
]
nestedLists = [
    [1, 2, 3],
    [4, 5, 6],
]
listWithExpressions = [
    1 + 2,
    3 * 4,
    5 - 6 * (8 / 2),
    8 + matrix[0][1] - vector.x,
]


(*
Token(type=SYMBOL, value="emptyList", position=(1, 1, 0))
Token(type=ASSIGN, value="=", position=(1, 11, 0))
Token(type=LIST_START, value="[", position=(1, 13, 0))
Token(type=LIST_END, value="]", position=(1, 18, 0))
Token(type=SYMBOL, value="singleElementList", position=(2, 1, 0))
Token(type=ASSIGN, value="=", position=(2, 19, 0))
Token(type=LIST_START, value="[", position=(2, 21, 0))
Token(type=INTEGER_LITERAL, value="42", position=(2, 22, 0))
Token(type=LIST_END, value="]", position=(2, 24, 0))
Token(type=SYMBOL, value="singleElementListWithTrailingComma", position=(3, 1, 0))
Token(type=ASSIGN, value="=", position=(3, 36, 0))
Token(type=LIST_START, value="[", position=(3, 38, 0))
Token(type=FLOAT_LITERAL, value="3.14", position=(4, 5, 4))
Token(type=COMMA, value=",", position=(4, 9, 4))
Token(type=LIST_END, value="]", position=(5, 1, 0))
Token(type=SYMBOL, value="listLiteralRetrieval", position=(6, 1, 0))
Token(type=ASSIGN, value="=", position=(6, 22, 0))
Token(type=LIST_START, value="[", position=(6, 24, 0))
Token(type=INTEGER_LITERAL, value="10", position=(7, 5, 4))
Token(type=COMMA, value=",", position=(8, 5, 4))
Token(type=INTEGER_LITERAL, value="20", position=(8, 7, 4))
Token(type=COMMA, value=",", position=(9, 5, 4))
Token(type=INTEGER_LITERAL, value="30", position=(9, 7, 4))
Token(type=LIST_END, value="]", position=(10, 1, 0))
Token(type=INDEXING_START, value="[", position=(10, 2, 0))
Token(type=INTEGER_LITERAL, value="1", position=(10, 3, 0))
Token(type=INDEXING_END, value="]", position=(10, 4, 0))
Token(type=SYMBOL, value="listWithoutCommas", position=(11, 1, 0))
Token(type=ASSIGN, value="=", position=(11, 19, 0))
Token(type=LIST_START, value="[", position=(11, 21, 0))
Token(type=INTEGER_LITERAL, value="1", position=(12, 5, 4))
Token(type=INTEGER_LITERAL, value="2", position=(13, 5, 4))
Token(type=INTEGER_LITERAL, value="3", position=(14, 5, 4))
Token(type=INTEGER_LITERAL, value="4", position=(15, 5, 4))
Token(type=INTEGER_LITERAL, value="5", position=(16, 5, 4))
Token(type=LIST_END, value="]", position=(17, 1, 0))
Token(type=SYMBOL, value="multiElementList", position=(19, 1, 0))
Token(type=ASSIGN, value="=", position=(19, 18, 0))
Token(type=LIST_START, value="[", position=(19, 20, 0))
Token(type=STRING_LITERAL, value="apple", position=(20, 5, 4))
Token(type=COMMA, value=",", position=(20, 12, 4))
Token(type=STRING_LITERAL, value="banana", position=(21, 5, 4))
Token(type=COMMA, value=",", position=(21, 13, 4))
Token(type=STRING_LITERAL, value="cherry", position=(22, 5, 4))
Token(type=COMMA, value=",", position=(22, 13, 4))
Token(type=LIST_END, value="]", position=(23, 1, 0))
Token(type=SYMBOL, value="nestedLists", position=(24, 1, 0))
Token(type=ASSIGN, value="=", position=(24, 13, 0))
Token(type=LIST_START, value="[", position=(24, 15, 0))
Token(type=LIST_START, value="[", position=(25, 5, 4))
Token(type=INTEGER_LITERAL, value="1", position=(25, 6, 4))
Token(type=COMMA, value=",", position=(25, 7, 4))
Token(type=INTEGER_LITERAL, value="2", position=(25, 9, 4))
Token(type=COMMA, value=",", position=(25, 10, 4))
Token(type=INTEGER_LITERAL, value="3", position=(25, 12, 4))
Token(type=LIST_END, value="]", position=(25, 13, 4))
Token(type=COMMA, value=",", position=(25, 14, 4))
Token(type=LIST_START, value="[", position=(26, 5, 4))
Token(type=INTEGER_LITERAL, value="4", position=(26, 6, 4))
Token(type=COMMA, value=",", position=(26, 7, 4))
Token(type=INTEGER_LITERAL, value="5", position=(26, 9, 4))
Token(type=COMMA, value=",", position=(26, 10, 4))
Token(type=INTEGER_LITERAL, value="6", position=(26, 12, 4))
Token(type=LIST_END, value="]", position=(26, 13, 4))
Token(type=COMMA, value=",", position=(26, 14, 4))
Token(type=LIST_END, value="]", position=(27, 1, 0))
Token(type=SYMBOL, value="listWithExpressions", position=(28, 1, 0))
Token(type=ASSIGN, value="=", position=(28, 21, 0))
Token(type=LIST_START, value="[", position=(28, 23, 0))
Token(type=INTEGER_LITERAL, value="1", position=(29, 5, 4))
Token(type=PLUS, value="+", position=(29, 7, 4))
Token(type=INTEGER_LITERAL, value="2", position=(29, 9, 4))
Token(type=COMMA, value=",", position=(29, 10, 4))
Token(type=INTEGER_LITERAL, value="3", position=(30, 5, 4))
Token(type=MULTIPLY, value="*", position=(30, 7, 4))
Token(type=INTEGER_LITERAL, value="4", position=(30, 9, 4))
Token(type=COMMA, value=",", position=(30, 10, 4))
Token(type=INTEGER_LITERAL, value="5", position=(31, 5, 4))
Token(type=MINUS, value="-", position=(31, 7, 4))
Token(type=INTEGER_LITERAL, value="6", position=(31, 9, 4))
Token(type=MULTIPLY, value="*", position=(31, 11, 4))
Token(type=PARENTHESES_START, value="(", position=(31, 13, 4))
Token(type=INTEGER_LITERAL, value="8", position=(31, 14, 4))
Token(type=DIVIDE, value="/", position=(31, 16, 4))
Token(type=INTEGER_LITERAL, value="2", position=(31, 18, 4))
Token(type=PARENTHESES_END, value=")", position=(31, 19, 4))
Token(type=COMMA, value=",", position=(31, 20, 4))
Token(type=INTEGER_LITERAL, value="8", position=(32, 5, 4))
Token(type=PLUS, value="+", position=(32, 7, 4))
Token(type=SYMBOL, value="matrix", position=(32, 9, 4))
Token(type=INDEXING_START, value="[", position=(32, 15, 4))
Token(type=INTEGER_LITERAL, value="0", position=(32, 16, 4))
Token(type=INDEXING_END, value="]", position=(32, 17, 4))
Token(type=INDEXING_START, value="[", position=(32, 18, 4))
Token(type=INTEGER_LITERAL, value="1", position=(32, 19, 4))
Token(type=INDEXING_END, value="]", position=(32, 20, 4))
Token(type=MINUS, value="-", position=(32, 22, 4))
Token(type=SYMBOL, value="vector", position=(32, 24, 4))
Token(type=DOT, value=".", position=(32, 30, 4))
Token(type=SYMBOL, value="x", position=(32, 31, 4))
Token(type=COMMA, value=",", position=(32, 32, 4))
Token(type=LIST_END, value="]", position=(33, 1, 0))
Token(type=EOF, value="", position=(141, 1, 0))
*)
