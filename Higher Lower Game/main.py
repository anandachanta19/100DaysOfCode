from art import logo, vs
from gameData import data
import os
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')



play = "yes"
while play == "yes":
    print("123")
    lose = False
    A = random.choice(data)
    B = random.choice(data)
    score = 0
    while lose == False:
        clear()
        print(logo)
        if score !=0:
            print(f"You're right! Current Sore: {score}")
        print(f"Compare A: {A["name"]}, a {A["description"]}, from {A["country"]}")
        print(vs)
        print(f"Against B: {B["name"]}, a {B["description"]}, from {B["country"]}")
        decision = input("Who has more folllowers? Type 'A' or 'B': ")
        if decision == "A" and A["follower_count"] >= B["follower_count"]:
            score += 1
            B = random.choice(data)
            while A == B:
                B = random.choice(data)
        elif decision == "B" and A["follower_count"] <= B["follower_count"]:
            score += 1
            A = random.choice(data) 
            while A == B:
                A = random.choice(data) 
        else:
            clear()
            print(f"Sorry, that's wrong. Final score: {score}")
            play = input(f"You can go above {score}. Wanna try again? Type 'yes' or 'no': ")
            lose = True
print("Exiting...")