value = let
    a : Int
    a = 1
    
    b : Int
    b = 2

    c : List[Int]
    c = [3, 4, 5]
  in
    a + b + c[3]

(*
Token(type=SYMBOL, value="value", position=(1, 1, 0))
Token(type=ASSIGN, value="=", position=(1, 7, 0))
Token(type=LET, value="let", position=(1, 9, 0))
Token(type=SYMBOL, value="a", position=(2, 5, 4))
Token(type=COLON, value=":", position=(2, 7, 4))
Token(type=SYMBOL, value="Int", position=(2, 9, 4))
Token(type=SYMBOL, value="a", position=(3, 5, 4))
Token(type=ASSIGN, value="=", position=(3, 7, 4))
Token(type=INTEGER_LITERAL, value="1", position=(3, 9, 4))
Token(type=SYMBOL, value="b", position=(5, 5, 4))
Token(type=COLON, value=":", position=(5, 7, 4))
Token(type=SYMBOL, value="Int", position=(5, 9, 4))
Token(type=SYMBOL, value="b", position=(6, 5, 4))
Token(type=ASSIGN, value="=", position=(6, 7, 4))
Token(type=INTEGER_LITERAL, value="2", position=(6, 9, 4))
Token(type=SYMBOL, value="c", position=(8, 5, 4))
Token(type=COLON, value=":", position=(8, 7, 4))
Token(type=SYMBOL, value="List", position=(8, 9, 4))
Token(type=INDEXING_START, value="[", position=(8, 13, 4))
Token(type=SYMBOL, value="Int", position=(8, 14, 4))
Token(type=INDEXING_END, value="]", position=(8, 17, 4))
Token(type=SYMBOL, value="c", position=(9, 5, 4))
Token(type=ASSIGN, value="=", position=(9, 7, 4))
Token(type=LIST_START, value="[", position=(9, 9, 4))
Token(type=INTEGER_LITERAL, value="3", position=(9, 10, 4))
Token(type=COMMA, value=",", position=(9, 11, 4))
Token(type=INTEGER_LITERAL, value="4", position=(9, 13, 4))
Token(type=COMMA, value=",", position=(9, 14, 4))
Token(type=INTEGER_LITERAL, value="5", position=(9, 16, 4))
Token(type=LIST_END, value="]", position=(9, 17, 4))
Token(type=IN, value="in", position=(10, 3, 2))
Token(type=SYMBOL, value="a", position=(11, 5, 4))
Token(type=PLUS, value="+", position=(11, 7, 4))
Token(type=SYMBOL, value="b", position=(11, 9, 4))
Token(type=PLUS, value="+", position=(11, 11, 4))
Token(type=SYMBOL, value="c", position=(11, 13, 4))
Token(type=INDEXING_START, value="[", position=(11, 14, 4))
Token(type=INTEGER_LITERAL, value="3", position=(11, 15, 4))
Token(type=INDEXING_END, value="]", position=(11, 16, 4))
Token(type=EOF, value="", position=(54, 3, 2))
*)