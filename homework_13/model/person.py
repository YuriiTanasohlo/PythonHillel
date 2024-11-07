from enum import Enum


class Person:
    def __init__(self, first_name: str, last_name: str, gender: "Person.Gender", age: int):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__age = age

    def get_last_name(self):
        return self.__last_name

    def __str__(self):
        return f"Person: first_name = {self.__first_name}, last_name = {self.__last_name}"

    class Gender(Enum):
        MALE = "male"
        FEMALE = "female"
