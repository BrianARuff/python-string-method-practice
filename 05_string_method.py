# Define initial string and print it.
string = "Brian Ruff"
print(string)

# Find first occurence/index of given substring in main string and print it.
print(string.find("f"))

# Find last index of given substring in main string and print it.
print(string.rfind("f"))

# Find lowest index of substring in string and print it.
print(string.index("f"))

# Find first occurence of substring in string after i but before j and print it.
print(string.index("a", 4, 8))