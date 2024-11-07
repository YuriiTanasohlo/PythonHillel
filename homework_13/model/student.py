from homework_13.model.person import Person


class Student(Person):
    def __init__(self, first_name: str, last_name: str, gender: "Person.Gender", age: int, record_book_number: str):
        super().__init__(first_name, last_name, gender, age)
        self.__record_book_number = record_book_number

    def __str__(self):
        return super().__str__() + f", record_book_number = {self.__record_book_number}"
