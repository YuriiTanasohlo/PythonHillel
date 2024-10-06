# example_list = [0, 1, 7, 2, 4, 8]
example_list = [1, 3, 5]
# example_list = [6]
# example_list = []

print("The initial list:")
print(example_list)

result = 0

# Checking if the list length is 0 then the result is 0, else
# Going through all even elements of the list and add them to the result variable
if len(example_list) == 0:
    result = 0
else:
    for i in range(0, len(example_list), 2):
        result += example_list[i]

    # Multiplying the result variable by the last element of the list
    result *= example_list[-1]

print(f"The result of calculation is {result}")
