try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
        print(result)
    elif operation == "-":
        result = num1 - num2
        print(result)
    elif operation == "*":
        result = num1 * num2
        print(result)
    elif operation == "/":
        result = num1 / num2
        print(result)

    if result % 2 == 0:
        print("The answer is even")
    else:
        print("The answer is odd")

except ValueError:
    print("That's not a correct value entered")
except ZeroDivisionError:
    print("You can't divide by zero")