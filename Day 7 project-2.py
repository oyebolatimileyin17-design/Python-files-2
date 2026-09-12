import random
options = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(options)
user_choice = input("Enter your choice (Rock, Paper, Scissors): ")
print(f"Computer choose: {computer_choice}")
print(f"You choose: {user_choice}")
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "Rock" and computer_choice == "Scissors") or \
     (user_choice == "Paper" and computer_choice == "Rock") or \
     (user_choice == "Scissors" and computer_choice == "Paper"):
    print("You win!")
else:
    print("Computer wins!")
