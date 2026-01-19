unaryNot = not 5
unaryMinus = - 10
unaryPlus = + 15

unaryPlusMinus = + - 20
unaryMinusPlus = - + 25
unaryNotMinusPlusPlusMinus = not - + + - 30

(*
Token(type=SYMBOL, value='unaryNot', position=(1, 1, 0))
Token(type=ASSIGN, value='=', position=(1, 10, 0))
Token(type=NOT, value='not', position=(1, 12, 0))
Token(type=INTEGER_LITERAL, value='5', position=(1, 16, 0))
Token(type=SYMBOL, value='unaryMinus', position=(2, 1, 0))
Token(type=ASSIGN, value='=', position=(2, 12, 0))
Token(type=MINUS, value='-', position=(2, 14, 0))
Token(type=INTEGER_LITERAL, value='10', position=(2, 16, 0))
Token(type=SYMBOL, value='unaryPlus', position=(3, 1, 0))
Token(type=ASSIGN, value='=', position=(3, 11, 0))
Token(type=PLUS, value='+', position=(3, 13, 0))
Token(type=INTEGER_LITERAL, value='15', position=(3, 15, 0))
Token(type=SYMBOL, value='unaryPlusMinus', position=(5, 1, 0))
Token(type=ASSIGN, value='=', position=(5, 16, 0))
Token(type=PLUS, value='+', position=(5, 18, 0))
Token(type=MINUS, value='-', position=(5, 20, 0))
Token(type=INTEGER_LITERAL, value='20', position=(5, 22, 0))
Token(type=SYMBOL, value='unaryMinusPlus', position=(6, 1, 0))
Token(type=ASSIGN, value='=', position=(6, 16, 0))
Token(type=MINUS, value='-', position=(6, 18, 0))
Token(type=PLUS, value='+', position=(6, 20, 0))
Token(type=INTEGER_LITERAL, value='25', position=(6, 22, 0))
Token(type=SYMBOL, value='unaryNotMinusPlusPlusMinus', position=(7, 1, 0))
Token(type=ASSIGN, value='=', position=(7, 28, 0))
Token(type=NOT, value='not', position=(7, 30, 0))
Token(type=MINUS, value='-', position=(7, 34, 0))
Token(type=PLUS, value='+', position=(7, 36, 0))
Token(type=PLUS, value='+', position=(7, 38, 0))
Token(type=MINUS, value='-', position=(7, 40, 0))
Token(type=INTEGER_LITERAL, value='30', position=(7, 42, 0))
Token(type=EOF, value='', position=(42, 1, 0))
*)
