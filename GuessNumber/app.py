# -----------------------------------------------------------------------------
# Name      : app.py
# Purpose   : Guess the number game.
#
# Author    : Muteeb Akram (muteebakram)
#
# Created   : 5-Nov-2021
# Changes   :
# Copyright : No copyright.
# -----------------------------------------------------------------------------
import sys
import math
import random
import signal
from time import sleep


def signal_handler(sig, frame):
    """Signal Handler when ctrl + c is pressed of SIGINT."""
    print("\nGood bye.")
    sys.exit(0)


def validate_integer(num):
    """Takes a number and tries to convert to integer.

    Args:
        num (string): String that can be converted to integer.

    Returns:
        int: String that is converted to integer.
        False: Invalid input and cannot be converted to integer.
    """

    if not num:
        return False

    try:
        num = int(num)
        if num <= 0:
            print("Zero or negative number is NOT allowed.")
            return False

        return num

    except ValueError:
        return False


def pick_ans(max):
    """Picks an answer for guess game based on upper limit.

    Args:
        max (int): Upper limit of guess game.

    Returns:
        int: Answer to be guessed.
    """
    choice = random.choice([1, 2, 4, 5])
    if choice == 1:
        return int(max / 2)
    elif choice == 2:
        return int(max / 4)
    elif choice == 3:
        return int(max - max / 2)
    elif choice == 4:
        return int(math.sqrt(max))
    else:
        return int(max)


def user_guess_number(max):
    """Guess the number for user.

    Args:
        max (str, int): Upper limit to guess number.
    """
    max = validate_integer(max)
    if not max:
        print("Unkown number, please type a valid integer.")
        return

    count = 0
    guess = -1
    ans = pick_ans(max)
    while guess != ans:
        count += 1
        guess = validate_integer(input(f"\nGuess the number from 1-{max}: "))
        if not guess:
            print(f"Please type a valid integer (1-{max})")
            continue

        if guess > ans:
            print("Guess is too high.")
        elif guess < ans:
            print("Guess is too low.")

    print(f"\nYay! you have guessed the number {ans} correctly in {count} attempts.")
    if count <= 5:
        print("Exceptional perfomance. I bet you can read computer's mind.")


def computer_guess_number(upper_limit=100, ans=None):
    """Guess the number for computer.

    Args:
        max (str, int): Upper limit to guess number.
    """
    upper_limit = validate_integer(upper_limit)
    if not upper_limit:
        print("Unkown number, please type a valid integer.")
        return

    ans = validate_integer(ans)
    if not ans:
        print(f"Unkown number, please type a answer (1-{upper_limit}).")
        return

    count = 0
    guess = 0
    min, max = 1, upper_limit
    while guess != ans:
        count += 1
        guess = random.randrange(min, max)
        if not guess or type(guess) != int:
            print(f"Please type a valid integer (1-{upper_limit})")
            continue

        if guess > ans:
            print("Guess is too high.", end=" ")
            max = guess
        elif guess < ans:
            print("Guess is too low.", end=" ")
            min = guess

        print(f"Computer guessed {guess}.")
        sleep(0.6)

    print(f"\nYay! computer guessed the number {ans} correctly in {count} attempts.")
    if count <= 5:
        print("Exceptional perfomance. I bet computer can read your mind.")


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    print("Welcome to guess the number game.")
    print("\nEnter the player:")
    print("1. User")
    print("2. Computer")

    choice = validate_integer(input("\nWho is playing? "))
    if choice and (choice == 1 or choice == 2):
        if choice == 1:
            max = input("Enter the maximum number of guess game: ")
            user_guess_number(max)
        elif choice == 2:
            upper_limit = input("Enter the maximum number of guess game: ")
            ans = input("Enter the number to be guessed by computer: ")
            computer_guess_number(upper_limit=upper_limit, ans=ans)
    else:
        print("Invalid choice. Enter 1 or 2.")
        exit(0)
