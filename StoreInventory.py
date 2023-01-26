from Items import Category, Clothing, Food, Games, Computers

class StoreInventory:
    def __init__(self, recentlyPurchasedMemoryLimit):
        """ Contains all the items available for purchase in the store"""
        self.clothingCategory = Category("Clothing")
        self.foodCategory = Category("Food")
        self.gamesCategory = Category("Games")
        self.computersCategory = Category("Computers")
        self.soldItems = list()
        self.recentlyPurchasedMemoryLimit = recentlyPurchasedMemoryLimit

    def getFullInventory(self):
        """ Returns the store's full inventory. """
        return self.clothingCategory.getInventory() + self.foodCategory.getInventory() + self.gamesCategory.getInventory() + self.computersCategory.getInventory()

    def addItemsToInitialInventory(self):
        """ Adds items to the initial inventory. """
        inventoryToAddTo = None  # Placeholder for the inventory to add the item.
        items = [Food("10.00", "Rice", 2000), Games("69.99", "Super Mario Bros", 1, "Arcade"),
                 Clothing("15.99", "Hoodie", "small"), Computers("999.99", "Apple Macbook Pro", "Blue", "1280x1080")]
        for item in items:
            if type(item) == Food:
                inventoryToAddTo = self.foodCategory
            if type(item) == Games:
                inventoryToAddTo = self.gamesCategory
            if type(item) == Clothing:
                inventoryToAddTo = self.clothingCategory
            if type(item) == Computers:
                inventoryToAddTo = self.computersCategory
            inventoryToAddTo.stockItemToInventory(item)  # Adds item to inventory

    def removeItemFromInventory(self, item):
        """ Removes an item from the category's inventory that the item belongs to. """
        inventoryToRemoveFrom = None  # Placeholder for the inventory that the item will be removed from
        try:
            if type(item) == Food:  # if the item is belongs to the food category
                inventoryToRemoveFrom = self.foodCategory
            if type(item) == Games:  # if the item is belongs to the games category
                inventoryToRemoveFrom = self.gamesCategory
            if type(item) == Clothing:  # if the item is belongs to the clothing category
                inventoryToRemoveFrom = self.clothingCategory
            if type(item) == Computers:  # if the item is belongs to the computers category
                inventoryToRemoveFrom = self.computersCategory
            inventoryToRemoveFrom.removeItemFromInventory(item)  # Removes item from corresponding inventory
        except AttributeError:
            print("The item you have chosen does not belong to any of the store's inventories. Purchase Failed. Sorry!")

    def returnItemToInventory(self, item):
        """ Returns an item to its corresponding inventory. """
        inventoryToReturnTo = None  # Placeholder for the inventory that the item will be removed from
        try:
            if type(item) == Food:  # if the item is belongs to the food category
                inventoryToReturnTo = self.foodCategory
            if type(item) == Games:  # if the item is belongs to the games category
                inventoryToReturnTo = self.gamesCategory
            if type(item) == Clothing:  # if the item is belongs to the clothing category
                inventoryToReturnTo = self.clothingCategory
            if type(item) == Computers:  # if the item is belongs to the computers category
                inventoryToReturnTo = self.computersCategory
            inventoryToReturnTo.removeItemFromInventory(item)  # removes item from inventory
        except AttributeError:
            print("The item you have tried to return has some issue prevent this from happening. Return Attempt Failed")





