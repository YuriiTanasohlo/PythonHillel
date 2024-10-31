def second_index(text, some_str):
    index = 0
    for _ in range(2):
        index = text.find(some_str, index)
        # Return None if first or second index wasn't found
        if index == -1:
            return None
        # Increment index in order to skip already checked char
        index += 1

    # Return index - 1 in order to counter the index incrementation inside the loop
    return index - 1


assert second_index("sims", "s") == 3, 'Test1' 
assert second_index("find the river", "e") == 12, 'Test2' 
assert second_index("hi", "h") is None, 'Test3' 
assert second_index("Hello, hello", "lo") == 10, 'Test4' 
print('ОК')