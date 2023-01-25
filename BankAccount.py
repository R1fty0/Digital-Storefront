class BankAccount:

    def __init__(self, initialDeposit, password):
        self.balance = float(initialDeposit)
        self.password = password
        self.identityConfirmed = False

    # Returns true if you have more balance than cost, false if you don't
    def canAfford(self, amount):
        if float(amount) <= self.balance:
            return True
        else:
            return False

    def makePurchase(self, itemAmount, itemName):
        self.checkPassword()  # Checks the user's password
        if self.identityConfirmed:
            print("Identification complete! Glad to see your still around. Making purchase.")
            self.balance = self.balance - float(itemAmount)
            print(f"You have purchased {itemName} for {itemAmount} dollars. Thank you for doing business with us. We hope you will happy with your purchase.")
            self.identityConfirmed = False  # Resets the verification process
        elif self.identityConfirmed is not True:
            print("Either you entered your password wrong or maybe it is not you...suspicious. Purchase Failed. Session Terminated.")

    def balanceReport(self):
        print(f'You have $ {self.balance} left in your account.')

    def checkPassword(self):
        """ Checks the user's password before they make a purchase for security reasons."""
        print("Before we continue, we just need to make sure it is still you shopping, and not someone else!")
        userInput = input("What is your password?: ")
        if userInput.upper() == self.password.upper():
            self.identityConfirmed = True
        else:
            self.identityConfirmed = False

