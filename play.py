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

options = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if player_choice >= 0 and player_choice <= 2:
    print(options[player_choice])

comp_choice = random.randint(0, 2)
print("Computer chose: ")
print(options[comp_choice])

if player_choice < 0 or player_choice >= 3:
    print("You entered an invalid number.\nYou Lose")
elif player_choice == comp_choice:
    print("It's a draw")
elif player_choice == 0 and comp_choice == 1:
    print("You lose")
elif player_choice == 0 and comp_choice == 2:
    print("You win")
elif player_choice < comp_choice:
    print("You lose")
elif player_choice > comp_choice:
    print("You win")
elif player_choice == 2 and comp_choice == 0:
    print("You lose")
elif player_choice == 2 and comp_choice == 1:
    print("You win")
