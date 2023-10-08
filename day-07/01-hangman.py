
import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
end_of_game = False
lives = 6
print(hangman_art.logo)

display = []
for letter in chosen_word:
    display.append("_")

while not end_of_game:
    guess = input("Please guess a letter: ").lower()
    if guess in display:
        print("You have already guessed the letter.")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print("Your letter is not in the word! You loose a life.")
        lives -= 1
        if lives == 0:
            print("You loose")
            end_of_game = True
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win!")
    print(hangman_art.stages[lives])
