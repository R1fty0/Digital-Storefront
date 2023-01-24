from StoreInventory import StoreInventory
from BankAccount import BankAccount
from BuyableItems import Buyable

"""
    Current Task: 
    Improve the Store class’ viewCatalog() method to provide the user a menu to choose which sub-catalog they want to view individually. 
    Advanced: Provide the user another menu to choose which specific item they want to view more details about individually. 
"""

# Initialize inventories
storeInventory = StoreInventory()
myStuff = list()
myShoppingCart = list()

# FUNCTIONS TO MANAGE MENU SYSTEM IN MAIN SHOPPING PROGRAM


def viewCatalog():
    instructions = ["Welcome to the Store Catalog!", "Enter the name of the category you see below would like to view more in detail."]
    for instructions in instructions:
        print(instructions)


def buyItem():
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
        print(f'We have {itemToPurchase.name} in stock!')
        userChoice = int(input('Type 1 to BUY NOW, 2 to place in your shopping cart, or any other key to cancel purchase.'))

        if userChoice == 1:
            makePurchaseFromStore(itemToPurchase)
        elif userChoice == 2:
            print('We will hold onto this item for you. Adding to shopping cart ... ')
            moveItemToShoppingCart(itemToPurchase)
        else:
            print('Purchase cancelled! Sending you back to the storefront ... ')
    else:  # If user-entered item is not found in the store inventory
        print('The item you are looking for is sold out or does not exist. Sorry!')


def reviewMyInventory():
    print('Here is a list of the items you now own: ')
    for item in myStuff:
        print(item.name)


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
    myShoppingCart.append(item)
    storeInventory.removeItemFromInventory(item)


def moveItemFromShoppingCartToInventory(item):
    storeInventory.restockItemToInventory(item)
    myShoppingCart.remove(item)


def makePurchaseFromStore(item):
    # If you can afford the item, buy it and remove it from the store
    if myBankAccount.canAfford(item.price):
        myBankAccount.makePurchase(item.price)
        print(f'Purchase complete! You now own {item.name}')
        myStuff.append(item)
        storeInventory.removeItemFromInventory(item)
    else:
        print('You can\'t afford this item ... ')


def makePurchaseFromShoppingCart(item):
    # If you can afford the item, buy it and remove it from the store
    if myBankAccount.canAfford(item.price):
        myBankAccount.makePurchase(item.price)
        print(f'Purchase complete! You now own {item.name}')
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
    myBankAccount = BankAccount(deposit, setPassword())

    # Begin shopping
    stillShopping = True

    Menu(stillShopping)


def Menu(stillShopping):
    while stillShopping:
        print("\n****************************************************** ")
        print("Please choose from one of the following menu options: ")
        print("1. View catalog of items to buy")
        print("2. Buy an item")
        print("3. View your cart of held items")
        print("4. Review the items you already own")
        print("5. View the status of your financials")
        print("6. Open the Store's Visual Interface.")
        print("7. Exit program")

        userChoice = int(input())

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
            startVisualStore()
        elif userChoice == 7:
            print('Thanks for shopping! Now exiting program ... ')
            stillShopping = False
        else:
            print('Incorrect input! Please choose again.')


def setPassword():
    """ Sets a password for the user's bank account. """
    password = input('Please enter a password for your account: ')
    confirmPassword = input('Please input your password one more time to confirm it!')
    if password != confirmPassword:
        print('Your passwords to not match ... ')
        setPassword()
    else:
        print('Password set! Your account is now ready!')
        return password


def startVisualStore():
    """ Opens the Store's Visual Window. """
    import VisualStore
    VisualStore.Store()

if __name__ == "__main__":
    Setup()
