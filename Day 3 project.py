try:

    num1 = float(input("Enter your first number:"))
    num2 = float(input("Enter your second number:"))
    operation = input("Enter the operation of your choice (+, -, *, / ):")

    if operation == "+":
        answer = num1 + num2
        print(f"The answer is: {answer}")
    elif operation == "-":
        answer = num1 - num2
        print(f"The answer is: {answer}")
    elif operation == "*":
        answer = num1 * num2
        print(f"The answer is: {answer}")
    elif operation == "/":
        answer = num1 / num2
        print(f"The answer is: {answer}")
except ValueError:
    print("That's not a real number")
except ZeroDivisionError:
    print("You can't divide the number by zero")


    