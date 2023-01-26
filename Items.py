class Category:
    def __init__(self, name):
        self.name = name
        self.inventory = list()
        self.initialInventory = list()

    def get_inventory(self):
        """ Returns the current inventory of the category"""
        return self.inventory

    def initializeInventory(self):
        """ Sets up the initial inventory of the category."""
        for item in self.initialInventory:
            self.inventory.append(item)

    def addMultipleItems(self, item, num):
        """ Add multiple items of the same type to the inventory. """
        for x in range(num):
            self.inventory.append(item)

    def stockItemToInventory(self, item):
        """ Stocks an item to the inventory"""
        try:
            self.inventory.append(item)
        except AttributeError:
            print("An error occurred. Unable to restock items.")

    def removeItemFromInventory(self, item):
        """ Removes an item from the inventory. """
        self.inventory.remove(item)


class Item:
    def __init__(self, price, name, category):
        self.price = price
        self.name = name
        self.category = category

    def viewDetails(self):
        """ Shows all the details of the item. """
        details = (vars(self))
        for key, value in details.items():  # This for-loop was brought to you by Chat-GPT.
            print(f"{key}: {value}")


class Clothing(Item):
    """ Clothing that the user can purchase."""
    def __init__(self, price, name, size):
        super().__init__(price, name, "Clothing")
        self.size = size


class Food(Item):
    """ Food that the user can purchase."""
    def __init__(self, price, name, weight):
        super().__init__(price, name, "Food")
        self.weight = weight


class Games(Item):
    """ Games that the user can purchase."""
    def __init__(self, price, name, numPlayers, genre):
        super().__init__(price, name, "Games")
        self.numPlayers = numPlayers
        self.genre = genre


class Computers(Item):
    """ Computers that the user can purchase."""
    def __init__(self, price, name, color, displaySize):
        super().__init__(price, name, "Computers")
        self.color = color
        self.displaySize = displaySize
