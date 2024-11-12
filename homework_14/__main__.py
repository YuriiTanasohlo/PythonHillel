from homework_14.repository.data_base import DataBase
from homework_14.controller.group_controller import GroupController
from homework_14.controller.student_controller import StudentController

if __name__ == "__main__":

    db = DataBase()
    student_controller = StudentController(db)
    group_controller = GroupController(db, student_controller)

    group_controller.show_init()

