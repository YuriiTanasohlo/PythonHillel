# from homework_14.controller.group_controller import GroupController

from homework_14.repository.data_base import DataBase

from homework_14.model.group import Group
from homework_14.model.student import Student

import homework_14.view.student as student_view


class StudentController:
    __date_base: DataBase

    def __init__(self, date_base: DataBase):
        self.__date_base = date_base

    def show_init(self, group: Group):
        return self.process_init_input(group, student_view.show_init_page())

    def process_init_input(self, group, command: int):

        match command:
            case 1:
                self.create_student(group, student_view.show_enter_student_page())
                self.process_init_input(group, self.show_student_list(group))
            case 2:
                self.delete_student(group, student_view.show_remove_student_page())
                self.process_init_input(group, self.show_student_list(group))
            case 3:
                self.process_init_input(group, self.show_student_list(group))
            case 4:
                return

    def create_student(self, group: Group, student: str):
        first_name, last_name, gender_str, age_str, record_book_number = student.split()
        if gender_str == 1:
            gender = Student.Gender.MALE
        else:
            gender = Student.Gender.FEMALE
        self.__date_base.add_student(group.number, Student(first_name, last_name, gender, age_str, record_book_number))

    def show_student_list(self, group):
        return student_view.show_student_list_page(group.get_all_students())

    def delete_student(self, group, record_book_number: str):
        self.__date_base.remove_student(group.number, record_book_number)
