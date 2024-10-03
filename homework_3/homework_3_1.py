# Declaring the first & second operators & operand by using the input function
# using the int function to convert a string to an integer type of data
first_operand = int(input("Please enter the first operand in format N+ (e.g., 123, 837789, 1): "))
second_operand = int(input("Please enter the second operand in format N+ (e.g., 123, 837789, 1): "))
operand = input("Please enter the operator the options (+, -, *, /): ")

match operand:
    case "+":
        result = first_operand + second_operand
    case "-":
        result = first_operand - second_operand
    case "*":
        result = first_operand * second_operand
    case "/":
        if second_operand == 0:
            result = "Cannot be divided by 0!"
        else:
            result = first_operand / second_operand
    case _:
        result = "Unexpected error.."
print(f"The result is: {result}")
