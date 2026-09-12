try:
    number = int(input("Enter a number:"))
    print(100 / number)
except ValueError:
    print("That wasn't a valid number olodo boy🤣🤣")
except ZeroDivisionError:
    print("Foolish boy you cant divide anything by zero😑 ")
finally:
    print("You finally got it so you're not a failure afterall")