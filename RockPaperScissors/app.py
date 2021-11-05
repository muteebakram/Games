# -----------------------------------------------------------------------------
# Name      : app.py
# Purpose   : Rock Paper Scissors game.
#
# Author    : Muteeb Akram (muteebakram)
#
# Created   : 5-Nov-2021
# Changes   :
# Copyright : No copyright.
# -----------------------------------------------------------------------------
import sys
import signal
import random

key_mapping = {
    "R": "Rock",
    "P": "Paper",
    "S": "Scissors",
}

USER = "User"
COMPUTER = "Computer"

user_wins = 0
computer_wins = 0


def signal_handler(sig, frame):
    """Signal Handler when ctrl + c is pressed of SIGINT."""
    print("\n")
    if user_wins > computer_wins:
        print("Awesome. You defeated computer.")
    elif user_wins < computer_wins:
        print("Damm!!. computer defeated you.")
    else:
        print("Draw. You equal computer.")
    print(f"You won: {user_wins}, computer won: {computer_wins}. Good bye.")
    sys.exit(0)


def validate_choice(choice):
    if not choice:
        return False

    if choice == "R" or choice == "P" or choice == "S":
        return True

    return False


def game():
    while True:
        user_choice = input("You Played: ").upper()
        if not validate_choice(user_choice):
            print("Invalid input. Please enter Rock(R) Paper(P) Scissors(S).\n")
            continue

        computer_choice = random.choice(["R", "P", "S"])
        print(f"Computer played: {computer_choice}")
        if user_choice == computer_choice:
            print(f"Draw!! User and computer played {key_mapping[user_choice]}.\n")
            continue

        # Logic
        # Rock(R) > Scissors(S)
        # Scissors(S) > Paper(P)
        # Paper(P) > Rock(R)

        if user_choice == "R":
            if computer_choice == "S":
                winner = USER
            else:
                winner = COMPUTER

        elif user_choice == "P":
            if computer_choice == "R":
                winner = USER
            else:
                winner = COMPUTER

        elif user_choice == "S":
            if computer_choice == "P":
                winner = USER
            else:
                winner = COMPUTER

        else:
            print("Invalid input. Please enter Rock(R) Paper(P) Scissors(S).\n")
            continue

        if winner == USER:
            global user_wins
            user_wins += 1
            print(
                f"User '{key_mapping[user_choice]}' beats '{key_mapping[computer_choice]}'. You win :)\n"
            )
        elif winner == COMPUTER:
            global computer_wins
            computer_wins += 1
            print(
                f"Computer '{key_mapping[computer_choice]}' beats '{key_mapping[user_choice]}'. You lose :(\n"
            )
        else:
            print("Error: No winner !!")


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    print("Welcome to Rock Paper Scissors game.\n")
    print("Rules: https://en.wikipedia.org/wiki/Rock_paper_scissors\n")
    print("Quit: Ctrl + C\n")
    print("Rock (R)")
    print("Paper (P)")
    print("Scissors (S)\n")

    game()
