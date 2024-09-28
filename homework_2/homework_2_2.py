# using the input function to get user's input and saving into an integer variable
# Using the int function to convert a string to an integer type of data
users_enter = int(input("Please enter a 5-digit number in format NNNNN (e.g., 12345): "))

# Extracting all 5 digits and assigning each to separate variables
digit_1 = users_enter // 10000
digit_2 = users_enter % 10000 // 1000
digit_3 = users_enter % 1000 // 100
digit_4 = users_enter % 100 // 10
digit_5 = users_enter % 10

# Printing the result message
print(f"The reversed number from the entered one is : {digit_5}{digit_4}{digit_3}{digit_2}{digit_1}")
