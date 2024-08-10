import random
import sys

figures = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
"""
    _______
---'   ________)
          ______)
          _______)
         _______)
---.__________)
""",
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

computer_choice = random.randint(0, 2)

print("Welcome to ROCK, PAPER, SCISSORS")

user_choice = int(input("Enter your choice, 0 for 'Rock', 1 for 'Paper' and 2 for 'Scissors': "))

if user_choice < 0 or user_choice > 2:
    print("Invalid Choice. GAME OVER!!!")
    sys.exit()

if user_choice == computer_choice:
    print("You chose: ")
    print(figures[user_choice] + "\n")
    print("Computer chose: ")
    print(figures[computer_choice] + "\n")
    print("It's a DRAW!!!")
else:
    if user_choice == 0 and computer_choice == 1:
        print("You chose: ")
        print(figures[user_choice] + "\n")
        print("Computer chose: ")
        print(figures[computer_choice] + "\n")
        print("Computer WINS!!!")
    elif user_choice == 0 and computer_choice == 2:
        print("You chose: ")
        print(figures[user_choice] + "\n")
        print("Computer chose: ")
        print(figures[computer_choice] + "\n")
        print("You WIN!!!")
    elif user_choice == 1 and computer_choice == 0:
        print("You chose: ")
        print(figures[user_choice] + "\n")
        print("Computer chose: ")
        print(figures[computer_choice] + "\n")
        print("You WIN!!!")
    elif user_choice == 1 and computer_choice == 2:
        print("You chose: ")
        print(figures[user_choice] + "\n")
        print("Computer chose: ")
        print(figures[computer_choice] + "\n")
        print("Computer WINS!!!")
    elif user_choice == 2 and computer_choice == 0:
        print("You chose: ")
        print(figures[user_choice] + "\n")
        print("Computer chose: ")
        print(figures[computer_choice] + "\n")
        print("Computer WINS!!!")
    else:
        print("You chose: ")
        print(figures[user_choice] + "\n")
        print("Computer chose: ")
        print(figures[computer_choice] + "\n")
        print("You WIN!!!")

