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




my_list = [1, 2, 3, 4, 5]

print(f"OG: {len(my_list)}")
for i in my_list:
    print(i)

itemToRemove = len(my_list)

my_list.remove(itemToRemove)

print(f"After moving an item: {len(my_list)}")

for i in my_list:
    print(i)
