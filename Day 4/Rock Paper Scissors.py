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

figures = [rock, paper, scissors]
figures_text = ["rock", "paper", "scissors"]

player_decision = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
computer_decision = random.choice(figures)

if 0 <= player_decision <= 2:
    print(f"You chose {figures_text[player_decision]}: {figures[player_decision]}")

if player_decision == 0:
    print(f"Computer chose {figures_text[figures.index(computer_decision)]}:{computer_decision}")
    if computer_decision == scissors:
        print("You win!")
    elif computer_decision == paper:
        print("You lose!")
    else:
        print("Draw!")

elif player_decision == 1:
    print(f"Computer chose {figures_text[figures.index(computer_decision)]}:{computer_decision}")
    if computer_decision == scissors:
        print("You lose!")
    elif computer_decision == rock:
        print("You win!")
    else:
        print("Draw!")

elif player_decision == 2:
    print(f"Computer chose {figures_text[figures.index(computer_decision)]}:{computer_decision}")
    if computer_decision == paper:
        print("You win!")
    elif computer_decision == rock:
        print("You lose!")
    else:
        print("Draw!")

else:
    print("Wrong Choice!")
