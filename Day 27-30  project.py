import json


class Expenses:
  def __init__(self, amount, category):
    self.amount = amount
    self.category = category

expenses = []
def add_expenses(amount, category):
    if amount <= 0:
        print("Amount must be positive.")
        return
    expenses.append(Expenses(amount, category))
    print(f"Added: {amount} for the category of {category}")

def view_expenses():
  for expense in expenses:
      print(f"{expense.category}: {expense.amount}")


def total_spent():
  total = 0 
  for expense in expenses:
    total += expense.amount
  return total

def total_by_category():
    totals = {}
    for expense in expenses:
        totals[expense.category] = totals.get(expense.category, 0) + expense.amount
    return totals
  

def save_expenses():
  with open("expenses.json", "w") as file:
      data = [{"amount": e.amount, "category": e.category} for e in expenses]
      json.dump(data, file)
    
def load_expenses():
  global expenses
  with open("expenses.json", "r") as file:
    data = json.load(file)
    expenses = [Expenses(item["amount"], item["category"]) for item in data]

def show_menu():
    print("\n1. Add Expense")
    print("2. View All Expenses")
    print("3. View Summary")
    print("4. Save & Quit")

def main():
    try:
       load_expenses()
    except (FileNotFoundError, json.JSONDecodeError):
       print("No saved expenses found - starting fresh.")
    while True:
        show_menu()
        choice = input("Choose an option:")

        if choice == "1":
           category = input("Category: ")
           amount_str = input("Amount: ")
           try:
               amount = float(amount_str)
               add_expenses(amount, category)
           except ValueError:
              print("That's not a valid number.")

        elif choice == "2":
         view_expenses()

        elif choice == "3":
             print(f"Total spent: {total_spent():,}")
             print("By category:", total_by_category())

        elif choice == "4":
            try:
               save_expenses()
               print("Saved. Goodbye!")
            except OSError:
               print("Couldn't save file.")
            break
        else:
           print("Invalid choice try again.")

main() #Done

