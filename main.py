# Import the random module to generate random choices:
import random

# Create a list of possible choices for the game:
possible_choices = ["Rock", "Scissors", "Paper"]

# Prompt the user to enter their choice:
user_choice = input("Choose Rock, Paper, or Scissors: ")

# Get the computer's choice randomly from the possible choices:
computer_choice = random.choice(possible_choices)

# Print the user's choice and the computer's choice:
print("Your choice: ", user_choice)
print("Computer choice: ", computer_choice)

# Determine the winner based on the rules of Rock, Paper, Scissors:
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "Rock" and computer_choice == "Scissors":
    print("You win!") 
elif user_choice == "Paper" and computer_choice == "Rock":
    print("You win!")
elif user_choice == "Scissors" and computer_choice == "Paper":
    print("You win!") 
else:
    print("Computer wins!")
