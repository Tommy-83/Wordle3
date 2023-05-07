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

for guess in range(1, 7):
    guess = input().lower()

    for i in range( min(len(guess), 5) ):
        if guess[i] == word[i]:
            print(colored(guess[i], 'green'), end="")
        elif guess[i] in word:
            print(colored(guess[i], 'yellow'), end="")
        else:
            print(guess[1], end="")