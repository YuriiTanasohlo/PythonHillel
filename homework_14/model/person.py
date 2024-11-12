from enum import Enum


class Person:
    __first_name: str
    __last_name: str
    __gender: "Person.Gender"
    __age: int

    def __init__(self, first_name: str, last_name: str, gender: "Person.Gender", age: int):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__age = age

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    def get_last_name(self):
        return self.__last_name

    def __str__(self):
        return f"Person: first_name = {self.__first_name}, last_name = {self.__last_name}"

    def __eq__(self, other: "Person"):
        if self.last_name == other.last_name and self.first_name == other.first_name:
            return True
        else:
            return False

    def __hash__(self):
        return hash(str(self))

    class Gender(Enum):
        MALE = "male"
        FEMALE = "female"
