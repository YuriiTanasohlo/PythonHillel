class Counter:

    def __init__(self, current: int = 1, min_value: int = 0, max_value: int = 10):
        self.__current = current
        self.__min_value = min_value
        self.__max_value = max_value

    def set_current(self, start: int):
        self.__current = start

    def set_max(self, max_value: int):
        if max_value < self.__current:
            raise ValueError("Max value is less than current value")
        self.__max_value = max_value

    def set_min(self, min_value):
        if min_value > self.__current:
            raise ValueError("Min value is more than current value")
        self.__min_value = min_value

    def step_up(self):
        if self.__current < self.__max_value:
            self.__current += 1
        else:
            raise ValueError("Max value is gained")

    def step_down(self):
        if self.__current > self.__min_value:
            self.__current -= 1
        else:
            raise ValueError("Min value is gained")

    def get_current(self):
        return self.__current
