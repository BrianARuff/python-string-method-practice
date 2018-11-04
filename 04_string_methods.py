# Define initial string with extra white space at beginning and end of string and print it.
string = " Brian Ruff  "
print(string)

# Strip string of white space and print it out.
stripped_string = string.strip()
print(stripped_string)

# Justify string with the total amount of white space in string and then print it out.
l_just_string = stripped_string.ljust(len(string), '.')
print(l_just_string)