import random
secret_number = random.randint(1, 20)
guess  = 0
while guess != secret_number:
    guess = int(input("Guess the number between 1 and 20: "))
    if guess > secret_number:
        print("Number too Big Try again !!")
    elif guess < secret_number:
        print("Number is too small Try again !!")
    else:
        print("You are correct!! The number is", secret_number)