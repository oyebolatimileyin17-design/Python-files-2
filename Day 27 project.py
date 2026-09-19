class Expense:
  def __init__(self, amount, category):
    self.amount = amount
    self.category = category
    expenses = []

def add_expense(amount, category):
    # creates an Expense object, adds it to expenses list
    pass

def show_expenses():
    # loops through expenses, prints each one
    pass

def total_spent():
    # adds up all expense amounts, returns the total
    pass

def total_by_category():
    # groups expenses by category, shows subtotal for each
    pass

def save_expenses():
    # converts expenses list to JSON, writes to file
    pass

def load_expenses():
    # reads JSON file, rebuilds Expense objects
    pass