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

binaryLiteral = 0b101010
negativeBinaryLiteral = -0b1101
octalLiteral = 0o52
negativeOctalLiteral = -0o15
hexadecimalLiteral = 0x2A
negativeHexadecimalLiteral = -0xFF

sectionedDecimalLiteral = 1_000_000
negativeSectionedDecimalLiteral = -9_876_543
sectionedBinaryLiteral = 0b1010_1010
negativeSectionedBinaryLiteral = -0b1101_0011
sectionedOctalLiteral = 0o12_345
negativeSectionedOctalLiteral = -0o76_543
sectionedHexadecimalLiteral = 0xAB_CD_EF
negativeSectionedHexadecimalLiteral = -0xAB_CD_EF
sectionedFloatLiteral = 3.14_15
negativeSectionedFloatLiteral = -0.00_1
sectionedSciFloatLiteral = 1.0e1_0
negativeSectionedSciFloatLiteral = -2.5E8_0
negativeSectionedSciFloatLiteralNegativeExponent = -4e-0_3

numberEndingWithPeriod = 45.

(*
Token(type=SYMBOL, value="integerLiteral", position=(1, 1, 0))
Token(type=ASSIGN, value="=", position=(1, 16, 0))
Token(type=INTEGER_LITERAL, value="42", position=(1, 18, 0))
Token(type=SYMBOL, value="negativeIntegerLiteral", position=(2, 1, 0))
Token(type=ASSIGN, value="=", position=(2, 24, 0))
Token(type=MINUS, value="-", position=(2, 26, 0))
Token(type=INTEGER_LITERAL, value="7", position=(2, 27, 0))
Token(type=SYMBOL, value="floatLiteral", position=(4, 1, 0))
Token(type=ASSIGN, value="=", position=(4, 14, 0))
Token(type=FLOAT_LITERAL, value="3.1415", position=(4, 16, 0))
Token(type=SYMBOL, value="negativeFloatLiteral", position=(5, 1, 0))
Token(type=ASSIGN, value="=", position=(5, 22, 0))
Token(type=MINUS, value="-", position=(5, 24, 0))
Token(type=FLOAT_LITERAL, value="0.001", position=(5, 25, 0))
Token(type=SYMBOL, value="sciFloatLiteralNoFraction", position=(7, 1, 0))
Token(type=ASSIGN, value="=", position=(7, 27, 0))
Token(type=SCI_FLOAT_LITERAL, value="1e10", position=(7, 29, 0))
Token(type=SYMBOL, value="negativeSciFloatLiteralNoFraction", position=(8, 1, 0))
Token(type=ASSIGN, value="=", position=(8, 35, 0))
Token(type=MINUS, value="-", position=(8, 37, 0))
Token(type=SCI_FLOAT_LITERAL, value="2.5E8", position=(8, 38, 0))
Token(type=SYMBOL, value="negativeSciFloatLiteralNoFractionNegativeExponent", position=(9, 1, 0))
Token(type=ASSIGN, value="=", position=(9, 51, 0))
Token(type=MINUS, value="-", position=(9, 53, 0))
Token(type=SCI_FLOAT_LITERAL, value="4e-3", position=(9, 54, 0))
Token(type=SYMBOL, value="sciFloatLiteralWithFraction", position=(10, 1, 0))
Token(type=ASSIGN, value="=", position=(10, 29, 0))
Token(type=SCI_FLOAT_LITERAL, value="6.022e23", position=(10, 31, 0))
Token(type=SYMBOL, value="negativeSciFloatLiteralWithFraction", position=(11, 1, 0))
Token(type=ASSIGN, value="=", position=(11, 37, 0))
Token(type=MINUS, value="-", position=(11, 39, 0))
Token(type=SCI_FLOAT_LITERAL, value="9.81E4", position=(11, 40, 0))
Token(type=SYMBOL, value="negativeSciFloatLiteralWithFractionNegativeExponent", position=(12, 1, 0))
Token(type=ASSIGN, value="=", position=(12, 53, 0))
Token(type=MINUS, value="-", position=(12, 55, 0))
Token(type=SCI_FLOAT_LITERAL, value="3.0e-5", position=(12, 56, 0))
Token(type=SYMBOL, value="binaryLiteral", position=(14, 1, 0))
Token(type=ASSIGN, value="=", position=(14, 15, 0))
Token(type=INTEGER_LITERAL, value="0b101010", position=(14, 17, 0))
Token(type=SYMBOL, value="negativeBinaryLiteral", position=(15, 1, 0))
Token(type=ASSIGN, value="=", position=(15, 23, 0))
Token(type=MINUS, value="-", position=(15, 25, 0))
Token(type=INTEGER_LITERAL, value="0b1101", position=(15, 26, 0))
Token(type=SYMBOL, value="octalLiteral", position=(16, 1, 0))
Token(type=ASSIGN, value="=", position=(16, 14, 0))
Token(type=INTEGER_LITERAL, value="0o52", position=(16, 16, 0))
Token(type=SYMBOL, value="negativeOctalLiteral", position=(17, 1, 0))
Token(type=ASSIGN, value="=", position=(17, 22, 0))
Token(type=MINUS, value="-", position=(17, 24, 0))
Token(type=INTEGER_LITERAL, value="0o15", position=(17, 25, 0))
Token(type=SYMBOL, value="hexadecimalLiteral", position=(18, 1, 0))
Token(type=ASSIGN, value="=", position=(18, 20, 0))
Token(type=INTEGER_LITERAL, value="0x2A", position=(18, 22, 0))
Token(type=SYMBOL, value="negativeHexadecimalLiteral", position=(19, 1, 0))
Token(type=ASSIGN, value="=", position=(19, 28, 0))
Token(type=MINUS, value="-", position=(19, 30, 0))
Token(type=INTEGER_LITERAL, value="0xFF", position=(19, 31, 0))
Token(type=SYMBOL, value="sectionedDecimalLiteral", position=(21, 1, 0))
Token(type=ASSIGN, value="=", position=(21, 25, 0))
Token(type=INTEGER_LITERAL, value="1_000_000", position=(21, 27, 0))
Token(type=SYMBOL, value="negativeSectionedDecimalLiteral", position=(22, 1, 0))
Token(type=ASSIGN, value="=", position=(22, 33, 0))
Token(type=MINUS, value="-", position=(22, 35, 0))
Token(type=INTEGER_LITERAL, value="9_876_543", position=(22, 36, 0))
Token(type=SYMBOL, value="sectionedBinaryLiteral", position=(23, 1, 0))
Token(type=ASSIGN, value="=", position=(23, 24, 0))
Token(type=INTEGER_LITERAL, value="0b1010_1010", position=(23, 26, 0))
Token(type=SYMBOL, value="negativeSectionedBinaryLiteral", position=(24, 1, 0))
Token(type=ASSIGN, value="=", position=(24, 32, 0))
Token(type=MINUS, value="-", position=(24, 34, 0))
Token(type=INTEGER_LITERAL, value="0b1101_0011", position=(24, 35, 0))
Token(type=SYMBOL, value="sectionedOctalLiteral", position=(25, 1, 0))
Token(type=ASSIGN, value="=", position=(25, 23, 0))
Token(type=INTEGER_LITERAL, value="0o12_345", position=(25, 25, 0))
Token(type=SYMBOL, value="negativeSectionedOctalLiteral", position=(26, 1, 0))
Token(type=ASSIGN, value="=", position=(26, 31, 0))
Token(type=MINUS, value="-", position=(26, 33, 0))
Token(type=INTEGER_LITERAL, value="0o76_543", position=(26, 34, 0))
Token(type=SYMBOL, value="sectionedHexadecimalLiteral", position=(27, 1, 0))
Token(type=ASSIGN, value="=", position=(27, 29, 0))
Token(type=SCI_FLOAT_LITERAL, value="0xAB_CD_EF", position=(27, 31, 0))
Token(type=SYMBOL, value="negativeSectionedHexadecimalLiteral", position=(28, 1, 0))
Token(type=ASSIGN, value="=", position=(28, 37, 0))
Token(type=MINUS, value="-", position=(28, 39, 0))
Token(type=SCI_FLOAT_LITERAL, value="0xAB_CD_EF", position=(28, 40, 0))
Token(type=SYMBOL, value="sectionedFloatLiteral", position=(29, 1, 0))
Token(type=ASSIGN, value="=", position=(29, 23, 0))
Token(type=FLOAT_LITERAL, value="3.14_15", position=(29, 25, 0))
Token(type=SYMBOL, value="negativeSectionedFloatLiteral", position=(30, 1, 0))
Token(type=ASSIGN, value="=", position=(30, 31, 0))
Token(type=MINUS, value="-", position=(30, 33, 0))
Token(type=FLOAT_LITERAL, value="0.00_1", position=(30, 34, 0))
Token(type=SYMBOL, value="sectionedSciFloatLiteral", position=(31, 1, 0))
Token(type=ASSIGN, value="=", position=(31, 26, 0))
Token(type=SCI_FLOAT_LITERAL, value="1.0e1_0", position=(31, 28, 0))
Token(type=SYMBOL, value="negativeSectionedSciFloatLiteral", position=(32, 1, 0))
Token(type=ASSIGN, value="=", position=(32, 34, 0))
Token(type=MINUS, value="-", position=(32, 36, 0))
Token(type=SCI_FLOAT_LITERAL, value="2.5E8_0", position=(32, 37, 0))
Token(type=SYMBOL, value="negativeSectionedSciFloatLiteralNegativeExponent", position=(33, 1, 0))
Token(type=ASSIGN, value="=", position=(33, 50, 0))
Token(type=MINUS, value="-", position=(33, 52, 0))
Token(type=SCI_FLOAT_LITERAL, value="4e-0_3", position=(33, 53, 0))
Token(type=SYMBOL, value="numberEndingWithPeriod", position=(35, 1, 0))
Token(type=ASSIGN, value="=", position=(35, 24, 0))
Token(type=FLOAT_LITERAL, value="45.", position=(35, 26, 0))
Token(type=EOF, value="", position=(146, 1, 0))
*)
