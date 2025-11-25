from art import logo
import random

def guessed_num():
    num = random.randint(1, 100)
    return num

def diff_level(diff):
    attempts_to_guess = 0
    if diff == "easy":
        return attempts_to_guess + 10
    elif diff == "hard":
        return attempts_to_guess + 5
    else:
        return input("You choose invalid difficulty level. Try once again: ")

game_over = False

while not game_over:
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number = guessed_num()
    attempts = diff_level(input("Choose a difficulty. Type 'easy' or 'hard': "))
    print(f"You have {attempts} remaining to guess the number")
    guess = int(input("Make a guess: "))
    while guess != number:
        if guess < number:
            print("Too low.\nGuess again.")
            attempts -= 1
            print(f"You have {attempts} remaining to guess the number")
            guess = int(input("Make a guess: "))
        elif guess > number:
            print("Too high.\nGuess again.")
            attempts -= 1
            print(f"You have {attempts} remaining to guess the number")
            guess = int(input("Make a guess: "))
        if attempts == 0:
            game_over = True
            print(f"You've run out of guesses. The guessed number was {number}")
        if guess == number:
            game_over = True
            print(f"You got it! The answer was {number}")


