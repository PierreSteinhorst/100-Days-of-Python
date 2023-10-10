# number guessing game
from art_number_guessing import logo
from random import randint

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = randint(1, 100)
print(f"Pssst, the correct answer is: {number}")

attempts = 0
difficulty = input("Choose a difficulty. Type 'easy' or 'hard'.").lower()
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
else:
    print("Invalid input!")

game_goes_on = True
while game_goes_on:
    print(f"You have {attempts} remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess < number:
        print("Too low.")
        print("Guess again.")
        attempts -= 1

    elif guess > number:
        print("Too high.")
        print("Guess again.")
        attempts -= 1
    elif guess == number:
        print("You got it!")
        game_goes_on = False

    if attempts == 0:
        print("You've run out of guesses, you lose!")
        game_goes_on = False

