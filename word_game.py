# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 12:41:54 2024

@author: Admin
"""

import random

# Print a welcome message for our player
print("****** Welcome to the Word Guess Game *****\nHint: African country names.\n")

# The user is asked to enter their name first
name = input("What is your name? ")
print(f"Good Luck, {name.upper()}!\n")

# List of words (African country names)
words = ['kenya', 'nigeria', 'southafrica', 'egypt', 'ghana', 'uganda', 'morocco', 'rwanda']

while True:
    # Choose one random word from the list of words
    word = random.choice(words)
    guesses = []
    enumerated_character = []
    turns = 12  # Number of turns for the player
    print("Guess the word:\n")

    # Main loop for guessing the word
    while turns > 0:
        failed = 0  # Count of failed attempts to display the word

        # Loop through characters in the word
        for i, character in enumerate(word):
            if i in enumerated_character:
                print(character.upper(), end=" ")  # Display guessed characters
            else:
                print("_", end=" ")  # Display underscores for unguessed characters
                failed += 1

        print()  # Newline for better formatting

        # Check if the player has successfully guessed all the characters
        if failed == 0:
            print(f"Congratulations {name}, You guessed the word: {word.upper()}!")
            break

        # Ask the player to guess a character
        guess = input("Guess a character: ").lower()

        # Validate the input
        if len(guess) != 1:
            print(f"Please enter only a single character. Only {guess[0]} will be taken as a guess")
            guess = guess[0]

        if guess in guesses and all(i in enumerated_character for i, char in enumerate(word) if char == guess):
            print("You have already guessed that character. Try a different one.")
            continue

        guesses.append(guess)  # Add the guess to the list of guessed characters

        # If the guessed character is not in the word
        
        if guess in word:
            for i, character in enumerate(word):
                if character == guess and i not in enumerated_character:
                    enumerated_character.append(i)
                    break
        else:
            turns -= 1
            print(f"Wrong guess! You have {turns} more {'guesses' if turns > 1 else 'guess'} left.")
           

        # If the player runs out of turns
        if turns == 0:
            print(f"Sorry {name}, you lost! The word was {word.upper()}.")

    # Ask the player if they want to play again
    again = input("Play again? (Y/N): ").upper()
    if again == "N":
        print("Thank you for playing! Goodbye!")
        break
