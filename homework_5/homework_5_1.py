import string
import keyword

var_name = input("Please enter a string - the variable name: ")

result = True

# Checking next conditions:
# Whether the first char is digit
if var_name[0].isdigit():
    result = False
# Whether the variable name contains space
elif var_name.find(' ') != -1:
    result = False
# Whether the variable name contains more than one char '_' (requirement for the HW)
elif var_name.count('_') > 1:
    result = False
# Whether the variable name contains only lowercase chars
elif not var_name.islower():
    result = False
# Whether the variable name contains any punctuation char except '_'
for char in string.punctuation:
    if char == "_":
        continue
    elif var_name.find(char) != -1:
        result = False
        break
# Whether the variable name is the reserved python words
for word in keyword.kwlist:
    if var_name == word:
        result = False
        print("6")
        break

print(result)
