# Define initial string with extra white space at beginning and end of string and print it.
string = " Brian Ruff  "
print(string)

# Strip string of white space and print it out.
stripped_string = string.strip()
print(stripped_string)

# Justify string on left side with the total amount of white space in string and then print it out.
l_just_string = stripped_string.ljust(len(string), '.')
print(l_just_string)

# Justify string on right side with the total amount of white space in string and then print it out.
r_just_string = stripped_string.rjust(len(string), '.')
print(r_just_string)

# Center string with nth amount of padding and print it.
center_pad_string = stripped_string.center(100, '-')
print(center_pad_string)