# Rock Paper Scissors Game
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

game_images = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n\n"))

computer_choice = random.randint(0, 2)

if player_choice == 0:
  print(game_images[0])
elif player_choice == 1:
  print(game_images[1])
else:
  print(game_images[2])

print("\nComputer Chose: \n")

if computer_choice == 0:
  print(game_images[0])
elif computer_choice == 1:
  print(game_images[1])
else:
  print(game_images[2])

if player_choice == 0 and computer_choice == 1:
  print("You Lose")
elif player_choice == 0 and computer_choice == 2:
  print("You Win")
elif player_choice == 1 and computer_choice == 0:
  print("You Win")
elif player_choice == 1 and computer_choice == 2:
  print("You Lose")
elif player_choice == 2 and computer_choice == 0:
  print("You Lose")
elif player_choice == 2 and computer_choice == 1:
  print("You Win")
else: 
  print("Tie Game")