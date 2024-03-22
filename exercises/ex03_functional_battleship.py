"""Functional Battleship."""

__author__ = "730408691"

import random

Blue_Box: str = "\U0001F7E6"
Red_Box: str = "\U0001F7E5"
White_Box: str = "\U00002B1C"


def input_guess(grid_size: int, line: str) -> int:
    """Return the row/column for the user's guess."""
    assert line == "row" or line == "column"
    guess_ship: int
    if line == "row":
        guess_ship = int(input("Guess the row: "))
    else:
        guess_ship = int(input("Guess the column: "))
    while guess_ship > grid_size or guess_ship <= 0:
        guess_ship = int(input(f"The grid is only {grid_size} by {grid_size}. Please try again: "))
    return guess_ship


def print_grid(grid_size: int, row_guess: int, column_guess: int, guess_accuracy: bool) -> None:
    """Print the game board as colorful boxes."""
    print_row: int = 1
    while print_row <= grid_size:
        emojis: str = ""
        column_count: int = 1
        while column_count <= grid_size:
            if row_guess == print_row and column_guess == column_count:
                if guess_accuracy:
                    emojis += Red_Box
                else:
                    emojis += White_Box
            else:
                emojis += Blue_Box
            column_count += 1
        print(emojis)
        print_row += 1


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Return accuracy of the user's guess."""
    if secret_row == row_guess and secret_column == column_guess:
        return True
    else:
        return False


def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Main game function."""
    turns = 0
    guess_accuracy = False
    while turns < 5 and not guess_accuracy:
        turns += 1
        print(f"=== Turn {turns}/5 ===")
        row_guess = input_guess(grid_size, "row")
        column_guess = input_guess(grid_size, "column")
        confirm = correct_guess(secret_row, secret_column, row_guess, column_guess)
        print_grid(grid_size, row_guess, column_guess, confirm)
        if confirm:
            print(f"Hit! You won in {turns}/5 turns!")
            guess_accuracy = True
        else:
            print("Miss!")
    if not guess_accuracy:
        print("X/5 - Better luck on your next game!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))