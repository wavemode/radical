emptyMap = {  }
simpleMap = { key1 = "value1"
    , key2 = 42
    , key3 = false }
mapWithoutCommas =
    {
        a = 1
        b = 2
        c = 3
    }
nestedMap = {
    outerKey1 = {
        innerKey1 = "innerValue1",
        innerKey2 = 3.14
    },
    outerKey2 = [1, 2, 3]
}
mapWithExpressions = {
    sumKey = 10 + 20
    ["concat" + "Key"] = "Hello, " + "world!"
}

(*
Token(type=SYMBOL, value="emptyMap", position=(1, 1, 0))
Token(type=ASSIGN, value="=", position=(1, 10, 0))
Token(type=OBJECT_START, value="{", position=(1, 12, 0))
Token(type=OBJECT_END, value="}", position=(1, 15, 0))
Token(type=SYMBOL, value="simpleMap", position=(2, 1, 0))
Token(type=ASSIGN, value="=", position=(2, 11, 0))
Token(type=OBJECT_START, value="{", position=(2, 13, 0))
Token(type=SYMBOL, value="key1", position=(2, 15, 0))
Token(type=ASSIGN, value="=", position=(2, 20, 0))
Token(type=STRING_LITERAL, value="value1", position=(2, 22, 0))
Token(type=COMMA, value=",", position=(3, 5, 4))
Token(type=SYMBOL, value="key2", position=(3, 7, 4))
Token(type=ASSIGN, value="=", position=(3, 12, 4))
Token(type=INTEGER_LITERAL, value="42", position=(3, 14, 4))
Token(type=COMMA, value=",", position=(4, 5, 4))
Token(type=SYMBOL, value="key3", position=(4, 7, 4))
Token(type=ASSIGN, value="=", position=(4, 12, 4))
Token(type=FALSE, value="false", position=(4, 14, 4))
Token(type=OBJECT_END, value="}", position=(4, 20, 4))
Token(type=SYMBOL, value="mapWithoutCommas", position=(5, 1, 0))
Token(type=ASSIGN, value="=", position=(5, 18, 0))
Token(type=OBJECT_START, value="{", position=(6, 5, 4))
Token(type=SYMBOL, value="a", position=(7, 9, 8))
Token(type=ASSIGN, value="=", position=(7, 11, 8))
Token(type=INTEGER_LITERAL, value="1", position=(7, 13, 8))
Token(type=SYMBOL, value="b", position=(8, 9, 8))
Token(type=ASSIGN, value="=", position=(8, 11, 8))
Token(type=INTEGER_LITERAL, value="2", position=(8, 13, 8))
Token(type=SYMBOL, value="c", position=(9, 9, 8))
Token(type=ASSIGN, value="=", position=(9, 11, 8))
Token(type=INTEGER_LITERAL, value="3", position=(9, 13, 8))
Token(type=OBJECT_END, value="}", position=(10, 5, 4))
Token(type=SYMBOL, value="nestedMap", position=(11, 1, 0))
Token(type=ASSIGN, value="=", position=(11, 11, 0))
Token(type=OBJECT_START, value="{", position=(11, 13, 0))
Token(type=SYMBOL, value="outerKey1", position=(12, 5, 4))
Token(type=ASSIGN, value="=", position=(12, 15, 4))
Token(type=OBJECT_START, value="{", position=(12, 17, 4))
Token(type=SYMBOL, value="innerKey1", position=(13, 9, 8))
Token(type=ASSIGN, value="=", position=(13, 19, 8))
Token(type=STRING_LITERAL, value="innerValue1", position=(13, 21, 8))
Token(type=COMMA, value=",", position=(13, 34, 8))
Token(type=SYMBOL, value="innerKey2", position=(14, 9, 8))
Token(type=ASSIGN, value="=", position=(14, 19, 8))
Token(type=FLOAT_LITERAL, value="3.14", position=(14, 21, 8))
Token(type=OBJECT_END, value="}", position=(15, 5, 4))
Token(type=COMMA, value=",", position=(15, 6, 4))
Token(type=SYMBOL, value="outerKey2", position=(16, 5, 4))
Token(type=ASSIGN, value="=", position=(16, 15, 4))
Token(type=LIST_START, value="[", position=(16, 17, 4))
Token(type=INTEGER_LITERAL, value="1", position=(16, 18, 4))
Token(type=COMMA, value=",", position=(16, 19, 4))
Token(type=INTEGER_LITERAL, value="2", position=(16, 21, 4))
Token(type=COMMA, value=",", position=(16, 22, 4))
Token(type=INTEGER_LITERAL, value="3", position=(16, 24, 4))
Token(type=LIST_END, value="]", position=(16, 25, 4))
Token(type=OBJECT_END, value="}", position=(17, 1, 0))
Token(type=SYMBOL, value="mapWithExpressions", position=(18, 1, 0))
Token(type=ASSIGN, value="=", position=(18, 20, 0))
Token(type=OBJECT_START, value="{", position=(18, 22, 0))
Token(type=SYMBOL, value="sumKey", position=(19, 5, 4))
Token(type=ASSIGN, value="=", position=(19, 12, 4))
Token(type=INTEGER_LITERAL, value="10", position=(19, 14, 4))
Token(type=PLUS, value="+", position=(19, 17, 4))
Token(type=INTEGER_LITERAL, value="20", position=(19, 19, 4))
Token(type=LIST_START, value="[", position=(20, 5, 4))
Token(type=STRING_LITERAL, value="concat", position=(20, 6, 4))
Token(type=PLUS, value="+", position=(20, 15, 4))
Token(type=STRING_LITERAL, value="Key", position=(20, 17, 4))
Token(type=LIST_END, value="]", position=(20, 22, 4))
Token(type=ASSIGN, value="=", position=(20, 24, 4))
Token(type=STRING_LITERAL, value="Hello, ", position=(20, 26, 4))
Token(type=PLUS, value="+", position=(20, 36, 4))
Token(type=STRING_LITERAL, value="world!", position=(20, 38, 4))
Token(type=OBJECT_END, value="}", position=(21, 1, 0))
Token(type=EOF, value="", position=(101, 1, 0))
*)
