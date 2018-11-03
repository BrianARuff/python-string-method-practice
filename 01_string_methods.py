# Instantiate a variable named sentence and then assign a string to it
sentence = "The quick brown fox jumps over the lazy dog"

# Print out the sentence variable.
print(sentence)

# Using a built-in function, make the entire sentence variable value lower case and save it into a new variable called lower_case_sentence
lower_case_sentence = sentence.lower()

# Print out the lower_case_sentence variable's value.
print(lower_case_sentence)

# Create a new variable called upper_case_sentence and make its value an all upper case version of the original sentence variable.
upper_case_sentence = sentence.upper()

# Print out a copy of upper_case_sentence variable's value.
print(upper_case_sentence)

# Create a new variable and assign a new string value to it; however, be sure to mix up the casing throughout the string.
oddly_cased_string = "listings: harry potter, the grinch, the shining, shrek, star wars, BRIAN"

# Print out the new variable's value
print(oddly_cased_string)

# Convert the new variable's value to title case in a variable called title_cased_string.
title_cased_string = oddly_cased_string.title()

# Print the title cased string variable.
print(title_cased_string)

# Create a new variable with a string as its value, and make sure to make words that should be upper case, lower case and vice-versa.
another_oddly_cased_string = "hI WORLD, i AM bRIAN rUFF."

# Swap the casing in the new variable's value and call the varible swap_cased_string.
swap_cased_string = another_oddly_cased_string.swapcase()

# Print the swap_cased_string variable's value
print(swap_cased_string)