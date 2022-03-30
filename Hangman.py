# To create the hangman game by using the basic data structures in python.
import random
from Hangman_words import word_list
from Hangman_art import stages
from Hangman_art import logo


# Creating a list of words to be guessed
# word_list = ["bombay", "chennai", "delhi", "gorakhpur", "bangalore"]
chosen_word = random.choice(word_list)

print(logo)

# Testing the code
#print(f"The chosen word is: {chosen_word}.")

lives = 6
# Creating blanks
display = []
for i in range(len(chosen_word)):
    display += "_"
    # display.append("_")
# print(display)

count = len(chosen_word)
while count > 0:
    # Input for guessing the letter
    guess = input("Guess a letter: \n").lower()

    if guess in display:
        print(f"You've already guessed the letter {guess}.")

    # Checking the guessed letter
    for pos in range(len(chosen_word)):
        if chosen_word[pos] == guess:
            display[pos] = guess
            count -= 1

    if guess not in chosen_word:
        print(f"The letter {guess} is not in the word. You lose a life!")
        lives -= 1
        print(stages[lives])
        if lives == 0:
            print("You lose!")
            break

    print(" ".join(display))

if count == 0:
    print("You win!")
