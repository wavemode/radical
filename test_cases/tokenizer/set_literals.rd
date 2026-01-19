simpleSet = { value1, "value1", value2, 42, value3, false }
setWithoutCommas =
    {
        a
        1
        b
        2
        c
        3
    }
nestedSet = {
    {
        innerKey1 = "innerValue1",
        innerKey2 = 3.14
    }
    [1, 2, 3]
}
setWithExpressions = {
    10 + 20,
    ["concat" + "Value"],
    "Hello, " + "world!",
}
setComprehension = { v * 2 for k, v in someMap if v > 10 }
nestedComprehension = { { subK = subV for subK, subV in v } for k, v in anotherMap }

(*
Token(type=SYMBOL, value='simpleSet', position=(1, 1, 0))
Token(type=ASSIGN, value='=', position=(1, 11, 0))
Token(type=OBJECT_START, value='{', position=(1, 13, 0))
Token(type=SYMBOL, value='value1', position=(1, 15, 0))
Token(type=COMMA, value=',', position=(1, 21, 0))
Token(type=STRING_LITERAL, value='value1', position=(1, 23, 0))
Token(type=COMMA, value=',', position=(1, 31, 0))
Token(type=SYMBOL, value='value2', position=(1, 33, 0))
Token(type=COMMA, value=',', position=(1, 39, 0))
Token(type=INTEGER_LITERAL, value='42', position=(1, 41, 0))
Token(type=COMMA, value=',', position=(1, 43, 0))
Token(type=SYMBOL, value='value3', position=(1, 45, 0))
Token(type=COMMA, value=',', position=(1, 51, 0))
Token(type=FALSE, value='false', position=(1, 53, 0))
Token(type=OBJECT_END, value='}', position=(1, 59, 0))
Token(type=SYMBOL, value='setWithoutCommas', position=(2, 1, 0))
Token(type=ASSIGN, value='=', position=(2, 18, 0))
Token(type=OBJECT_START, value='{', position=(3, 5, 4))
Token(type=SYMBOL, value='a', position=(4, 9, 8))
Token(type=INTEGER_LITERAL, value='1', position=(5, 9, 8))
Token(type=SYMBOL, value='b', position=(6, 9, 8))
Token(type=INTEGER_LITERAL, value='2', position=(7, 9, 8))
Token(type=SYMBOL, value='c', position=(8, 9, 8))
Token(type=INTEGER_LITERAL, value='3', position=(9, 9, 8))
Token(type=OBJECT_END, value='}', position=(10, 5, 4))
Token(type=SYMBOL, value='nestedSet', position=(11, 1, 0))
Token(type=ASSIGN, value='=', position=(11, 11, 0))
Token(type=OBJECT_START, value='{', position=(11, 13, 0))
Token(type=OBJECT_START, value='{', position=(12, 5, 4))
Token(type=SYMBOL, value='innerKey1', position=(13, 9, 8))
Token(type=ASSIGN, value='=', position=(13, 19, 8))
Token(type=STRING_LITERAL, value='innerValue1', position=(13, 21, 8))
Token(type=COMMA, value=',', position=(13, 34, 8))
Token(type=SYMBOL, value='innerKey2', position=(14, 9, 8))
Token(type=ASSIGN, value='=', position=(14, 19, 8))
Token(type=FLOAT_LITERAL, value='3.14', position=(14, 21, 8))
Token(type=OBJECT_END, value='}', position=(15, 5, 4))
Token(type=LIST_START, value='[', position=(16, 5, 4))
Token(type=INTEGER_LITERAL, value='1', position=(16, 6, 4))
Token(type=COMMA, value=',', position=(16, 7, 4))
Token(type=INTEGER_LITERAL, value='2', position=(16, 9, 4))
Token(type=COMMA, value=',', position=(16, 10, 4))
Token(type=INTEGER_LITERAL, value='3', position=(16, 12, 4))
Token(type=LIST_END, value=']', position=(16, 13, 4))
Token(type=OBJECT_END, value='}', position=(17, 1, 0))
Token(type=SYMBOL, value='setWithExpressions', position=(18, 1, 0))
Token(type=ASSIGN, value='=', position=(18, 20, 0))
Token(type=OBJECT_START, value='{', position=(18, 22, 0))
Token(type=INTEGER_LITERAL, value='10', position=(19, 5, 4))
Token(type=PLUS, value='+', position=(19, 8, 4))
Token(type=INTEGER_LITERAL, value='20', position=(19, 10, 4))
Token(type=COMMA, value=',', position=(19, 12, 4))
Token(type=LIST_START, value='[', position=(20, 5, 4))
Token(type=STRING_LITERAL, value='concat', position=(20, 6, 4))
Token(type=PLUS, value='+', position=(20, 15, 4))
Token(type=STRING_LITERAL, value='Value', position=(20, 17, 4))
Token(type=LIST_END, value=']', position=(20, 24, 4))
Token(type=COMMA, value=',', position=(20, 25, 4))
Token(type=STRING_LITERAL, value='Hello, ', position=(21, 5, 4))
Token(type=PLUS, value='+', position=(21, 15, 4))
Token(type=STRING_LITERAL, value='world!', position=(21, 17, 4))
Token(type=COMMA, value=',', position=(21, 25, 4))
Token(type=OBJECT_END, value='}', position=(22, 1, 0))
Token(type=SYMBOL, value='setComprehension', position=(23, 1, 0))
Token(type=ASSIGN, value='=', position=(23, 18, 0))
Token(type=OBJECT_START, value='{', position=(23, 20, 0))
Token(type=SYMBOL, value='v', position=(23, 22, 0))
Token(type=MULTIPLY, value='*', position=(23, 24, 0))
Token(type=INTEGER_LITERAL, value='2', position=(23, 26, 0))
Token(type=FOR, value='for', position=(23, 28, 0))
Token(type=SYMBOL, value='k', position=(23, 32, 0))
Token(type=COMMA, value=',', position=(23, 33, 0))
Token(type=SYMBOL, value='v', position=(23, 35, 0))
Token(type=IN, value='in', position=(23, 37, 0))
Token(type=SYMBOL, value='someMap', position=(23, 40, 0))
Token(type=IF, value='if', position=(23, 48, 0))
Token(type=SYMBOL, value='v', position=(23, 51, 0))
Token(type=GREATER_THAN, value='>', position=(23, 53, 0))
Token(type=INTEGER_LITERAL, value='10', position=(23, 55, 0))
Token(type=OBJECT_END, value='}', position=(23, 58, 0))
Token(type=SYMBOL, value='nestedComprehension', position=(24, 1, 0))
Token(type=ASSIGN, value='=', position=(24, 21, 0))
Token(type=OBJECT_START, value='{', position=(24, 23, 0))
Token(type=OBJECT_START, value='{', position=(24, 25, 0))
Token(type=SYMBOL, value='subK', position=(24, 27, 0))
Token(type=ASSIGN, value='=', position=(24, 32, 0))
Token(type=SYMBOL, value='subV', position=(24, 34, 0))
Token(type=FOR, value='for', position=(24, 39, 0))
Token(type=SYMBOL, value='subK', position=(24, 43, 0))
Token(type=COMMA, value=',', position=(24, 47, 0))
Token(type=SYMBOL, value='subV', position=(24, 49, 0))
Token(type=IN, value='in', position=(24, 54, 0))
Token(type=SYMBOL, value='v', position=(24, 57, 0))
Token(type=OBJECT_END, value='}', position=(24, 59, 0))
Token(type=FOR, value='for', position=(24, 61, 0))
Token(type=SYMBOL, value='k', position=(24, 65, 0))
Token(type=COMMA, value=',', position=(24, 66, 0))
Token(type=SYMBOL, value='v', position=(24, 68, 0))
Token(type=IN, value='in', position=(24, 70, 0))
Token(type=SYMBOL, value='anotherMap', position=(24, 73, 0))
Token(type=OBJECT_END, value='}', position=(24, 84, 0))
Token(type=EOF, value='', position=(130, 1, 0))
*)
