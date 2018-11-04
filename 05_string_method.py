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
print(string.index("a", 3, 8))

# Replace function
s1 = 'this is the world we live in'
s2 = 'i'
s3 = 'I'
# s1 is the string comparator, s2 is the old value in the string comparator, s3 is the new value that is going to change what ever s2 is, only in s1, and it will only affect the first occurence because of the count paramter being filled out. If it had not been filled out then it would replace all of the "i"s with "I"s.
s1 = s1.replace(s2, s3, 1)
print(s1)