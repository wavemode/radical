five : 5 = 5
six : 5.5 = 5.5
sci : 1.2e3 = 1.2e3

basicStringType : "hello" = "hello"
rawStringType : r"raw\nstring" = r"raw\nstring"
multiLineStringType : """multi
line
string""" = """multi
line
string"""

rawMultiLineStringType : r"""raw
multi
line
string""" = r"""raw
multi
line
string"""

(*
Token(type=SYMBOL, value='five', position=(1, 1, 0))
Token(type=COLON, value=':', position=(1, 6, 0))
Token(type=INTEGER_LITERAL, value='5', position=(1, 8, 0))
Token(type=ASSIGN, value='=', position=(1, 10, 0))
Token(type=INTEGER_LITERAL, value='5', position=(1, 12, 0))
Token(type=SYMBOL, value='six', position=(2, 1, 0))
Token(type=COLON, value=':', position=(2, 5, 0))
Token(type=FLOAT_LITERAL, value='5.5', position=(2, 7, 0))
Token(type=ASSIGN, value='=', position=(2, 11, 0))
Token(type=FLOAT_LITERAL, value='5.5', position=(2, 13, 0))
Token(type=SYMBOL, value='sci', position=(3, 1, 0))
Token(type=COLON, value=':', position=(3, 5, 0))
Token(type=FLOAT_LITERAL, value='1.2', position=(3, 7, 0))
Token(type=SYMBOL, value='e3', position=(3, 10, 0))
Token(type=ASSIGN, value='=', position=(3, 13, 0))
Token(type=FLOAT_LITERAL, value='1.2', position=(3, 15, 0))
Token(type=SYMBOL, value='e3', position=(3, 18, 0))
Token(type=SYMBOL, value='basicStringType', position=(5, 1, 0))
Token(type=COLON, value=':', position=(5, 17, 0))
Token(type=STRING_LITERAL, value='hello', position=(5, 19, 0))
Token(type=ASSIGN, value='=', position=(5, 27, 0))
Token(type=STRING_LITERAL, value='hello', position=(5, 29, 0))
Token(type=SYMBOL, value='rawStringType', position=(6, 1, 0))
Token(type=COLON, value=':', position=(6, 15, 0))
Token(type=RAW_STRING_LITERAL, value='raw\nstring', position=(6, 17, 0))
Token(type=ASSIGN, value='=', position=(6, 32, 0))
Token(type=RAW_STRING_LITERAL, value='raw\nstring', position=(6, 34, 0))
Token(type=SYMBOL, value='multiLineStringType', position=(7, 1, 0))
Token(type=COLON, value=':', position=(7, 21, 0))
Token(type=MULTILINE_STRING_LITERAL, value='multi
line
string', position=(7, 23, 0))
Token(type=ASSIGN, value='=', position=(7, 47, 0))
Token(type=MULTILINE_STRING_LITERAL, value='multi
line
string', position=(7, 49, 0))
Token(type=SYMBOL, value='rawMultiLineStringType', position=(9, 1, 0))
Token(type=COLON, value=':', position=(9, 24, 0))
Token(type=RAW_MULTILINE_STRING_LITERAL, value='raw
multi
line
string', position=(9, 26, 0))
Token(type=ASSIGN, value='=', position=(9, 55, 0))
Token(type=RAW_MULTILINE_STRING_LITERAL, value='raw
multi
line
string', position=(9, 57, 0))
Token(type=EOF, value='', position=(60, 3, 2))
*)