import random

def generate_random():
    return random.randint(1, 10)

def guess_number(number):
    guess = None
    guess = int(input("Guess the number between 1 and 10: \n"))

    while guess != number:
        if guess < number:
            guess = int(input("Too low! Try again.\n"))
        elif guess > number:
            guess = int(input("Too high! Try again.\n"))
    print("Congratulations! You guessed it!")
    rematch = input("Play again? Y/N\n").lower()
    if rematch == "y":
        guess_number(generate_random())



print("Welcome to the number guessing game!")
guess_number(generate_random())