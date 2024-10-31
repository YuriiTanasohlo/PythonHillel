import math
from typing import Union


def difference(*numbers: Union[int, float]) -> float:

    # check if amount of received numbers is 0, return 0
    if len(numbers) == 0:
        return 0
    # assign infinitive values for max & min values as default
    max_num = -math.inf
    min_num = math.inf
    # for each number in the numbers check whether it is min or max
    for number in numbers:
        if number > max_num:
            max_num = number
        if number < min_num:
            min_num = number

    # return rounded difference between max and min
    return round(max_num - min_num, 2)


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
