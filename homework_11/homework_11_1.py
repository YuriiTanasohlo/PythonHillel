from inspect import isgenerator


# the function checks the prime numbers in double loop (the second loop is halved after 4th iteration of the first loop)
def prime_generator(end):
    for i in range(2, end + 1):
        is_natural = True
        for j in range(2, i if i < 5 else i // 2):
            if i % j == 0:
                is_natural = False
                break
        if is_natural:
            yield i


gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')