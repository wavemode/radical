integerLiteral = 42
negativeIntegerLiteral = -7

floatLiteral = 3.1415
negativeFloatLiteral = -0.001

sciFloatLiteralNoFraction = 1e10
negativeSciFloatLiteralNoFraction = -2.5E8
negativeSciFloatLiteralNoFractionNegativeExponent = -4e-3
sciFloatLiteralWithFraction = 6.022e23
negativeSciFloatLiteralWithFraction = -9.81E4
negativeSciFloatLiteralWithFractionNegativeExponent = -3.0e-5

(*
Token(type=SYMBOL, value='integerLiteral', position=(1, 1, 0))
Token(type=ASSIGN, value='=', position=(1, 16, 0))
Token(type=INTEGER_LITERAL, value='42', position=(1, 18, 0))
Token(type=SYMBOL, value='negativeIntegerLiteral', position=(2, 1, 0))
Token(type=ASSIGN, value='=', position=(2, 24, 0))
Token(type=MINUS, value='-', position=(2, 26, 0))
Token(type=INTEGER_LITERAL, value='7', position=(2, 27, 0))
Token(type=SYMBOL, value='floatLiteral', position=(4, 1, 0))
Token(type=ASSIGN, value='=', position=(4, 14, 0))
Token(type=FLOAT_LITERAL, value='3.1415', position=(4, 16, 0))
Token(type=SYMBOL, value='negativeFloatLiteral', position=(5, 1, 0))
Token(type=ASSIGN, value='=', position=(5, 22, 0))
Token(type=MINUS, value='-', position=(5, 24, 0))
Token(type=FLOAT_LITERAL, value='0.001', position=(5, 25, 0))
Token(type=SYMBOL, value='sciFloatLiteralNoFraction', position=(7, 1, 0))
Token(type=ASSIGN, value='=', position=(7, 27, 0))
Token(type=SCI_FLOAT_LITERAL, value='1e10', position=(7, 29, 0))
Token(type=SYMBOL, value='negativeSciFloatLiteralNoFraction', position=(8, 1, 0))
Token(type=ASSIGN, value='=', position=(8, 35, 0))
Token(type=MINUS, value='-', position=(8, 37, 0))
Token(type=SCI_FLOAT_LITERAL, value='2.5E8', position=(8, 38, 0))
Token(type=SYMBOL, value='negativeSciFloatLiteralNoFractionNegativeExponent', position=(9, 1, 0))
Token(type=ASSIGN, value='=', position=(9, 51, 0))
Token(type=MINUS, value='-', position=(9, 53, 0))
Token(type=SCI_FLOAT_LITERAL, value='4e-3', position=(9, 54, 0))
Token(type=SYMBOL, value='sciFloatLiteralWithFraction', position=(10, 1, 0))
Token(type=ASSIGN, value='=', position=(10, 29, 0))
Token(type=SCI_FLOAT_LITERAL, value='6.022e23', position=(10, 31, 0))
Token(type=SYMBOL, value='negativeSciFloatLiteralWithFraction', position=(11, 1, 0))
Token(type=ASSIGN, value='=', position=(11, 37, 0))
Token(type=MINUS, value='-', position=(11, 39, 0))
Token(type=SCI_FLOAT_LITERAL, value='9.81E4', position=(11, 40, 0))
Token(type=SYMBOL, value='negativeSciFloatLiteralWithFractionNegativeExponent', position=(12, 1, 0))
Token(type=ASSIGN, value='=', position=(12, 53, 0))
Token(type=MINUS, value='-', position=(12, 55, 0))
Token(type=SCI_FLOAT_LITERAL, value='3.0e-5', position=(12, 56, 0))
Token(type=EOF, value='', position=(53, 1, 0))
*)
