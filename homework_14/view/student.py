import os

from homework_14.model.student import Student


def show_init_page():
    __clear_console()
    print("Please enter 1 to create a student")
    print("Please enter 2 to remove a student")
    print("Please enter 3 to list all the existing students in the group")
    print("Please enter 4 to return to all groups")

    return int(input())


def show_enter_student_page():
    print("Please enter first_name, last_name, gender (1 = male, 2 = female), age, record_book_number divided by space")
    print("e.g. \"Mike Jackson 1 23 LT3793\"")

    return input()


def show_remove_student_page():
    print("Please enter record_book_number of the student to remove")

    return input()


def show_student_list_page(students: set[Student]):
    __clear_console()
    print("List of students:")
    for student in students:
        print(student)

    print("Please click enter to continue")
    input()
    return show_init_page()


def __clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')