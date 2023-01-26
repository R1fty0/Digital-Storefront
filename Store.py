from StoreInventory import StoreInventory
from BankAccount import BankAccount
from Items import Item
from UserInventory import UserInventory
Border = "****************************************************************************************************"


"""
    Current Tasks: 
    Tier 2:  Improve the reviewMyStuff() method, which pulls data from the list that contains all of the items you have bought, 
    to contain a lot more functionality. Instead of just reporting everything the user has bought all at once, provide a more customized experience that gives the user more choice and information when reviewing their stuff. 
    Hint: You may need to adjust how the user’s bought items are stored and tracked to provide access to certain information. 	 	
"""

# Initialize inventories
storeInventory = StoreInventory(3)
myStuff = UserInventory()
myShoppingCart = list()


"""
    # FUNCTIONS TO MANAGE MENU SYSTEM IN MAIN SHOPPING PROGRAM
"""


def returnItemToStore(item):
    """ Returns an item to the store and refunds the user their money."""
    myStuff.removeItemFromInventory(item)  # Removes the item from the user's inventory
    storeInventory.returnItemToInventory(item)  # Returns the item to the store
    myBankAccount.refundItem(item)  # Gives the user a refund


def viewRecentPurchases():
    """ Allows the user to view the most recent purchases they made and return any of those items. """
    listOfPurchases = storeInventory.soldItems
    if len(listOfPurchases) > int(storeInventory.recentlyPurchasedMemoryLimit) - 1:  # Removes an item from the inventory list to ensure that the recentPurchasedMemoryLimit is not exceeded.
        listOfPurchases.remove(storeInventory.recentlyPurchasedMemoryLimit)
    if len(listOfPurchases) != 0:
        print("Here is the list of items you most recently purchased:")
        for item in listOfPurchases:
            print(f"- You purchased the item {item.name} for {item.price} dollars from the {item.category} category.")
        options = ["If you would like to return an item, press 1.",
                   "If you would like to return to the main menu, press any other key."]
        for text in options:
            print(text)
        choice = input("What would you like to do?: ")
        try:
            if int(choice) == 1:
                itemToReturn = input("What is the name of the item you would like to return: ")
                for items in listOfPurchases:  # Returns item to store
                    if items.name.upper() == itemToReturn.upper():
                        returnItemToStore(items)
        except ValueError:
            print("Returning to main menu.")
    else:  # If there is no purchases made by the user, returns user to main menu.
        print("Looks like you haven't purchased anything. Nothing to see here...")


def viewItemDetails(inventoryToView):
    """ Enables the user to view an item in more detail. """
    itemToView = input("Enter the name of the item you would like to view in more detail: ")
    try:
        for item in inventoryToView.getInventory():
            if itemToView.upper() == item.name.upper():
                print("Here is the details of the item you selected:")
                item.viewDetails()
    except AttributeError or ValueError:
        for item in inventoryToView:
            if itemToView.upper() == item.name.upper():
                item.viewDetails()


def viewCatalog():
    """ Shows the user the store's inventory, which contains all items available for purchase. """
    print(Border)
    instructions = ["Welcome to the Store Catalog!",
                    "Enter the name of the category you see below would like to view more in detail."]
    categories = ["- Clothing", "- Food", "- Computers", "- Games"]
    for instructions in instructions:
        print(instructions)
    for instructions in categories:
        print(instructions)
    inventoryToView = None
    category = input("What category would you like to view?: ")
    print(Border)
    try:
        if category.upper() == storeInventory.foodCategory.name.upper():
            inventoryToView = storeInventory.foodCategory
        if category.upper() == storeInventory.gamesCategory.name.upper():
            inventoryToView = storeInventory.gamesCategory
        if category.upper() == storeInventory.clothingCategory.name.upper():
            inventoryToView = storeInventory.clothingCategory
        if category.upper() == storeInventory.computersCategory.name.upper():
            inventoryToView = storeInventory.computersCategory
        print(f"Here are the items available for purchase in the {inventoryToView.name} category.")
        for items in inventoryToView.getInventory():
            print(f"- {items.name}")
        print(Border)
        choice = input(
            "If you would like to view any of these items in more detail, press 1. Otherwise, press any key to exit the catalog.")
        try:
            if int(choice) == 1:
                viewItemDetails(inventoryToView)
        except ValueError:
            print(Border)
            print("Returning to main menu.")

    except AttributeError or ValueError:
        print(Border)
        feedback = ["An error has occurred when identifying what category you are trying to view!",
                    "Press 1 to try again.", "Press any other key to return to the menu."]  # Shows the user their options
        for text in feedback:
            print(text)
        choice = input("What would you like to do?: ")
        try:
            print(Border)
            if int(choice) == 1:
                print("Re-opening the catalog...")
                viewCatalog()
        except ValueError:
            print(Border)
            print("Returning to the main menu menu!")


def buyItem():
    """ Purchases an item a user wants."""
    itemName = input('Please type in the name of the item you wish to buy!: ')

    # Holding variable for the desired item, if found
    itemToPurchase = None

    # Look through the full inventory to see if the item is present
    # Convert both item name and user input to lower case to prevent case issues!
    for item in storeInventory.getFullInventory():
        if item.name.lower() == itemName.lower():
            itemToPurchase = item
            break  # end loop early if a suitable item is found

    # If a suitable item was found, give them the option to buy it!
    if itemToPurchase is not None:
        print(f"We have {itemToPurchase.name} in stock!")
        userChoice = int(input("Press 1 to buy, Press 2 to put item in shopping cart or Press 3 to exit."))
        print(Border)
        if userChoice == 1:
            passwordVerified = myBankAccount.checkPassword()
            if passwordVerified:
                makePurchase(itemToPurchase, "Store")
            else:
                print("Purchase Failed!")
        elif userChoice == 2:  # Adds item to user's shopping cart
            print('We will hold onto this item for you. Adding to shopping cart ... ')
            moveItemTo(itemToPurchase, "shopping cart")
    else:
        print(Border)
        print('Something went wrong!. Purchase cancelled! Sending you back to the storefront ... ')


