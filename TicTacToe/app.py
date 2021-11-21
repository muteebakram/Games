# -----------------------------------------------------------------------------
# Name      : app.py
# Purpose   : Tic Tac Toe.
#
# Author    : Muteeb Akram (muteebakram)
#
# Created   : 5-Nov-2021
# Changes   :
# Copyright : No copyright.
# -----------------------------------------------------------------------------
import sys
import random
import signal
from time import sleep


class TicTacToe:
    def __init__(self):
        self.player_o = "O"
        self.player_x = "X"
        self.total_games = 0
        self.player_o_wins = 0
        self.player_x_wins = 0
        self.current_player = ""
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def print_board(self):
        """Print's the current state of the board."""
        print(
            f"\n{self.board[0]} | {self.board[1]} | {self.board[2]}\n"
            "--•---•--\n"
            f"{self.board[3]} | {self.board[4]} | {self.board[5]}\n"
            "--•---•--\n"
            f"{self.board[6]} | {self.board[7]} | {self.board[8]}\n"
        )

    def change_turn(self):
        """Change the turn from current player to next player."""
        if self.current_player == self.player_x:
            self.current_player = self.player_o

        elif self.current_player == self.player_o:
            self.current_player = self.player_x

        else:
            print("Invalid turn.")
            sys.exit(1)

    def validate_move(self, move):
        """Validate the move played by current player.

        Args:
            move (string): Input recived from current player.

        Raises:
            ValueError: Invalid input from current player.

        Returns:
            bool: True: Valid position from current player.
                  False: Invalid position from current player.
        """
        try:
            move = int(move) - 1
            if move >= 0 and move <= 8:
                if type(self.board[move]) != int:
                    print(f"Position already played by Player-{self.board[move]}\n")
                    return False

                self.board[move] = self.current_player
                return True

            # Invalid number
            raise ValueError

        except ValueError:
            print(
                f"Invalid input from Player-{self.current_player}."
                " Enter a free available position (1-9).\n"
            )
            return False

    def is_win(self):
        """Check if the game is won by current player.

        Returns:
            bool: True if won else False.
        """
        # Horizontal win check
        if (
            (self.board[0] == self.board[1] == self.board[2] == self.current_player)
            or (self.board[3] == self.board[4] == self.board[5] == self.current_player)
            or (self.board[6] == self.board[7] == self.board[8] == self.current_player)
        ):
            return True

        # Vertical win check
        if (
            (self.board[0] == self.board[3] == self.board[6] == self.current_player)
            or (self.board[1] == self.board[4] == self.board[7] == self.current_player)
            or (self.board[2] == self.board[5] == self.board[8] == self.current_player)
        ):
            return True

        # Diagonal win check
        if (self.board[0] == self.board[4] == self.board[8] == self.current_player) or (
            self.board[6] == self.board[4] == self.board[2] == self.current_player
        ):
            return True

        # No win
        return False

    def is_draw(self):
        """Check if the game is draw.

        Returns:
            bool: True: Game is draw.
                  False: Atleast one position remaining to be played.
        """
        for pos in self.board:
            if type(pos) == int:
                return False

        return True

    def add_points(self):
        """Adds point to respective winner when game is won."""
        if self.current_player == self.player_x:
            self.player_x_wins += 1

        elif self.current_player == self.player_o:
            self.player_o_wins += 1

        else:
            print("Failed to add points.")
            sys.exit(1)

    def print_points(self):
        """Print the score of the overall game."""
        print()
        print("-" * 11, "SCORE", "-" * 11)
        print(
            f"\nTotal games   :\t{self.total_games}\n"
            f"Draws         :\t{self.total_games - self.player_x_wins - self.player_o_wins}\n"
            f"Player-X wins :\t{self.player_x_wins}\n"
            f"Player-O wins :\t{self.player_o_wins}"
        )
        print("-" * 29, "\n")

    def clear_game(self):
        """
        Clear or rest the board when game is draw or won.
        Randomly choice who gets to start the next game.
        """
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.current_player = random.choice([self.player_x, self.player_o])
        print(f"Player-{self.current_player} start game #{self.total_games + 1}")
        self.print_board()
        print("-" * 29)

    def quit_game(self, sig, frame):
        """Quit the game by pressing Ctrl + C

        Args:
            sig (signal): SIGINT (kill -9) signal.
            frame (noidea): noidea
        """
        print()
        self.print_points()

        if self.player_o_wins > self.player_x_wins:
            print("Player-X is Tic Tac Toe champion.")
        elif self.player_x_wins > self.player_o_wins:
            print("Player-O is Tic Tac Toe champion.")
        else:
            print("Draw! Players you need to re-match for ultimate Tic Tac Toe champion.")

        print("\nGood Bye. Have a nice day :)")
        sys.exit(0)


def start():
    game = TicTacToe()
    signal.signal(signal.SIGINT, game.quit_game)
    game.clear_game()

    while True:
        move = input(f"Player-{game.current_player} make a move(1-9): ")
        if not game.validate_move(move):
            continue

        game.print_board()
        if game.is_win() or game.is_draw():
            game.total_games += 1
            if game.is_draw():
                print("Draw game!\n")

            if game.is_win():
                print(
                    f"\nPlayer-{game.current_player} WON the game #{game.total_games}."
                )
                game.add_points()

            game.print_points()
            sleep(2)
            game.clear_game()
            continue

        game.change_turn()
        print("-" * 29)


if __name__ == "__main__":
    print("\nWelcome to Tic Tac Toe.\n")
    print("Rules: https://en.wikipedia.org/wiki/Tic-tac-toe\n")
    print("Quit: Ctrl + C\n")
    start()
