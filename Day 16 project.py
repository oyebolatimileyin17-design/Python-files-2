class Bankaccount:
   def __init__(self, owner, balance):
      self.owner = owner
      self.balance = balance

   def deposit(self, amount):
      self.balance = self.balance + amount
      print(f"{self.owner} your account balance is {self.balance}")

   def withdraw(self, amount):
      self.balance = self.balance - amount

   def check_balance(self):
       print(f"{self.owner}'s balance: {self.balance}") 

account1 = Bankaccount("John Doe", 1000)
account2 = Bankaccount("Mac Book", 4988)

account1.deposit(300)
print(account1.balance)

account2.deposit(5939)
print(account2.balance)

account1.withdraw(500)
print(account1.balance)

account2.withdraw(3000)
print(account2.balance)