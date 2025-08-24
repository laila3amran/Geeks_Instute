class BankAccount:
    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.balance = balance
        self.authenticated = False   # user is not logged in yet

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("You must be logged in first!")
        if amount <= 0:
            raise Exception("Deposit must be positive!")
        self.balance += amount
        print(f" Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("You must be logged in first!")
        if amount <= 0:
            raise Exception("Withdrawal must be positive!")
        if self.balance < amount:
            raise Exception("Insufficient funds!")
        self.balance -= amount
        print(f" Withdrew {amount}. New balance: {self.balance}")

    def authenticate(self, username, password):
        """Check login credentials"""
        if self.username == username and self.password == password:
            self.authenticated = True
            print(" Login successful!")
            return True
        else:
            print(" Wrong username or password")
            return False
        

class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password, balance=0, minimum_balance=0):
        super().__init__(username, password, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("You must be logged in first!")
        if amount <= 0:
            raise Exception("Withdrawal must be positive!")
        if self.balance - amount < self.minimum_balance:
            raise Exception(" Cannot go below minimum balance!")
        self.balance -= amount
        print(f" Withdrew {amount}. New balance: {self.balance}")

