# example_list = [1, 3]
# example_list = [12, 3, 4, 10]
example_list = [4, 3, 14, 9, 6, 0, 5]
# example_list = [12, 3, 4, 10, 8]
# example_list = []
# example_list = [3]

# Printing the initial list
print(f"The list before the changes: {example_list}")

# If length of the list is more than 1 than moving the last element to the beginning of the list
# Using if statement to check the condition
# Using .pop(-1) function to return and remove the last element
# Using .insert(0, val) function to insert the removed element to the beginning of the list
if not (len(example_list) > 1):
    element = example_list.pop(-1)
    print(f"The element to be moved: {element}")
    example_list.insert(0, element)

# Printing the final list
print(f"The list after the changes: {example_list}")

