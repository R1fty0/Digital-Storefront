class Person:
    def __init__(self, age, name, color):
        self.age = age
        self.name = name
        self.color = color

class Employee():
    cls_id = 'employee'
    another = 'foo'

    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary


bob = Employee(1, 'bobbyhadz', 100)


employee = (vars(bob))
for key, value in employee.items():
    print(f"{key}: {value}")


import itertools

my_list = [1, 2, 3, 4, 5]

for n in my_list:
    last_item = next(itertools.islice(my_list, 1, None))
    print("Last item:" + str(last_item))

last_item = next(itertools.islice(my_list, 1, None))

print(last_item) # 5


