import random
import sys
from termcolor import colored

def start_menu():
    print("Welcome To Wordle by Tommy")
    print("try and guess the 5 letter word")

def pick_a_word():
    with open("words.txt") as f:
        words = f.read().splitlines()
        return random.choice(words)

start_menu()
word = pick_a_word()

for attempt in range(1, 7):
    guess = input().lower()

    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[1K')

    for i in range( min(len(guess), 5) ):
        if guess[i] == word[i]:
            print(colored(guess[i], 'green'), end="")
        elif guess[i] in word:
            print(colored(guess[i], 'yellow'), end="")
        else:
            print(guess[i], end="")

    if guess == word:
            print(colored(f"Well done! You guessed the Wordle in {attempt}", 'green'))
            break