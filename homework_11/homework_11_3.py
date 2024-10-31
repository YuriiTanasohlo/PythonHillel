# the function is converting the argument number to a string and check the last char of the string manually
def is_even(number):
    number_str = str(number)
    last_char = number_str[len(number_str) - 1]
    match last_char:
        case "1" | "3" | "5" | "7" | "9":
            return False
        case "0" | "2" | "4" | "6" | "8":
            return True
        case _:
            raise Exception("Invalid number")


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('OK')
