import random
import sys

def start_menu():
    print("Welcome To Wordle by Tommy")
    print("try and guess the 5 letter word")

def pick_a_word():
    with open("words.txt") as f:
        words = f.read().splitlines()
        return random.choice(words)

start_menu()
word = pick_a_word()

