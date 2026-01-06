string_constant = "This is a string constant"

multi_line_string = """
This is a multi-line
string that spans
several lines.

Escape sequence are supported: \n, \t, \", \', \\
"""

raw_string = r"C:\Users\Name\Documents\file.txt"  # no escape sequences are processed

raw_multi_line_string = r"""
This is a raw multi-line string. Escape sequences like \n and \t
are not processed here.
"""

formatted_string = f"The value of string_constant is: {string_constant}"

another_formatted_string = f"""
Multi-line formatted string:
- Original: {string_constant}
"""

concatenated_string = "Hello, " + "world!"  # using + operator

unicode_string = "☂️🌧️"
first_code_point: str = unicode_string[0]
second_code_point: str = unicode_string[1]
umbrella: str = unicode_string[0:2]  # umbrella emoji consists of two code points

# stdlib utilities
import std::string

strlen = f"Length of unicode_string is: {string.length(unicode_string)}" # will count unicode code points
upper_str = f"Uppercase: {string.to_upper(string_constant)}"
lower_str = f"Lowercase: {string.to_lower(string_constant)}"
replaced_str = f"Replaced string: {string.replace(string_constant, 'constant', 'value')}"
trimmed_str = f"Trimmed string: '{string.trim('   padded string   ')}'"
split_str = string.split("one,two,three", ",")
joined_str = string.join(["one", "two", "three"], "; ")
substring = f"Substring (0, 4): {string.substring(string_constant, 0, 4)}"
find_index = f"Index of 'is': {string.find(string_constant, 'is')}"


multi_line_string_strip_indent = string.strip_indent("""
        This is a multi-line string with indentation.
    Four leading spaces will be stripped from each line.
""")

