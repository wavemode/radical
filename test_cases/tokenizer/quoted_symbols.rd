`my quoted var` = 10

`my
varname
can
contain
anything` = 20

`var name with a backtick `` inside` = 30

(*
Token(type=SYMBOL, value="my quoted var", position=(1, 1, 0))
Token(type=ASSIGN, value="=", position=(1, 17, 0))
Token(type=INTEGER_LITERAL, value="10", position=(1, 19, 0))
Token(type=SYMBOL, value="my\nvarname\ncan\ncontain\nanything", position=(3, 1, 0))
Token(type=ASSIGN, value="=", position=(3, 35, 0))
Token(type=INTEGER_LITERAL, value="20", position=(3, 37, 0))
Token(type=SYMBOL, value="var name with a backtick ", position=(5, 1, 0))
Token(type=SYMBOL, value=" inside", position=(5, 28, 0))
Token(type=ASSIGN, value="=", position=(5, 38, 0))
Token(type=INTEGER_LITERAL, value="30", position=(5, 40, 0))
Token(type=EOF, value="", position=(20, 1, 0))
*)
