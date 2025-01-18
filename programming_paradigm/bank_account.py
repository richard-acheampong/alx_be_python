# Objective: 
# Understand the fundamentals of OOP in Python by implementing a BankAccount class that encapsulates 
#     banking operations. Use command line arguments to interact with instances of this class.

# Task Description:
# You will create two Python scripts: bank_account.py, which contains the BankAccount class, 
# and main-0.py (bank_account_main), which interfaces with the class through command line arguments to perform banking operations.

class BankAccount:
    def __init__(self, initial_balance = 0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.account_balance = initial_balance

    def validate_amount(self, amount):
        if amount < 0:
            raise ValueError("Invalid amount")
        return amount
    
    def deposit(self, amount):
        try:
            self.validate_amount(amount)
            self.account_balance += amount
            return self.account_balance
        except ValueError as e:
                print(e)

        
    def withdraw(self, amount):
        self.validate_amount(amount)
        if amount > self.account_balance:
            return False
        self.account_balance -= amount
        return self.account_balance
        

    def display_balance(self):
        print(f"Current balance: ${self.account_balance}")

    