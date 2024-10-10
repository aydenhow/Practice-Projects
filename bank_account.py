# bank_account.py #

class BankAccount:
    balance = 0
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return "%s's account. Balance: $%.2f" % (self.name, self.balance)
    def show_balance(self):
        print("Balance: $%.2f" % self.balance)
    def deposit(self, amount):
        if amount <= 0:
            print("Error! Amount must be a positive value.")
        else:
            print("$%.2f has been deposited." % amount)
            self.balance += amount
            self.show_balance()
    def withdraw(self, amount):
        if amount > self.balance:
            print("Error! Cannot withdraw more than the current balance.")
        else:
            print("$%.2f has been withdrawn." % amount)
            self.balance -= amount
            self.show_balance()

my_account = BankAccount("John Smith")

print(my_account)
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1200)
my_account.deposit(0)
