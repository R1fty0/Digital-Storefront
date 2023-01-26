
class BankAccount:

    def __init__(self, initialDeposit):
        self.balance = float(initialDeposit)
        self.password = None
        if self.password is None:
            self.set_password()

    # Returns true if you have more balance than cost, false if you don't
    def canAfford(self, amount):
        if float(amount) <= self.balance:
            return True
        else:
            return False

    def makePurchase(self, itemAmount, itemName):
        """ Allows the user to purchase an item from their shopping cart or from the store's inventory."""
        self.balance = self.balance - float(itemAmount)  # Purchases Item
        print(f"You have purchased {itemName} for {itemAmount} dollars. "
              f"Thank you for doing business with us. We hope you will happy with your purchase.")

    def balanceReport(self):
        print(f'You have $ {self.balance} left in your account.')

    def checkPassword(self):
        userEntry = input("Before we continue, what is your password?: ")
        if userEntry.upper() == str(self.password).upper():
            return True
        else:
            print("You entered the wrong password.")
            return False

    def set_password(self):
        """ Sets the password for the user's account."""
        password = input("Before you begin shopping, we need you set up a password for your account! "
                         "What would you like the password to your account to be?:")
        confirmedPassword = input("Re-enter your password to confirm it!:")

        try:  # If the password contains numbers
            if float(password) == float(confirmedPassword):
                self.password = password
                print(f"Your password is {self.password}.")
        except ValueError:  # If the password contains numbers
            if password.upper() == confirmedPassword.upper():
                self.password = password
                print(f"Your password is {self.password}.")
            else:  # If the passwords do not match or are not letters or numbers
                print("The passwords you entered do not match! Please try again.")
                self.set_password()
