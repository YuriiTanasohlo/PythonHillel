from homework_13.model.student import Student


class Group:
    def __init__(self, number: str):
        self.__number = number
        self.__group = set()

    def add_student(self, student: Student):
        self.__group.add(student)

    def find_student(self, last_name: str):
        return next((student for student in self.__group if student.get_last_name() == last_name), None)

    def delete_student(self, last_name: str):
        student = self.find_student(last_name)
        if student is not None:
            self.__group.remove(self.find_student(last_name))

    def __str__(self):
        students = ""
        for student in self.__group:
            students += f"{student}\n"
        return f"Group: number = {self.__number}, students: \n{students}"
