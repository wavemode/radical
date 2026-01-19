singleEntryTree = { a b, }
multiEntryTree = {
    rootLeft childLeft1,
    rootLeft childLeft2,
    rootRight childRight1,
    rootRight childRight2,
}
nestedTree = {
    parent1 {
        child1A grandchild1
        child1B grandchild2
    }
    , parent2 {
        child2A grandchild3
        child2B grandchild4
    }
}


tripleNestedTreeNoCommas = {
    grandParent1 {
        parent1 {
            child1A grandchild1
            child1B grandchild2
        }
        parent2 {
            child2A grandchild3
            child2B grandchild4
        }
    }
    grandParent2 {
        parent3 {
            child3A grandchild5
            child3B grandchild6
        }
    }
}

treeComprehension = {
    ["a"] {
        b { 
            c
        }
    }
    for a in someSetA
    for b in someSetB
    for c in someSetC
}

(*
Token(type=SYMBOL, value='singleEntryTree', position=(1, 1, 0))
Token(type=ASSIGN, value='=', position=(1, 17, 0))
Token(type=OBJECT_START, value='{', position=(1, 19, 0))
Token(type=SYMBOL, value='a', position=(1, 21, 0))
Token(type=SYMBOL, value='b', position=(1, 23, 0))
Token(type=COMMA, value=',', position=(1, 24, 0))
Token(type=OBJECT_END, value='}', position=(1, 26, 0))
Token(type=SYMBOL, value='multiEntryTree', position=(2, 1, 0))
Token(type=ASSIGN, value='=', position=(2, 16, 0))
Token(type=OBJECT_START, value='{', position=(2, 18, 0))
Token(type=SYMBOL, value='rootLeft', position=(3, 5, 4))
Token(type=SYMBOL, value='childLeft1', position=(3, 14, 4))
Token(type=COMMA, value=',', position=(3, 24, 4))
Token(type=SYMBOL, value='rootLeft', position=(4, 5, 4))
Token(type=SYMBOL, value='childLeft2', position=(4, 14, 4))
Token(type=COMMA, value=',', position=(4, 24, 4))
Token(type=SYMBOL, value='rootRight', position=(5, 5, 4))
Token(type=SYMBOL, value='childRight1', position=(5, 15, 4))
Token(type=COMMA, value=',', position=(5, 26, 4))
Token(type=SYMBOL, value='rootRight', position=(6, 5, 4))
Token(type=SYMBOL, value='childRight2', position=(6, 15, 4))
Token(type=COMMA, value=',', position=(6, 26, 4))
Token(type=OBJECT_END, value='}', position=(7, 1, 0))
Token(type=SYMBOL, value='nestedTree', position=(8, 1, 0))
Token(type=ASSIGN, value='=', position=(8, 12, 0))
Token(type=OBJECT_START, value='{', position=(8, 14, 0))
Token(type=SYMBOL, value='parent1', position=(9, 5, 4))
Token(type=OBJECT_START, value='{', position=(9, 13, 4))
Token(type=SYMBOL, value='child1A', position=(10, 9, 8))
Token(type=SYMBOL, value='grandchild1', position=(10, 17, 8))
Token(type=SYMBOL, value='child1B', position=(11, 9, 8))
Token(type=SYMBOL, value='grandchild2', position=(11, 17, 8))
Token(type=OBJECT_END, value='}', position=(12, 5, 4))
Token(type=COMMA, value=',', position=(13, 5, 4))
Token(type=SYMBOL, value='parent2', position=(13, 7, 4))
Token(type=OBJECT_START, value='{', position=(13, 15, 4))
Token(type=SYMBOL, value='child2A', position=(14, 9, 8))
Token(type=SYMBOL, value='grandchild3', position=(14, 17, 8))
Token(type=SYMBOL, value='child2B', position=(15, 9, 8))
Token(type=SYMBOL, value='grandchild4', position=(15, 17, 8))
Token(type=OBJECT_END, value='}', position=(16, 5, 4))
Token(type=OBJECT_END, value='}', position=(17, 1, 0))
Token(type=SYMBOL, value='tripleNestedTreeNoCommas', position=(20, 1, 0))
Token(type=ASSIGN, value='=', position=(20, 26, 0))
Token(type=OBJECT_START, value='{', position=(20, 28, 0))
Token(type=SYMBOL, value='grandParent1', position=(21, 5, 4))
Token(type=OBJECT_START, value='{', position=(21, 18, 4))
Token(type=SYMBOL, value='parent1', position=(22, 9, 8))
Token(type=OBJECT_START, value='{', position=(22, 17, 8))
Token(type=SYMBOL, value='child1A', position=(23, 13, 12))
Token(type=SYMBOL, value='grandchild1', position=(23, 21, 12))
Token(type=SYMBOL, value='child1B', position=(24, 13, 12))
Token(type=SYMBOL, value='grandchild2', position=(24, 21, 12))
Token(type=OBJECT_END, value='}', position=(25, 9, 8))
Token(type=SYMBOL, value='parent2', position=(26, 9, 8))
Token(type=OBJECT_START, value='{', position=(26, 17, 8))
Token(type=SYMBOL, value='child2A', position=(27, 13, 12))
Token(type=SYMBOL, value='grandchild3', position=(27, 21, 12))
Token(type=SYMBOL, value='child2B', position=(28, 13, 12))
Token(type=SYMBOL, value='grandchild4', position=(28, 21, 12))
Token(type=OBJECT_END, value='}', position=(29, 9, 8))
Token(type=OBJECT_END, value='}', position=(30, 5, 4))
Token(type=SYMBOL, value='grandParent2', position=(31, 5, 4))
Token(type=OBJECT_START, value='{', position=(31, 18, 4))
Token(type=SYMBOL, value='parent3', position=(32, 9, 8))
Token(type=OBJECT_START, value='{', position=(32, 17, 8))
Token(type=SYMBOL, value='child3A', position=(33, 13, 12))
Token(type=SYMBOL, value='grandchild5', position=(33, 21, 12))
Token(type=SYMBOL, value='child3B', position=(34, 13, 12))
Token(type=SYMBOL, value='grandchild6', position=(34, 21, 12))
Token(type=OBJECT_END, value='}', position=(35, 9, 8))
Token(type=OBJECT_END, value='}', position=(36, 5, 4))
Token(type=OBJECT_END, value='}', position=(37, 1, 0))
Token(type=SYMBOL, value='treeComprehension', position=(39, 1, 0))
Token(type=ASSIGN, value='=', position=(39, 19, 0))
Token(type=OBJECT_START, value='{', position=(39, 21, 0))
Token(type=LIST_START, value='[', position=(40, 5, 4))
Token(type=STRING_LITERAL, value='a', position=(40, 6, 4))
Token(type=LIST_END, value=']', position=(40, 9, 4))
Token(type=OBJECT_START, value='{', position=(40, 11, 4))
Token(type=SYMBOL, value='b', position=(41, 9, 8))
Token(type=OBJECT_START, value='{', position=(41, 11, 8))
Token(type=SYMBOL, value='c', position=(42, 13, 12))
Token(type=OBJECT_END, value='}', position=(43, 9, 8))
Token(type=OBJECT_END, value='}', position=(44, 5, 4))
Token(type=FOR, value='for', position=(45, 5, 4))
Token(type=SYMBOL, value='a', position=(45, 9, 4))
Token(type=IN, value='in', position=(45, 11, 4))
Token(type=SYMBOL, value='someSetA', position=(45, 14, 4))
Token(type=FOR, value='for', position=(46, 5, 4))
Token(type=SYMBOL, value='b', position=(46, 9, 4))
Token(type=IN, value='in', position=(46, 11, 4))
Token(type=SYMBOL, value='someSetB', position=(46, 14, 4))
Token(type=FOR, value='for', position=(47, 5, 4))
Token(type=SYMBOL, value='c', position=(47, 9, 4))
Token(type=IN, value='in', position=(47, 11, 4))
Token(type=SYMBOL, value='someSetC', position=(47, 14, 4))
Token(type=OBJECT_END, value='}', position=(48, 1, 0))
Token(type=EOF, value='', position=(151, 1, 0))
*)
