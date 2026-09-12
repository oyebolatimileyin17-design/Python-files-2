contacts = {}

contacts["mum"] = "07016108620"
contacts["friend"] = "08104313289"
contacts["dad"] = "08035364857"
contacts["Self"] = "08129480675"
contacts["cousin"] = "07015156720"

def add_contacts(name, number):
    contacts[name] = number
    print(f"{name} added.")

def search_contacts(name):
    try:
        print(f"{name}'s number: {contacts[name]}")
    except KeyError:
        print("Contact Doesn't exist")

while True:
    choice = input("Choose: (1) Add contact (2) Search contacts (3) Quit: ")
    if choice == "1":
        name = input("Enter the person name:")
        number = input("Enter the person number:")
        add_contacts(name, number)
    elif choice == "2":
         name = input("Enter the person's name:")
         search_contacts(name)
    elif choice == "3":
        break
    else:
        print("Invalid choice, try again.")
        SyntaxError