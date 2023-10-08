from art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0


def check_answer(guess, answer, turns):
    '''Checks answer against guess. Returns the number of turns remaining.'''
    if guess > answer:
        print("Too high.")
        return turns -1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")


def check_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    print("Welcome to the game: Number Guessing Game!\n")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)

    turns = check_difficulty()
    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses. You lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()

