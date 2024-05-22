import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
from art import logo
print(logo)

print("Welcome to the secret auction program.")
bids ={}
repeat = "yes"
while repeat == "yes":
    name = input("What is your name?\n")
    bid = int(input("What's your bid?\n"))
    bids[name] = bid
    repeat = input("Are there any other bidders? Type 'yes' or 'no'\n")
    clear()

max = 0
winner = ""
for person in bids:
    if bids[person] > max:
        max = bids[person]
        winner = person
    
print(f"The winner is {winner} with a bid of ${max}")