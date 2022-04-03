#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

WELCOME_TEXT = "Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100"
print(logo)
print(WELCOME_TEXT)

random_num = random.randint(1, 101)
easy_level = 10
hard_level = 5
user_difficulty = input("Choose a difficulty. Type 'easy' for 10 attempts. 'hard' for 5 attempts. ").lower()
user_choice = int(input("Make a guess: "))

if user_choice == random_num:
  print(f"You got it! The answer was {random_num}")