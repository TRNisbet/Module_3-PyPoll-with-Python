# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)
print(f"The CPU picked {computer_choice}")

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if (user_choice == "r" and computer_choice == "r") or \
(user_choice == "p" and computer_choice == "p") or \
(user_choice == "s" and computer_choice == "s"):
    print("It is a tie")

elif (user_choice == "r" and computer_choice == "s") or \
(user_choice == "p" and computer_choice == "r") or \
(user_choice == "s" and computer_choice == "p"):
    print("You Win!")

elif (user_choice == "r" and computer_choice == "p") or (user_choice == "p" and computer_choice == "s") or (user_choice == "s" and computer_choice == "r"):
    print("You Lose :(")

else:
    print("You picked an invalid choice, and everyone is laughing at you!")
