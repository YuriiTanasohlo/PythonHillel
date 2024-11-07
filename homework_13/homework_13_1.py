from homework_13.model.student import Student
from homework_13.model.group import Group

group_1 = Group("1")
vasyl = Student("Vasyl", "Vasylenko", Student.Gender.MALE, 23, "23234")
ivan = Student("Ivan", "Ivanenko", Student.Gender.MALE, 22, "23235")
petro = Student("Petro", "Petrenko", Student.Gender.MALE, 23, "23236")

group_1.add_student(vasyl)
group_1.add_student(ivan)

print(group_1)
print(group_1.find_student(vasyl.get_last_name()))
print(group_1.find_student(ivan.get_last_name()))
print(group_1.find_student(petro.get_last_name()))

group_1.delete_student(vasyl.get_last_name())
group_1.delete_student(petro.get_last_name())

print(group_1)
