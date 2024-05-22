import random
from art import logo

def number_guess(number, runs):
    while runs != 0:
        print(f"You have {runs} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Too high.")
            runs -= 1
        elif guess < number:
            print("Too low.")
            runs -= 1
        else:
            print(f"You got it! The answer was {guess}")
    print("You are out of attempts! So you loose.")

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
number = random.randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ")
if difficulty == "hard":
    runs = 5
    number_guess(number, runs)
elif difficulty == "easy":
    runs = 10
    number_guess(number, runs)