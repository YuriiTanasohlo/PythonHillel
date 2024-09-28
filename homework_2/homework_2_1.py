# using the input function to get user's input and saving into an integer variable
# Using the int function to convert a string to an integer type of data
users_enter = int(input("Please enter a 4-digit number in format NNNN (e.g., 1234): "))

# Extracting all 4 digits and assigning each to separate variables
digit_1 = users_enter // 1000
digit_2 = users_enter % 1000 // 100
digit_3 = users_enter % 100 // 10
digit_4 = users_enter % 10

# Printing the result message
print("The entered number contains next digits:")
print(digit_1)
print(digit_2)
print(digit_3)
print(digit_4)