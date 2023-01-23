class BankAccount:

    def __init__(self, initialDeposit, password):
        self.balance = float(initialDeposit)
        self.password = password

    # Returns true if you have more balance than cost, false if you don't
    def canAfford(self, amount):
        if float(amount) <= self.balance:
            return True
        else:
            return False

    def makePurchase(self, amount):
        if self.checkPassword() and amount <= self.balance:
            self.balance -= amount
            print(f'{amount} spent from your account.')
            print(f'You now have ${self.balance} remaining.')
            return True
        elif not self.checkPassword():
            print("You entered an incorrect password. Please try again later.")
            return False
        else:
            print('You do not have enough funds left to afford this item.')
            return False

    def balanceReport(self):
        print(f'You have $ {self.balance} left in your account.')

    def checkPassword(self):
        passEntry = input('Please enter your password to confirm your identity: ')
        """
            Tells me what the current values are.
        """
        print("User entered:" + str(passEntry))
        print("Password is:" + str(self.password))

        if passEntry == self.password:
            print('Correct Password')
            return True
        elif passEntry != self.password:
            print('Incorrect password!')
            return False
