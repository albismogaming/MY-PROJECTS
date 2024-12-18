import numpy as np
from STAGES import *
from WORD_LIST import *
from TITLE import title
from COLORS import *
from FUNCTIONS import *


# USE NUMPY RANDOM CHOICE FUNCTION TO CHOOSE A RANDOM WORD
selected_word = np.random.choice(words).upper()

# CONSTANT FOR THE AMOUNT OF GUESSES A USER GETS
player_lives = 6
game_over = False
correct_letters = []

print(rgb_colored(title, GOLD))
print(rgb_colored(f"YOUR SELECTED WORD IS [{len(selected_word)}] LETTERS LONG!\n", PEACH))
print(rgb_colored("GOOD LUCK!\n", PEACH))
print(rgb_colored("#"*44, GOLD))

while not game_over:
    # ASK THE USER TO GUESS A LETTER - USE INPUT()
    print(f"\nREMAINING LIVES: {player_lives}")
    guess = input("GUESS A LETTER ==> ").upper()
    print(rgb_colored("-"*44, PEACH))
    display = ""

    if guess in correct_letters:
        print(f"GUESS AGAIN. {guess} HAS ALREADY BEEN USED.\n")

    for x in selected_word:
        if x == guess:
            print("YOU HAVE A GUESSED A LETTER IN THE WORD!\nNICE JOB! 🤩\n")
            display += x
            correct_letters.append(guess)
        elif x in correct_letters:
            display += x
        else:
            display += "_"

    if guess not in selected_word:
        print(f"YOU HAVE GUESSED A LETTER NOT IN THE WORD.\nLOSE A LIFE! 🥲\n")
        player_lives -= 1

    print(rgb_colored(STAGES[player_lives], PEACH))
    print(f"WORD: {display}")
    print()
    print(rgb_colored("#"*44, GOLD))

    if player_lives == 0:
        game_over = True
        print(f"\nYOU WERE UNSUCCESSFUL IN GUESSING THE WORD {selected_word}!")
        print("YOU LOSE! :)")

    if "_" not in display:
        game_over = True
        print("\nYOU HAVE SUCCESSFULLY GUESSED THE WORD!")
        print("YOU WIN! :)\n")
