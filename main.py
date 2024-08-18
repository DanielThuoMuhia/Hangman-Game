import random
import os
from hang_man_words import word_list
from hang_man_art import stages, logo

while True:
    # Clear the terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    # Print the game logo
    print(logo)

    # Choose a random word from the word_list and determine its length
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    lives = 6

    # Create an empty list called display with underscores representing each letter in the chosen_word
    display = []
    for _ in range(word_length):
        display += "_"
    print(display)

    end_of_game = False

    while not end_of_game:
        # Ask the user to guess a letter and convert it to lowercase
        guess = input("Guess a letter: ").lower()

        # Check if the user has already guessed the letter
        if guess in display:
            print(f"You have already guessed {guess}")

        # Check if the guessed letter is in the chosen_word
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        # Print the current state of the display list
        print(f"{' '.join(display)}")

        # If the guessed letter is not in the chosen_word, decrease lives by 1
        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")
                print(f"The word was {chosen_word}")

        # Check if the user has guessed all the letters in the chosen_word
        if "_" not in display:
            end_of_game = True
            print("You win")

        # Print the current stage of the hangman based on the number of lives left
        print(stages[lives])

    # Ask if the user wants to play again
    replay = input("Do you want to play again? (yes/no): ").lower()
    if replay != 'yes':
        break