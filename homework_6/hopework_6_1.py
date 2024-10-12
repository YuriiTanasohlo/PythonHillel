import string

input_string = input("Please enter two letters separated by a hyphen (e.g. \"e-c\"): ")

# Defining the entered letters
first_letter, second_letter = input_string.split("-")

# Defining indexes in string.ascii_letters of the entered letters
first_index = string.ascii_letters.find(first_letter)
second_index = string.ascii_letters.find(second_letter)

# Defining the result using list slice
print(f"The result is: {string.ascii_letters[first_index:second_index + 1]}")
