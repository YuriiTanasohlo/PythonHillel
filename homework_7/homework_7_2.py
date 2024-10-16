def correct_sentence(text):
    # trim spaces on the beginning and at the end of the string
    text = text.strip()

    # removing multiple spaces in a row
    while text.find("  ") != -1:
        text = text.replace("  ", " ")

    index = 0
    while True:
        # If first letter on the beginning of the string or after dot is in lowercase,
        # replace it with the uppercase letter
        if not text[index].isupper():
            text = text[:index] + text[index].upper() + text[index + 1:]
        # find index of the next dot
        index = text.find(".", index)
        # if the next dot doesn't exist, or it is the end of the string, escape the loop
        if index == -1 or index + 1 == len(text):
            break
        # increment the index in order to skip the dot
        index += 1
        # add space, if it doesn't exist after the dot
        if text[index] != " ":
            text = text[:index] + " " + text[index:]
        # increment the index in order to skip the space
        index += 1
    # add dot to the end of string
    if text[-1] != ".":
        text += "."

    return text


#
assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
assert (correct_sentence(" greetings  for      you.        Friends.   hello ")
        == "Greetings for you. Friends. Hello."), 'Test6'
print('ОК')
