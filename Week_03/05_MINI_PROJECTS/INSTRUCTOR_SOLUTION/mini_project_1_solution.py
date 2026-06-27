"""
Mini-Project 1: Word Guessing Game — INSTRUCTOR SOLUTION
Week 3

This is ONE valid, complete implementation of the specification in
README.md. It is not the only correct design -- students may structure
play_game's internal loop differently, use different variable names,
or add extra helper functions, as long as each required function meets
its stated specification and the game works correctly end to end.

Do not show this file to students before they have attempted their own
implementation.
"""

import random


WORD_LIST = [
    "python", "function", "variable", "computer", "keyboard",
    "program", "string", "integer", "boolean", "syntax",
    "debug", "loop", "array", "object", "method"
]


def choose_secret_word(word_list):
    """
    Assumes: word_list is a non-empty sequence of strings
    Returns: one word from word_list, chosen at random
    """
    return random.choice(word_list)


def get_blank_display(secret_word, guessed_letters):
    """
    Assumes: secret_word is a string, guessed_letters is a string
             containing every letter the player has guessed so far
    Returns: a string showing secret_word with each not-yet-guessed
             letter replaced by an underscore, letters separated by
             spaces (e.g., "apple" with guessed_letters="ae" returns
             "a _ _ _ e")
    """
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def is_word_guessed(secret_word, guessed_letters):
    """
    Assumes: secret_word is a string, guessed_letters is a string
             containing every letter the player has guessed so far
    Returns: True if every letter in secret_word appears in
             guessed_letters, False otherwise
    """
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True


def is_valid_guess(guess, guessed_letters):
    """
    Assumes: guess is a string, guessed_letters is a string of
             previously guessed letters
    Returns: True if guess is a single lowercase letter that has NOT
             already been guessed, False otherwise
    """
    if len(guess) != 1:
        return False
    if guess not in "abcdefghijklmnopqrstuvwxyz":
        return False
    if guess in guessed_letters:
        return False
    return True


def get_player_guess(guessed_letters):
    """
    Assumes: guessed_letters is a string of previously guessed letters
    Returns: a single validated lowercase letter from the player (keeps
             asking until a valid, not-yet-guessed letter is entered)
    """
    guess = input("Guess a letter: ").lower()
    while not is_valid_guess(guess, guessed_letters):
        if len(guess) != 1 or guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a single letter (a-z).")
        else:
            print(f"You already guessed '{guess}'. Try a different letter.")
        guess = input("Guess a letter: ").lower()
    return guess


def play_game(word_list, max_wrong_guesses=6):
    """
    Assumes: word_list is a non-empty sequence of strings,
             max_wrong_guesses is a positive integer
    Runs one complete game from start to finish, printing the game's
    progress, and reports the final result (win or lose) along with
    the secret word.
    """
    secret_word = choose_secret_word(word_list)
    guessed_letters = ""
    wrong_guesses = 0

    while wrong_guesses < max_wrong_guesses:
        print()
        print(get_blank_display(secret_word, guessed_letters))
        print(f"Wrong guesses remaining: {max_wrong_guesses - wrong_guesses}")

        guess = get_player_guess(guessed_letters)
        guessed_letters += guess

        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")

        if is_word_guessed(secret_word, guessed_letters):
            print()
            print(f"You won! The word was '{secret_word}'.")
            return

    print()
    print(f"You ran out of guesses. The word was '{secret_word}'.")


if __name__ == "__main__":
    print("Welcome to the Word Guessing Game!")
    print("=" * 40)
    play_game(WORD_LIST)
