class UserInventory:
    def __init__(self):
        """ An inventory that contains all the items that user has bought. """
        self.inventory = list()

    def getInventory(self):
        """ Returns the user's inventory. """
        return self.inventory

    def removeItemFromInventory(self, item):
        """ Removes an item from the inventory. """
        self.inventory.remove(item)

    def addItemToInventory(self, item):
        """ Adds an item to the user's inventory. """
        self.inventory.append(item)