def reviewMyStuff():
    """ Presents the user with all the items they purchased. """
    print("Here is the list of all the items you own: ")
    print(Border)
    for item in myStuff.getInventory():
        print(item)
    choice = input("If you would like to view any of these items in more detail, press 1. Otherwise, press any key to exit your inventory.")
    print(Border)
    if int(choice) == 1:
        viewItemDetails(myStuff.getInventory())  # View item details
    else:
        print("Returning to main menu.")


def reviewFinancials():
    """ Shows the user how much their balance is. """
    myBankAccount.balanceReport()
    print(Border)


def reviewMyShoppingCart():
    if len(myShoppingCart) > 0:
        print('Here are all of the items being held in your shopping cart: ')
        print(Border)
        for item in myShoppingCart:
            print(f"- {item.name}")

        # Check to see if the user wants to purchase anything currently in their shopping cart
        userChoice = int(input('Would you like to purchase any held items now? 1 for YES or any other key for NO'))
        try:
            if userChoice == 1:
                buyItemInShoppingCart()  # Buy item from shopping cart
        except ValueError:
            print('Leaving shopping cart as is and returning to the storefront ... ')

    else:  # If cart is empty
        print('Your shopping cart is empty! Nothing to see here ... ')


def buyItemInShoppingCart():
    # Ask user what they want to buy
    userChoice = input('Type in the name of the item you want to buy from the shopping cart: ')

    # Compare user requested name with cart entry names and offer a purchasing offer if there is a match
    itemInCart: Item
    for itemInCart in myShoppingCart:  # Find item in shopping cart
        if itemInCart.name.lower() == userChoice.lower():
            makePurchase(itemInCart, "Shopping cart")  # Buy item
        else:
            print('Item could not be found in shopping cart ... ')


def removeItemFromShoppingCart():
    """ Removes a selected item from the user's shopping cart. """
    userChoice = input('Which item would you like to remove from your shopping cart?')  # Ask user for item they want to remove

    # Compare user requested name with cart entry names and remove item if found
    itemInCart: Item
    for itemInCart in myShoppingCart:
        if itemInCart.name.lower() == userChoice.lower():  # Find item in shopping cart
            print(f'You have removed {itemInCart.name} from your shopping cart!')
            moveItemTo(itemInCart, "user inventory")  # Remove item
        else:
            print('Item could not be found in your shopping cart. Nothing was removed.')


def moveItemTo(item, destination):
    """ Moves a selected item to the given destination."""
    if destination.lower() == "shopping cart":  # Remove item from store into shopping
        storeInventory.removeItemFromInventory(item)
        myShoppingCart.append(item)
        print(f"The item {item.name} has been moved to your shopping cart.")
    elif destination.lower() == "user inventory":  # Remove item from shopping cart into user inventory
        myShoppingCart.remove(item)
        myStuff.addItemToInventory(item)
        print(f"The item {item.name} has been purchased from your shopping cart..")


def makePurchase(item, purchasedFrom):
    """ Allows the user to purchase an item from either the store's catalog or their shopping cart. """
    # If you can afford the item, buy it and remove it from the store
    if myBankAccount.canAfford(item.price):  #
        myBankAccount.makePurchase(item.price, item.name)
        print(f'Purchase complete! You now own {item.name}.')
        myStuff.addItemToInventory(item)
        storeInventory.soldItems.append(item)  # Adds item to memory containing bought items
        if purchasedFrom.lower() == "shopping cart":
            myShoppingCart.remove(item)   # Removes item from shopping cart
        elif purchasedFrom.lower == "store":
            storeInventory.removeItemFromInventory(item)  # Removes item from store's inventory
    else:
        print('You can\'t afford this item ... ')


"""
    # PROGRAM BEGINS HERE

"""


def Setup():
    """ Sets up an account for the user before starting the storefront """
    print('Welcome to my storefront!')
    # setup bank account
    print('To begin, please set up a bank account.')
    deposit = input('How much do you want to deposit into your account?: ')
    global myBankAccount
    myBankAccount = BankAccount(deposit)

    # Begin shopping
    stillShopping = True
    Menu(stillShopping)


def Menu(stillShopping):
    storeInventory.addItemsToInitialInventory()    # Populates initial inventories.

    menu = ["Please choose from one of the following menu options: ",
            "1. View catalog of items to buy",
            "2. Buy an item",
            "3. View your cart of held items",
            "4. Review the items you already own.",
            "5. View the status of your financials.",
            "6. View the most recent items you purchased and return any of those items." , "7. Exit program."]
    while stillShopping:

        for instructions in menu:  # Shows menu options
            print(instructions)
            print(Border)

        userChoice = input("What would you like to do?: ")

        try:
            userChoice = int(userChoice)
            if userChoice == 1:
                viewCatalog()
            elif userChoice == 2:
                buyItem()
            elif userChoice == 3:
                reviewMyShoppingCart()
            elif userChoice == 4:
                reviewMyStuff()
            elif userChoice == 5:
                reviewFinancials()
            elif userChoice == 6:
                viewRecentPurchases()
            elif userChoice == 7:
                print('Thanks for shopping! Now exiting program ... ')
                stillShopping = False
                print(Border)
        except ValueError:
            print("Something went wrong. Please try again.")


if __name__ == "__main__":
    """ Program starts here. """
    Setup()
