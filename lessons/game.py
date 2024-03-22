"""Number Guessing Game."""
from random import randint

SECRET: int = randint(1,10)
correct: bool = False

while not correct:
    guess: int = int(input("Guess a number: "))

    if guess == SECRET:
        print (f"Correct! {guess} is the number!")
        correct = True
    else:
        print("Guess again!")