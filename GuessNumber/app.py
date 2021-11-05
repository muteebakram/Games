# -----------------------------------------------------------------------------
# Name      : app.py
# Purpose   : Guess the number game.
#
# Author    : Muteeb Akram (muteeb_akram)
#
# Created   : 5-Nov-2021
# Changes   :
# Copyright : No copyright.
# -----------------------------------------------------------------------------
import sys
import math
import random
import signal


def signal_handler(sig, frame):
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
            print("Zero and negative number is allowed.")
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


def guess_number(max):
    """Guess the number.

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
        guess = validate_integer(input(f"\nGuess the number from 1-{max}: "))
        if not guess:
            print(f"Please type a valid integer (1-{max})")
            continue

        if guess > ans:
            print("Guess too high.")
        elif guess < ans:
            print("Guess too low.")

        count += 1

    print(f"\nYay! you have guessed the number {ans} correctly in {count} attempts.")
    if (count <= 5):
        print("Exceptional perfomance. I bet you can read my mind.")


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    max = input("Enter the upper limit: ")
    guess_number(max)
