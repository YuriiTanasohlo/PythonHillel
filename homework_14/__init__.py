from homework_14.model.student import Student
from homework_14.model.group import Group


if __name__ == "__main__":

    group_1 = Group("1")
    vasyl = Student("Vasyl", "Vasylenko", Student.Gender.MALE, 23, "23234")
    ivan = Student("Ivan", "Ivanenko", Student.Gender.MALE, 22, "23235")
    petro = Student("Petro", "Petrenko", Student.Gender.MALE, 23, "23236")
    petro1 = Student("Petro", "Petrenko", Student.Gender.MALE, 23, "23236")

    group_1.add_student(vasyl)
    group_1.add_student(ivan)
    group_1.add_student(petro)

    print(group_1.find_student("Petrenko") == petro)
    print(group_1.find_student("Petrenko") == petro1)
    print(group_1.find_student("Petrenko") == ivan)
