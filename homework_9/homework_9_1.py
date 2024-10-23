def popular_words(text: str, words: list) -> dict:
    # get rid of double spaces
    if text.find("  ") != -1:
        text = text.replace("  ", " ")
    # get rid of spaces on the start & end of the string
    text = text.strip()
    # convert to lowercase
    text = text.lower()
    # split the string by space into a list
    text_words = text.split(" ")

    # count each word in words and add result to a dict
    result_dict = {}
    for word in words:
        result_dict[word] = text_words.count(word)

    return result_dict


assert (popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                      ['i', 'was', 'three', 'near']) ==
        {'i': 4, 'was': 3, 'three': 0, 'near': 0}), 'Test1'
assert (popular_words('''When I was Three I was full of glee''',
                      ['when', 'i', 'was', 'three', 'full', 'of', 'glee']) ==
        {'when': 1, 'i': 2, 'was': 2, 'three': 1, 'full': 1, 'of': 1, 'glee': 1}), 'Test2'
assert (popular_words('''When I was Four   I began to explore''',
                      ['when', 'i', 'was', 'four', 'began', 'to', 'explore']) ==
        {'when': 1, 'i': 2, 'was': 1, 'four': 1, 'began': 1, 'to': 1, 'explore': 1})
assert (popular_words('''When I was Five I felt so alive''',
                      ['when', 'i', 'was', 'five', 'felt', 'so', 'alive']) ==
        {'when': 1, 'i': 2, 'was': 1, 'five': 1, 'felt': 1, 'so': 1, 'alive': 1})
assert (popular_words('''When I was Six I learned a few tricks''',
                      ['when', 'i', 'was', 'six', 'learned', 'a', 'few', 'tricks', 'tickets']) ==
        {'when': 1, 'i': 2, 'was': 1, 'six': 1, 'learned': 1, 'a': 1, 'few': 1, 'tricks': 1, 'tickets': 0})

print('OK')
