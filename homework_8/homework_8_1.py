def add_one(array_of_digits):

    assembled_number = ""

    # add all the elements of the argument list to a string in a loop
    for digit in array_of_digits:
        # Before adding check whether the element (number) in proper range
        if not 0 <= digit <= 9:
            raise Exception("Digits must be in range from 0 to 9!")

        assembled_number += str(digit)
    # calculate result number by converting the string to an integer
    # increment the number & convert the result number to a string
    result_number = str(int(assembled_number) + 1)

    result_array_of_digits = []
    # add each char as a digit to the result array
    for char in result_number:
        result_array_of_digits.append(int(char))

    return result_array_of_digits


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
