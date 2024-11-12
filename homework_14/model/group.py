from homework_14.model.student import Student

from homework_14.exceptions.group_exception import OverloadedGroupException


class Group:
    __number: str
    __group: set

    def __init__(self, number: str):
        self.__number = number
        self.__group = set()

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = number

    def add_student(self, student: Student):
        if len(self.__group) > 10:
            raise OverloadedGroupException("Too much students in the group!")
        else:
            self.__group.add(student)

    def find_student(self, record_book_number: str):
        return next((student for student in self.__group if student.record_book_number == record_book_number), None)

    def remove_student(self, record_book_number: str):
        student = self.find_student(record_book_number)
        if student is not None:
            self.__group.remove(student)

    def get_all_students(self):
        return self.__group

    def length(self):
        return len(self.__group)

    def __str__(self):
        students = ""
        for student in self.__group:
            students += f"{student}\n"
        return f"Group: number = {self.__number}, students: \n{students}"
