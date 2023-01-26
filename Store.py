from StoreInventory import StoreInventory
from BankAccount import BankAccount
from Items import Item


"""
    Current Tasks: 
    Tier 2:  Improve the reviewMyStuff() method, which pulls data from the list that contains all of the items you have bought, 
    to contain a lot more functionality. Instead of just reporting everything the user has bought all at once, provide a more customized experience that gives the user more choice and information when reviewing their stuff. 
    Hint: You may need to adjust how the user’s bought items are stored and tracked to provide access to certain information. 	 	
    Tier 3: (viewCatalog) Provide the user another menu to choose which specific item they want to view more details about individually. 
"""

# Initialize inventories
storeInventory = StoreInventory(3)
myStuff = list()
myShoppingCart = list()


"""
    # FUNCTIONS TO MANAGE MENU SYSTEM IN MAIN SHOPPING PROGRAM
"""


def viewRecentPurchases():
    """ Allows the user to view the most recent purchases they made. """
    listOfPurchases = storeInventory.soldItems
    if len(listOfPurchases) != 0:
        print("Here is the list of items you most recently purchased:")
        for item in listOfPurchases:
            print(f"- You purchased the item {item.name} for {item.price} dollars.")
            listOfPurchases.remove(item)
    else:  # If there is no purchases made by the user.
        print("Looks like you haven't purchased anything. Nothing to see here...")


def viewCatalog():
    instructions = ["Welcome to the Store Catalog!",
                    "Enter the name of the category you see below would like to view more in detail."]
    categories = ["- Clothing", "- Food", "- Computers", "- Games"]
    for instructions in instructions:
        print(instructions)
    for instructions in categories:
        print(instructions)
    category = input("What category would you like to view?: ")
    print("\n****************************************************** ")
    storeInventory.displayCategory(category)


def buyItem():
    """ Purchases an item a user wants."""
    itemName = input('Please type in the name of the item you wish to buy!')

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
        if userChoice == 1:
            passwordVerified = myBankAccount.checkPassword()
            if passwordVerified:
                makePurchaseFromStore(itemToPurchase)
            else:
                print("Purchase Failed!")
        elif userChoice == 2:
            print('We will hold onto this item for you. Adding to shopping cart ... ')
            moveItemToShoppingCart(itemToPurchase)
    else:
        print('Something went wrong!. Purchase cancelled! Sending you back to the storefront ... ')


def reviewMyInventory():
    food = list()
    clothes = list()
    computers = list()
    games = list()
    """ Shows the user all the items in each category they own. """
    for item in myStuff:
        # if item.name.lower() ==
        pass


def reviewFinancials():
    myBankAccount.balanceReport()


def reviewMyShoppingCart():
    if len(myShoppingCart) > 0:
        print('Here are all of the items being held in your shopping cart: ')
        for item in myShoppingCart:
            print(item.name)

        # Check to see if the user wants to purchase anything currently in their shopping cart
        userChoice = int(input('Would you like to purchase any held items now? 1 for YES or any other key for NO'))

        if userChoice == 1:
            buyItemInShoppingCart()
        else:
            print('Leaving shopping cart as is and returning to the storefront ... ')

    else:  # If cart is empty
        print('Your shopping cart is empty! Nothing to see here ... ')


def buyItemInShoppingCart():
    userChoice = input('Type in the name of the item you want to buy from the shopping cart: ')

    # Compare user requested name with cart entry names and offer a purchasing offer if there is a match
    itemInCart: Buyable
    for itemInCart in myShoppingCart:
        if itemInCart.name.lower() == userChoice.lower():
            makePurchaseFromShoppingCart(itemInCart)
        else:
            print('Item could not be found in shopping cart ... ')


def removeItemFromShoppingCart():
    userChoice = input('Which item would you like to remove from your shopping cart?')

    # Compare user requested name with cart entry names and remove item if found
    itemInCart: Buyable
    for itemInCart in myShoppingCart:
        if itemInCart.name.lower() == userChoice.lower():
            print(f'You have removed {itemInCart.name} from your shopping cart!')
            moveItemFromShoppingCartToInventory(itemInCart)
        else:
            print('Item could not be found in your shopping cart. Nothing was removed.')


def moveItemToShoppingCart(item):
    """ Moves a selected item to the user's shopping cart."""
    myShoppingCart.append(item)
    storeInventory.removeItemFromInventory(item)


def moveItemFromShoppingCartToInventory(item):
    """ Moves a selected item to the user's inventory after they purchase an item from their shopping cart."""
    storeInventory.restockItemToInventory(item)
    myShoppingCart.remove(item)


def makePurchaseFromStore(item):
    # If you can afford the item, buy it and remove it from the store
    if myBankAccount.canAfford(item.price):
        myBankAccount.makePurchase(item.price, item.name)
        print(f'Purchase complete! You now own {item.name}.')
        myStuff.append(item)
        storeInventory.removeItemFromInventory(item)
    else:
        print('You can\'t afford this item ... ')


def makePurchaseFromShoppingCart(item):
    # If you can afford the item, buy it and remove it from the store
    if myBankAccount.canAfford(item.price):
        myBankAccount.makePurchase(item.price, item.name)
        print(f'Purchase complete! You now own {item.name}.')
        myStuff.append(item)
        myShoppingCart.remove(item)
    else:
        print('You can\'t afford that item ... ')


"""
    # PROGRAM BEGINS HERE

"""


def Setup():
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
    menu = ["\n******************************************************"
            "\nPlease choose from one of the following menu options: ", "1. View catalog of items to buy",
            "2. Buy an item",
            "3. View your cart of held items", "4. Review the items you already own",
            "5. View the status of your financials",
            "6. View the most recent items you purchased."
            , "7. Exit program"]

    while stillShopping:

        for instructions in menu:
            print(instructions)
        userChoice = int(input("What would you like to do?"))

        if userChoice == 1:
            viewCatalog()
        elif userChoice == 2:
            buyItem()
        elif userChoice == 3:
            reviewMyShoppingCart()
        elif userChoice == 4:
            reviewMyInventory()
        elif userChoice == 5:
            reviewFinancials()
        elif userChoice == 6:
            viewRecentPurchases()
        elif userChoice == 7:
            print('Thanks for shopping! Now exiting program ... ')
            stillShopping = False
        else:
            print('Incorrect input! Please choose again.')


def terminateSession():
    print("Our security measures have determined that you are not the current user that is logged in right now. Session Terminated.")


if __name__ == "__main__":
    """ Program starts here. """
    Setup()
