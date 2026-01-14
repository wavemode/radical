stringConstant = "This is a string constant"

multiLineString = """
    This is a multi-line
    string that spans
    several lines.

    Escape sequence are supported: \n, \t, \", \", \\
"""

rawString = r"C:\Users\Name\Documents\file.txt"  -- no escape sequences are processed

rawMultiLineString = r"""
This is a raw multi-line string. Escape sequences like \n and \t
are not processed here.
"""

formatString = f"The value of stringConstant is: {stringConstant}"

anotherFormatString = f"""
Multi-line formatted string:
- Original: {stringConstant}
"""

concatenatedString = "Hello, " + "world!"  -- using + operator

unicodeString = "☂️🌧️"
firstCodePoint: str = unicodeString[0]
secondCodePoint: str = unicodeString[1]
umbrella: str = unicodeString[0:2]  -- umbrella emoji consists of two code points

-- builtin methods

strlen = f"Length of unicodeString is: {unicodeString.length()}" -- will count unicode code points
upperStr = f"Uppercase: {stringConstant.toUpper()}"
lowerStr = f"Lowercase: {stringConstant.toLower()}"
replacedStr = f"Replaced string: {stringConstant.replace("is", "was")}"
trimmedStr = f"Trimmed string: {"   padded string   ".trim()}"
splitStr = "one,two,three".split(",")
joinedStr = "; ".join(["one", "two", "three"])
substring = f"Substring (0, 4): {stringConstant[0:4]}"
findIndex = f"Index of "is": {stringConstant.indexOf("is")}"
includesSubstr = f"Includes "string": {stringConstant.includes("string")}"
startsWithSubstr = f"Starts with "This": {stringConstant.startsWith("This")}"
endsWithSubstr = f"Ends with "constant": {stringConstant.endsWith("constant")}"
multiLineStringStrippedIndent = """
        This is a multi-line string with indentation.
    Four leading spaces will be stripped from each line.
""".stripIndent()

