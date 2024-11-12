from homework_14.model.student import Student

from homework_14.exceptions.group_exception import OverloadedGroupException


class Group:
    def __init__(self, number: str):
        self.__number = number
        self.__group = set()

    def add_student(self, student: Student):
        if len(self.__group) > 10:
            raise OverloadedGroupException("Too much students in the group!")
        else:
            self.__group.add(student)

    def find_student(self, last_name: str):
        return next((student for student in self.__group if student.get_last_name() == last_name), None)

    def delete_student(self, last_name: str):
        student = self.find_student(last_name)
        if student is not None:
            self.__group.remove(self.find_student(last_name))

    # added a service method that was not in the task
    def length(self):
        return len(self.__group)

    def __str__(self):
        students = ""
        for student in self.__group:
            students += f"{student}\n"
        return f"Group: number = {self.__number}, students: \n{students}"
