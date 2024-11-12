import os

from homework_14.model.group import Group


def show_init_page():
    __clear_console()
    print("Welcome to Uni app")
    print("Please enter 1 to create a group")
    print("Please enter 2 to choose existing group")
    print("Please enter 3 to list all the existing groups")

    return int(input())


def show_enter_group_page():
    __clear_console()
    print("Please enter the group number")

    return int(input())


def show_list_group_page(groups: set[Group]):
    __clear_console()
    print("List of groups:")
    for group in groups:
        print(group.number)

    print("Please click enter to continue")
    input()
    return show_init_page()


def show_group_page(group: "Group"):
    __clear_console()
    print(f"Group with number {group.number}")


def __clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
