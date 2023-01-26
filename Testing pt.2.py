class Category:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = list()
        self.initialInventory = list()

    def get_inventory(self):
        return self.inventory

    def initializeInventory(self):
        for items in self.initialInventory:
            self.inventory.append(items)


class Item:
    def __init__(self, price, name, category):
        self.price = price
        self.name = name
        self.category = category

    def viewDetails(self):
        details = (vars(self))
        for key, value in details.items():
            print(f"{key}: {value}")