def find_unique_value(input_list):
    # create set out of the input list
    input_set = set(input_list)
    # check count of each element from set in the input list
    # if count is equal to 1, then the element is unique
    for element in input_set:
        if input_list.count(element) == 1:
            return element
    # return None if all elements in the input list are not unique
    return None


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
