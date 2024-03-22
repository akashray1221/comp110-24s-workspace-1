"""EX02 - One Shot Battleship"""

__author__ = "730408691"

grid_size: int = 4
secret_row: int = 3
secret_column: int = 2

attack_row: int = int(input("Guess a row: "))
while attack_row > grid_size or attack_row < 1:
    attack_row = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
attack_column: int = int(input("Guess a column: "))
while attack_column > grid_size or attack_column < 1:
    attack_column = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

Blue_Box: str = "\U0001F7E6"
White_Box: str = "\U00002B1C"
Red_Box: str = "\U0001F7E5"
result: str = ""
row_count: int = 1
column_count: int = 1

if attack_row == secret_row and attack_column == secret_column:
    result = Red_Box
else:
    result = White_Box

while row_count <= grid_size:
    row: str = ""
    if attack_row == row_count:
        while column_count <= grid_size:
            if attack_column == column_count:
                row += result
            else:
                row += Blue_Box
            column_count += 1
    else:
        while column_count <= grid_size:
            row += Blue_Box
            column_count += 1
    print (row)
    row_count += 1
if attack_row == secret_row:
    if attack_column == secret_column:
        print ("Hit!")
    else:
        print ("Close! Correct row, wrong column.")
elif attack_column == secret_column:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")