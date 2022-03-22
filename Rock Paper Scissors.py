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
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player == 0:
    print(rock)
elif player == 1:
    print(paper)
elif player == 2:
    print(scissors)
else:
    print("You entered the wrong input")

computer = random.randint(0, 2)
if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
elif computer == 2:
    print(scissors)
else:
    print("You entered the wrong input")
#print(computer)

if (player == 0 and computer == 0) or (player == 1 and computer == 1) or (player == 2 and computer == 2) :
    print("It's a draw.")
elif (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
    print("You lose!")
elif (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
    print("You Won!")
else:
    print("Invalid input")

#comment