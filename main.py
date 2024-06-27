import random
from images import *

game_on = True
computer_score = 0
player_score = 0


def game():
    print(f"Your score= {player_score}, Computer Score= {computer_score}")
    choices = [rock, paper, scissors]
    nums = {0: "ROCK", 1: "PAPER", 2: "SCISSORS"}
    player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if player_choice >= 3 or player_choice < 0:
        print("Please enter a valid input")
    else:

        print(f"You chose: {nums[player_choice]}")
        print(choices[int(player_choice)])
        comp_choice = random.randint(0, 2)
        print(f"Computer chose: {nums[comp_choice]}")
        print(choices[int(comp_choice)])
        checker(player_choice, comp_choice)
    return


def checker(player_choice, comp_choice):
    global player_score, computer_score
    if player_choice == comp_choice:
        print("It's a draw, 1 point for each")
        player_score += 1
        computer_score += 1
    elif (player_choice == 1 and comp_choice == 0) or (player_choice == 2 and comp_choice == 1) or (
            player_choice == 0 and comp_choice == 2):
        print("That's a point for you! You Win!")
        player_score += 1
    else:
        print("Oops! Computer scores!")
        computer_score += 1
    print(f"Your score= {player_score}, Computer Score= {computer_score}")
    return


while game_on:
    play = input("Do you want to play? (Y/N): ")
    if play.lower() == "n":
        print("Goodbye!")
        game_on = False
    elif play.lower() == "y":
        game()
    else:
        print("Please enter a valid input")
