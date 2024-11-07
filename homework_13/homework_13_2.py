from homework_13.model.counter import Counter

my_counter = Counter(3, 1, 5)

try:
    print(my_counter.get_current())
    my_counter.step_up()

    print(my_counter.get_current())
    my_counter.step_up()

    print(my_counter.get_current())
    my_counter.step_up()
except ValueError as e:
    print(e)

try:
    print(my_counter.get_current())
    my_counter.set_max(4)
except ValueError as e:
    print(e)

try:
    print(my_counter.get_current())
    my_counter.set_max(6)

    print(my_counter.get_current())
    my_counter.step_up()

    print(my_counter.get_current())
    my_counter.step_up()
except ValueError as e:
    print(e)

try:
    print(my_counter.get_current())
    my_counter.set_min(4)

    print(my_counter.get_current())
    my_counter.step_down()

    print(my_counter.get_current())
    my_counter.step_down()

    print(my_counter.get_current())
    my_counter.step_down()
except ValueError as e:
    print(e)

try:
    print(my_counter.get_current())
    my_counter.set_min(5)
except ValueError as e:
    print(e)

try:
    print(my_counter.get_current())
    my_counter.set_min(2)

    print(my_counter.get_current())
    my_counter.step_down()

    print(my_counter.get_current())
    my_counter.step_down()

    print(my_counter.get_current())
    my_counter.step_down()
except ValueError as e:
    print(e)
