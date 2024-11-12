from homework_14.controller.student_controller import StudentController

from homework_14.repository.date_base import DateBase

from homework_14.model.group import Group

import homework_14.view.group as group_view


class GroupController:

    __group_repository: "DateBase"
    __student_controller: "StudentController"

    def __init__(self, group_repository: "DateBase", student_controller: "StudentController"):
        self.__group_repository = group_repository
        self.__student_controller = student_controller

    def show_init(self):
        self.process_init_input(group_view.show_init_page())

    def process_init_input(self, command: int):

        match command:
            case 1:
                self.create_group(group_view.show_enter_group_page())
                self.process_init_input(self.show_list_group())
            case 2:
                self.show_group(group_view.show_enter_group_page())
            case 3:
                self.process_init_input(self.show_list_group())

    def create_group(self, number: str):
        group = Group(number)
        self.__group_repository.add_group(group)

    def show_group(self, number: str):
        group = self.__group_repository.get_group(number)
        group_view.show_group_page(group)
        self.__student_controller.show_init(group)
        self.show_list_group()

    def show_list_group(self):
        groups = self.__group_repository.get_all_groups()
        return group_view.show_list_group_page(groups)
