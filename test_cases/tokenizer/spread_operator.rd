listWithSingleSpread = [...otherList]
mapWithSingleSpread = {
    ...otherMap
}

listWithMultipleSpreads = [
    1
    ...listA
    2
    ...listB
    3
]

mapWithMultipleSpreads = {
    key1 = "value1"
    ...mapA
    key2 = "value2"
    ...mapB
    key3 = "value3"
}

setWithMultipleSpreads = {
    1
    ...setA
    2
    ...setB
    3
}

treeWithMultipleSpreads = {
    name "value"
    ...treeA
    otherName {
        child1 10
        child2 20.0
    }
    ...treeB
}

(*
Token(type=SYMBOL, value='listWithSingleSpread', position=(1, 1, 0))
Token(type=ASSIGN, value='=', position=(1, 22, 0))
Token(type=LIST_START, value='[', position=(1, 24, 0))
Token(type=SPREAD, value='...', position=(1, 25, 0))
Token(type=SYMBOL, value='otherList', position=(1, 28, 0))
Token(type=LIST_END, value=']', position=(1, 37, 0))
Token(type=SYMBOL, value='mapWithSingleSpread', position=(2, 1, 0))
Token(type=ASSIGN, value='=', position=(2, 21, 0))
Token(type=OBJECT_START, value='{', position=(2, 23, 0))
Token(type=SPREAD, value='...', position=(3, 5, 4))
Token(type=SYMBOL, value='otherMap', position=(3, 8, 4))
Token(type=OBJECT_END, value='}', position=(4, 1, 0))
Token(type=SYMBOL, value='listWithMultipleSpreads', position=(6, 1, 0))
Token(type=ASSIGN, value='=', position=(6, 25, 0))
Token(type=LIST_START, value='[', position=(6, 27, 0))
Token(type=INTEGER_LITERAL, value='1', position=(7, 5, 4))
Token(type=SPREAD, value='...', position=(8, 5, 4))
Token(type=SYMBOL, value='listA', position=(8, 8, 4))
Token(type=INTEGER_LITERAL, value='2', position=(9, 5, 4))
Token(type=SPREAD, value='...', position=(10, 5, 4))
Token(type=SYMBOL, value='listB', position=(10, 8, 4))
Token(type=INTEGER_LITERAL, value='3', position=(11, 5, 4))
Token(type=LIST_END, value=']', position=(12, 1, 0))
Token(type=SYMBOL, value='mapWithMultipleSpreads', position=(14, 1, 0))
Token(type=ASSIGN, value='=', position=(14, 24, 0))
Token(type=OBJECT_START, value='{', position=(14, 26, 0))
Token(type=SYMBOL, value='key1', position=(15, 5, 4))
Token(type=ASSIGN, value='=', position=(15, 10, 4))
Token(type=STRING_LITERAL, value='value1', position=(15, 12, 4))
Token(type=SPREAD, value='...', position=(16, 5, 4))
Token(type=SYMBOL, value='mapA', position=(16, 8, 4))
Token(type=SYMBOL, value='key2', position=(17, 5, 4))
Token(type=ASSIGN, value='=', position=(17, 10, 4))
Token(type=STRING_LITERAL, value='value2', position=(17, 12, 4))
Token(type=SPREAD, value='...', position=(18, 5, 4))
Token(type=SYMBOL, value='mapB', position=(18, 8, 4))
Token(type=SYMBOL, value='key3', position=(19, 5, 4))
Token(type=ASSIGN, value='=', position=(19, 10, 4))
Token(type=STRING_LITERAL, value='value3', position=(19, 12, 4))
Token(type=OBJECT_END, value='}', position=(20, 1, 0))
Token(type=SYMBOL, value='setWithMultipleSpreads', position=(22, 1, 0))
Token(type=ASSIGN, value='=', position=(22, 24, 0))
Token(type=OBJECT_START, value='{', position=(22, 26, 0))
Token(type=INTEGER_LITERAL, value='1', position=(23, 5, 4))
Token(type=SPREAD, value='...', position=(24, 5, 4))
Token(type=SYMBOL, value='setA', position=(24, 8, 4))
Token(type=INTEGER_LITERAL, value='2', position=(25, 5, 4))
Token(type=SPREAD, value='...', position=(26, 5, 4))
Token(type=SYMBOL, value='setB', position=(26, 8, 4))
Token(type=INTEGER_LITERAL, value='3', position=(27, 5, 4))
Token(type=OBJECT_END, value='}', position=(28, 1, 0))
Token(type=SYMBOL, value='treeWithMultipleSpreads', position=(30, 1, 0))
Token(type=ASSIGN, value='=', position=(30, 25, 0))
Token(type=OBJECT_START, value='{', position=(30, 27, 0))
Token(type=SYMBOL, value='name', position=(31, 5, 4))
Token(type=STRING_LITERAL, value='value', position=(31, 10, 4))
Token(type=SPREAD, value='...', position=(32, 5, 4))
Token(type=SYMBOL, value='treeA', position=(32, 8, 4))
Token(type=SYMBOL, value='otherName', position=(33, 5, 4))
Token(type=OBJECT_START, value='{', position=(33, 15, 4))
Token(type=SYMBOL, value='child1', position=(34, 9, 8))
Token(type=INTEGER_LITERAL, value='10', position=(34, 16, 8))
Token(type=SYMBOL, value='child2', position=(35, 9, 8))
Token(type=FLOAT_LITERAL, value='20.0', position=(35, 16, 8))
Token(type=OBJECT_END, value='}', position=(36, 5, 4))
Token(type=SPREAD, value='...', position=(37, 5, 4))
Token(type=SYMBOL, value='treeB', position=(37, 8, 4))
Token(type=OBJECT_END, value='}', position=(38, 1, 0))
Token(type=EOF, value='', position=(111, 1, 0))
*)
