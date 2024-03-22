"""EX01 - Simple Battleship - A cute step toward Battleship."""
 
__author__ = "730408691"

ship: str = input("Pick a secret boat location between 1 and 4: ")
ship_location: int = int(ship)

#If ship_location is not bw 1 & 4 -> Print an error message

if ship_location > 4:
    print("Error! " + str(ship_location) + " too high!")
    exit()
    
if ship_location < 1:
    print("Error! " + str(ship_location) + " too low!")
    exit()

attack: str = input("Guess a number between 1 and 4: ")
attack_location: int = int(attack)

if attack_location > 4:
    print("Error! " + str(attack_location) + " too high!")
    exit()
    
if attack_location < 1:
    print("Error! " + str(attack_location) + " too low!")
    exit()

Blue_Box: str = "\U0001F7E6"
White_Box: str = "\U00002B1C"
Red_Box: str = "\U0001F7E5"

if attack_location == ship_location:
    if attack_location == 1:
        print(Red_Box + Blue_Box * 3)
    if attack_location == 2:
        print(Blue_Box + Red_Box + Blue_Box * 2)
    if attack_location == 3:
        print(Blue_Box * 2 + Red_Box + Blue_Box)
    if attack_location == 4:
        print(Blue_Box * 3 + Red_Box)
    print("Correct! You hit the ship.")
elif attack_location == 1:
    print(White_Box + Blue_Box * 3)
    print("Incorrect! You missed the ship.")
elif attack_location == 2:
    print(Blue_Box + White_Box + Blue_Box * 2)
    print("Incorrect! You missed the ship.")
elif attack_location == 3:
    print(Blue_Box * 2 + White_Box + Blue_Box)
    print("Incorrect! You missed the ship.")
elif attack_location == 4:
    print(Blue_Box * 3 + White_Box)
    print("Incorrect! You missed the ship.")