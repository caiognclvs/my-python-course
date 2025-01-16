import random
import sys
from enum import Enum

# value = input("Please enter a value: ")
# while True:
#     playerchoice = input("Enter...\n1 for Rock\n2 for Paper\n3 for Scissors\n\n")
#     if type(playerchoice) != str:
#         print("You must enter 1, 2 or 3")
#     else:
#         break
#     while True:
#         if playerchoice < 1 or playerchoice > 3:
#             print("You must enter 1, 2 or 3")
#         else:
#             break

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playagain = True

while playagain:
    playerchoice = input("\nEnter...\n1 for Rock\n2 for Paper\n3 for Scissors\n\n")
    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2 or 3")

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("\nYou chose " + str(RPS(player)).replace('RPS.', ''))
    print("Python chose " + str(RPS(computer)).replace('RPS.', '') + "\n")

    if player == 1 and computer == 3:
        print("You win!")
    elif player == 2 and computer == 1:
        print("You win!")
    elif player == 3 and computer == 2:
        print("You win!")
    elif player == computer:
        print("Tie game!")
    else:
        print("Python wins!")
    
    playagain = input("\nPlay again? \nY for yes\n Q to quit\n\n")
    if playagain.lower() == "y":
        continue
    else:
        print("\nThank you for playing!")
        break

sys.exit("Bye!")