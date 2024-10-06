# example_list = [0, 1, 0, 12, 3]
# example_list = [0]
# example_list = [1, 0, 13, 0, 0, 0, 5]
example_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

# example_list_result = example_list.copy()
# print(example_list.count(0))
amount_of_zeroes = example_list.count(0)

print("The initial list:")
print(example_list)
print(f"The list contains '0' {amount_of_zeroes} times")
print()

i = 0
while i < len(example_list):
    if example_list[i] == 0:
        example_list.pop(i)
        example_list.append(0)
        amount_of_zeroes -= 1
        if amount_of_zeroes < 1:
            break
    else:
        i += 1

print("The result list:")
print(example_list)

