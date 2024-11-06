class Item:
    def __init__(self, name: str, description: str, price: int, size: str):
        self.__name = name
        self.__description = description
        self.__price = price
        self.__size = size

    def __str__(self):
        return f"Item: {self.__name}, price: {self.__price}"

    def get_price(self):
        return self.__price
