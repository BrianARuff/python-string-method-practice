# Define initial string.
string = "Happy, Happy Birthday!!"

# Define second string.
string_two = "Happy"

# Count occurence of string_two in string and then print it.
occurence = string.count(string_two)
print(occurence)

# Generate string multiplied by an integer and print it out
string_repeated_nth_times = string * 3
print(string_repeated_nth_times)

 # Get character at any index of a given string and print it.
char_at_zero = string[0]
print(char_at_zero)

# Slice a string starting at position "i" and ending at position "j" while stepping k amount of times and then print the result.
new_string = "Willabeast"
sliced_string = new_string[0:10:2]
print(sliced_string)

# Make a function that performs the same operations as above.

def slice_and_dice(string, i, j, k):
    return string[i:j:k]

print(slice_and_dice('WildaBeast', 0, 10, 2))