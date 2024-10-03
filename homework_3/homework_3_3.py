# example_list = [1, 3]
# example_list = [12, 3, 4, 10]
# example_list = [4, 3, 14, 9, 6, 0, 5]
# example_list = [12, 3, 4, 10, 8]
example_list = [1, 2, 3]
# example_list = []
# example_list = [3]

# If length of the list is 0 then just assigning result list as a list that contains two empty sub-lists
if len(example_list) == 0:
    result_list = [[], []]
# Else if length of the list is 1 then assigning result list as a list that contains the original list and an empty list
elif len(example_list) == 1:
    result_list = [example_list, []]
# Else calculating length of the first sub-list (the biggest one in case original list length is odd)
# And then assigning the result list as a list that contains two sub-lists out of the original one
# Using slicing instrument for slicing the original list
else:
    first_part_list_length = len(example_list) - len(example_list) // 2
    result_list = [example_list[0:first_part_list_length], example_list[first_part_list_length:]]

print(result_list)
