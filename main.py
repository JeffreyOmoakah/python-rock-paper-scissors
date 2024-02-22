import random

possible_choice = ["Rock", "Scissor", "Paper"]
user_choice = input("Choose Rock, Paper, or Scissors: ")
computer_choice = random.choice(possible_choice)

print("Your choice: ", user_choice)
print("Computer choice: ", computer_choice)

if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "Rock" and computer_choice == "Scissor":
    print("You win")
elif user_choice == "Paper" and computer_choice == "Rock":
    print("You win")
elif user_choice == "Scissor" and computer_choice == "Paper":
    print("You win")
else:
    print("Computer wins!")