def first_word(text):
    punctuation = ",."
    for char in punctuation:
        if text.find(char) != -1:
            text = text.replace(char, " ")

    text = text.strip()

    amount_of_chars = text.find(" ")
    if text.find(" ") != -1:
        return text[:amount_of_chars]
    else:
        return text


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')