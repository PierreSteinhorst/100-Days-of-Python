from hangman_words import word_list, word_list_ex
from hangman_art import stages, logo
import random

end_of_game = False
lives = 6

print(logo)
print("Welcome to my game: Hangman")

chosen_word = random.choice(word_list)
print(chosen_word)
chosen_word_list = list(chosen_word)
display = []

for letter in chosen_word_list:
    display.append("_")

while not end_of_game:
    guess = input("Please type in your letter you want to choose. ").lower()
    if guess in display:
        print("You have already guessed the letter!")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print("Your letter is not in the word!")
        lives -= 1
        if lives == 0:
            print("You loose!")
            end_of_game = True
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win!")
    print(stages[lives])
