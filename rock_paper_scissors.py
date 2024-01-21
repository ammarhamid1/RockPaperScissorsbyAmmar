from random import choice
from colorama import Fore, Style

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
player_wins = 0
computer_wins = 0
draws = 0

while True:
    is_player_win = False
    is_draw = False
    print(Fore.LIGHTMAGENTA_EX + "================================================================")
    print("            Rock Paper Scissors Game by Ammar Hamid")
    print("================================================================")
    player_move = input(Style.RESET_ALL + "Choose [r]ock, [p]aper or [s]cissors:")
    print(Fore.LIGHTMAGENTA_EX + "----------------------------------------------------------------")

    if player_move.lower() == "r":
        player_move = rock
    elif player_move.lower() == "p":
        player_move = paper
    elif player_move.lower() == "s":
        player_move = scissors
    else:
        raise SystemExit("Invalid input! Try again.")
    computer_move = choice([rock, paper, scissors])

    print(Fore.LIGHTBLUE_EX + f"You choose {player_move}!")
    print(Style.RESET_ALL + f"The computer chooses: {computer_move}!")

    if player_move == computer_move:
        is_draw = True
    if (player_move == rock and computer_move == scissors) \
            or (player_move == paper and computer_move == rock) \
            or (player_move == scissors and computer_move == paper):
        is_player_win = True
    else:
        is_player_win = False

    if is_draw:
        print(Fore.LIGHTYELLOW_EX + "Draw!")
        draws += 1
    elif is_player_win:
        print(Fore.GREEN + "You won!")
        player_wins += 1
    else:
        print(Fore.RED + "You lost!")
        computer_wins += 1
    print(Fore.LIGHTMAGENTA_EX + "================================================================")
    print("      Thank you for the game! /SoftUni Fundamentals 2024/")
    print("================================================================")

    play_again = input(Style.RESET_ALL + "[Y]es to Play Again, [R]esult or [Q]uit!: ")
    print(Fore.LIGHTMAGENTA_EX + "----------------------------------------------------------------")
    if play_again.lower() == "y":
        continue
    elif play_again.lower() == "r":
        print(Fore.LIGHTYELLOW_EX + f"Result:\nPlayer - {player_wins}: Computer: {computer_wins}\nDraws: {draws}")
        break
    elif play_again.lower() == "q":
        print("Good Bye!")
        break
    else:
        raise SystemExit("Invalid input! Exiting.")


