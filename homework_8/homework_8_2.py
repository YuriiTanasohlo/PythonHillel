import string


def is_palindrome(text):
    # remove all punctuation chars
    for char in string.punctuation:
        if text.find(char) != -1:
            text = text.replace(char, "")
    # remove all spaces
    if text.find(" ") != -1:
        text = text.replace(" ", "")
    # convert to lowercase
    text = text.lower()
    # check each char in the text till the middle
    # if a char by index isn't the same as char by index starting from end, return False
    for i in range(len(text) // 2):
        if not text[i] == text[-i - 1]:
            return False
    # return True as all teh chars are mirrored
    return True


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
