try:
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
    operation = input("Enter operation (+, -, *, /): ")

    def add(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    def multiply(x, y):
        return x * y
    def divide(x, y):
        return x / y

    if operation == "+":
        print(add(num1, num2))
    elif operation == "-":
        print(subtract(num1, num2))
    elif operation == "*":
        print(multiply(num1, num2))
    elif operation == "/":
        print(divide(num1, num2))

except ValueError:
    print("Not a valid number")
except ZeroDivisionError:
    print("Can't divide by zero")   