from homework_12.model.item import Item
from homework_12.model.customer import Customer


class Order:
    def __init__(self, customer: Customer):
        self.__customer = customer
        self.__items = {}

    def __str__(self):
        items = ""
        for item, amount in self.__items.items():
            items += f"{item}, amount {amount}\n"
        return f"Order: customer = {self.__customer}\nwith items:\n{items}"

    def add_item(self, item: Item, amount: int):
        self.__items[item] = amount

    def get_total(self):
        total = 0
        for item, amount in self.__items.items():
            total += item.get_price() * amount
        return total
