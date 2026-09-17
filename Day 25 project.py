class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def check_balance(self):
        print(f"{self.owner}'s balance: {self.balance}")


# Tests
account = BankAccount("Test User", 1000)

account.deposit(500)
assert account.balance == 1500, "Deposit didn't work correctly"

account.withdraw(200)
assert account.balance == 1300, "Withdraw didn't work correctly"

print("All tests passed!")