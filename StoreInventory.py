from Items import Category, Clothing, Food, Games, Computers


class StoreInventory:

    def __init__(self):
        """ Contains all the items available for purchase in the store"""
        self.clothingCategory = Category("Clothing")
        self.foodCategory = Category("Food")
        self.gamesCategory = Category("Games")
        self.computersCategory = Category("Computers")

    def getFullInventory(self):
        """ Returns the store's full inventory. """
        return self.clothingCategory.get_inventory() + self.foodCategory.get_inventory() + self.gamesCategory.get_inventory() + self.computersCategory.get_inventory()

    def addItemsToInitialInventory(self):
        """ Adds items to the initial inventory. """
        items = [Food("10.00", "Rice", 2000), Games("69.99", "Super Mario Bros", 1, "Arcade"), Clothing("15.99", "Hoodie", "small"), Computers("999.99", "Apple Macbook Pro", "Blue", "1280x1080")]
        for item in items:
            if type(item) == Food:  # Adds food items to the food category.
                self.foodCategory.stockItemToInventory(item)
            if type(item) == Games:  # Adds food items to the game category.
                self.gamesCategory.stockItemToInventory(item)
            if type(item) == Clothing:  # Adds food items to the clothing category.
                self.clothingCategory.stockItemToInventory(item)
            if type(item) == Computers:  # Adds food items to the computer category.
                self.computersCategory.stockItemToInventory(item)

    def addNewItemToCategory(self):
        """ Adds a new item to the desired inventory."""
        pass




