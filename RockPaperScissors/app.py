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


def signal_handler(sig, frame):
    """Signal Handler when ctrl + c is pressed of SIGINT."""
    print("\nGood bye.")
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
                print(
                    f"\nUser '{key_mapping[user_choice]}' beats '{key_mapping[computer_choice]}'. You win :)"
                )
            else:
                print(
                    f"\nComputer '{key_mapping[computer_choice]}' beats '{key_mapping[user_choice]}'. You lose :("
                )
            break

        elif user_choice == "P":
            if computer_choice == "R":
                print(
                    f"\nUser '{key_mapping[user_choice]}' beats '{key_mapping[computer_choice]}'. You win :)"
                )
            else:
                print(
                    f"\nComputer '{key_mapping[computer_choice]}' beats '{key_mapping[user_choice]}'. You lose :("
                )
            break

        elif user_choice == "S":
            if computer_choice == "P":
                print(
                    f"\nUser '{key_mapping[user_choice]}' beats '{key_mapping[computer_choice]}'. You win :)"
                )
            else:
                print(
                    f"\nComputer '{key_mapping[computer_choice]}' beats '{key_mapping[user_choice]}'. You lose :("
                )
            break

        else:
            print("Invalid input. Please enter Rock(R) Paper(P) Scissors(S).\n")
            continue


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    print("Welcome to Rock Paper Scissors game.\n")
    print("Rules: https://en.wikipedia.org/wiki/Rock_paper_scissors\n")
    print("Rock (R)")
    print("Paper (P)")
    print("Scissors (S)\n")

    game()
