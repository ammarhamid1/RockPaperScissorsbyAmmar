from random import choice

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
is_player_win = False
is_draw = False

print("================================================================")
print("            Rock Paper Scissors Game by Ammar Hamid")
print("================================================================")
player_move = input("Choose [r]ock, [p]aper or [s]cissors:")
print("----------------------------------------------------------------")
player_move.lower()

if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    raise SystemExit("Invalid input! Try again.")
computer_move = choice([rock, paper, scissors])

print(f"You choose {player_move}!")
print(f"The computer chooses: {computer_move}!")

if player_move == computer_move:
    is_draw = True
if (player_move == rock and computer_move == scissors) \
        or (player_move == paper and computer_move == rock) \
        or (player_move == scissors and computer_move == paper):
    is_player_win = True
else:
    is_player_win = False

if is_draw:
    print("Draw!")
elif is_player_win:
    print("You won!")
else:
    print("You lost!")
print("================================================================")
print("      Thank you for the game! /SoftUni Fundamentals 2024/")
print("================================================================")
