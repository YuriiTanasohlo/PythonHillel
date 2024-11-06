class Customer:
    def __init__(self, last_name: str, first_name: str, patronymic: str, phone_number: int, email: str):
        self.__last_name = last_name
        self.__first_name = first_name
        self.__patronymic = patronymic
        self.__phone_number = phone_number
        self.__email = email

    def __str__(self):
        return f"Customer: {self.__first_name} {self.__last_name}"
