from homework_14.model.group import Group
from homework_14.model.student import Student


class DataBase:
    __groups = set()

    @staticmethod
    def add_group(group: Group):
        DataBase.__groups.add(group)

    @staticmethod
    def get_group(number: str):

        for group in DataBase.__groups:
            if group.number == number:
                return group

    @staticmethod
    def remove_group(number: str):

        for group in DataBase.__groups:
            if group.number == number:
                DataBase.__groups.remove(group)
                break

    @staticmethod
    def get_all_groups():
        return DataBase.__groups

    @staticmethod
    def add_student(group_number: str, student: Student):
        group = DataBase.get_group(group_number)
        group.add_student(student)

    @staticmethod
    def remove_student(group_number: str, record_book_number: str):
        group = DataBase.get_group(group_number)
        group.remove_student(record_book_number)
