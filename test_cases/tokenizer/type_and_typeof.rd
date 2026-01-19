myValue = 5

otherValue : typeof myValue = 10

option1 = "A"
option2 = "B"
option3 = "C"

enumValue :
    type option1
    | type option2
    | type option3
    = "C"

(*
Token(type=SYMBOL, value='myValue', position=(1, 1, 0))
Token(type=ASSIGN, value='=', position=(1, 9, 0))
Token(type=INTEGER_LITERAL, value='5', position=(1, 11, 0))
Token(type=SYMBOL, value='otherValue', position=(3, 1, 0))
Token(type=COLON, value=':', position=(3, 12, 0))
Token(type=TYPEOF, value='typeof', position=(3, 14, 0))
Token(type=SYMBOL, value='myValue', position=(3, 21, 0))
Token(type=ASSIGN, value='=', position=(3, 29, 0))
Token(type=INTEGER_LITERAL, value='10', position=(3, 31, 0))
Token(type=SYMBOL, value='option1', position=(5, 1, 0))
Token(type=ASSIGN, value='=', position=(5, 9, 0))
Token(type=STRING_LITERAL, value='A', position=(5, 11, 0))
Token(type=SYMBOL, value='option2', position=(6, 1, 0))
Token(type=ASSIGN, value='=', position=(6, 9, 0))
Token(type=STRING_LITERAL, value='B', position=(6, 11, 0))
Token(type=SYMBOL, value='option3', position=(7, 1, 0))
Token(type=ASSIGN, value='=', position=(7, 9, 0))
Token(type=STRING_LITERAL, value='C', position=(7, 11, 0))
Token(type=SYMBOL, value='enumValue', position=(9, 1, 0))
Token(type=COLON, value=':', position=(9, 11, 0))
Token(type=TYPE, value='type', position=(10, 5, 4))
Token(type=SYMBOL, value='option1', position=(10, 10, 4))
Token(type=VARIANT, value='|', position=(11, 5, 4))
Token(type=TYPE, value='type', position=(11, 7, 4))
Token(type=SYMBOL, value='option2', position=(11, 12, 4))
Token(type=VARIANT, value='|', position=(12, 5, 4))
Token(type=TYPE, value='type', position=(12, 7, 4))
Token(type=SYMBOL, value='option3', position=(12, 12, 4))
Token(type=ASSIGN, value='=', position=(13, 5, 4))
Token(type=STRING_LITERAL, value='C', position=(13, 7, 4))
Token(type=EOF, value='', position=(48, 1, 0))
*)
