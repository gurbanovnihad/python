#!/usr/bin/python3
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

outcomes = [rock, paper, scissors]
usr_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if usr_choice < 0 or usr_choice > 2:
    print("You typed an invalid number, you lose!")

else:
    print(outcomes[usr_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:\n{}".format(outcomes[computer_choice]))

    if usr_choice == 0 and computer_choice == 2:
        print("You Won!")
    elif usr_choice == 2 and computer_choice == 1:
        print("You Won!")
    elif usr_choice == 1 and computer_choice == 0:
        print("You Won!")
    elif usr_choice == computer_choice:
        print("It is a Draw :(, Play Again!")
    else:
        print("You Lost!")

