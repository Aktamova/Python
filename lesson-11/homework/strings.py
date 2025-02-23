bank account

account = 0

deposit = account +=any deposit

withdrawal = account -=any withdrawal (if withdrawal money > account, then print 'not enough money in balance')

check_balance = need to check money inside of account
class BankAccount:
    def __init__(self, initial_balance=0.0):
        self._balance = initial_balance  

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Deposited: ${amount:.2f}. New balance: ${self._balance:.2f}"
        return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self._balance:
                self._balance -= amount
                return f"Withdrew: ${amount:.2f}. Remaining balance: ${self._balance:.2f}"
            return "Error: Insufficient funds."
        return "Withdrawal amount must be positive."

    def get_balance(self):
        return self._balance

account = BankAccount(100)  
account.deposit(100)
account.get_balance()
account.withdraw(150)



create a function that will find sum of digits I provide (use for loop)
def sum_digits(*arg):
    sum = 0
    for num in arg:
        sum += num
    print(sum) 

sum_digits(1, 2, 3)
