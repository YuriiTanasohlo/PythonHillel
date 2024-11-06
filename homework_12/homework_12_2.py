from homework_12.model.item import Item
from homework_12.model.customer import Customer
from homework_12.model.order import Order


bread = Item("bread", "simple bread", 12, "normal")
egg = Item("bread", "simple bread", 3, "small")
meat = Item("meat", "chicken meat", 56, "normal")

petro = Customer("Petrenko", "Petro", "Petrovych", 235634634, "petrenko@gmail.com")
stepan = Customer("Ptepanenko", "Stepan", "Stepanovych", 5456868, "stepanenko@gmail.com")


petro_order = Order(petro)
petro_order.add_item(bread, 2)
petro_order.add_item(egg, 10)
petro_order.add_item(meat, 1)

stepan_order = Order(stepan)
stepan_order.add_item(bread, 1)
stepan_order.add_item(egg, 20)

print("Items:")
print(bread)
print(egg)
print(meat)
print()
print("Petro:")
print(petro)
print(petro_order)
print(f"Total: {petro_order.get_total()}\n")
print("Stepan:")
print(stepan)
print(stepan_order)
print(f"Total: {stepan_order.get_total()}\n")

"""
Items:
Item: bread, price: 12
Item: bread, price: 3
Item: meat, price: 56

Petro:
Customer: Petro Petrenko
Order: customer = Customer: Petro Petrenko
with items:
Item: bread, price: 12, amount 2
Item: bread, price: 3, amount 10
Item: meat, price: 56, amount 1

Total: 110

Stepan:
Customer: Stepan Ptepanenko
Order: customer = Customer: Stepan Ptepanenko
with items:
Item: bread, price: 12, amount 1
Item: bread, price: 3, amount 20

Total: 72
"""