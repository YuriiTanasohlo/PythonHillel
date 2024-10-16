def common_elements():
    # Generate two lists according to the requirements
    numbers_multiples_of_3 = list(range(0, 100, 3))
    numbers_multiples_of_5 = list(range(0, 100, 5))

    # Convert the lists to sets and return numbers that exist in the both sets
    return set(numbers_multiples_of_3).intersection(set(numbers_multiples_of_5))


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
