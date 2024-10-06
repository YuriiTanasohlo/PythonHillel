import random

random_list = [random.randint(1, 100) for i in range(random.randint(3, 10))]

print("A random list:")
print(random_list)

# Creating a list of 3 elements and assigning them manually
result_list = [random_list[-1], random_list[-3], random_list[-2]]

print("The result list")
print(result_list)