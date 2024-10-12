import string

# Getting the customer's input string
input_string = input("Please enter a string: ")

# Removing all the punctuation chars from the string
for char in string.punctuation:
    input_string = input_string.replace(char, "")

# Make each the word with capital first letter in the string
input_string = input_string.title()

# Removing spaces from the string
input_string = input_string.replace(" ", "")

# Adding '#' char in the beginning of the string
input_string = "#" + input_string

# Slicing the first 140 chars
input_string = input_string[:140]

# Printing the result
print(f"The hashtag is {input_string}")
