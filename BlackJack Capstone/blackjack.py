import os
import random
from art import logo

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def result(user_cards, computer_cards, decision, cards):
    if decision != "hit" and decision != "stand":
        print("You have Entered an invalid input")
    if decision == "hit":
        user_cards.append(random.choice(cards))
        print(f"Your final hand: {user_cards} and your final score: {sum(user_cards)}")
        print(f"Computer's final hand: {computer_cards} and Computer's final score: {sum(computer_cards)}")
        if sum(user_cards) > 21 or sum(user_cards) < sum(computer_cards):
            print ("You loose, Computer wins.")
        elif sum(user_cards) == sum(computer_cards):
            print("Its a draw!")
        elif sum(user_cards)> sum(computer_cards):
            print("You win, Computer loose!")
    elif decision == "stand":
        print(f"Your final hand: {user_cards} and your final score: {sum(user_cards)}")
        print(f"Computer's final hand: {computer_cards} and Computer's final score: {sum(computer_cards)}")
        if sum(user_cards) > 21 or sum(user_cards) < sum(computer_cards):
            print ("You loose, Computer wins.")
        elif sum(user_cards) == sum(computer_cards):
            print("Its a draw!")
        elif sum(user_cards)> sum(computer_cards):
            print("You win, Computer loose!")

        
    
    
def blackJack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards =[random.choice(cards), random.choice(cards)]
    computer_cards =[random.choice(cards), random.choice(cards)]
    print(f"Your cards: {user_cards} and Your Score: {sum(user_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")
    decision = input("Type 'hit' to get another card, type 'stand' to pass: ")
    if sum(computer_cards) < 17:
        computer_cards.append(random.choice(cards))
    result(user_cards, computer_cards, decision, cards)
    
        
    
while(True):    
    choice = input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ")
    if choice == "yes":
        clear()
        print(logo)
        blackJack()
    elif choice != "no":
        print("You have Entered an invalid input")
    else:
        print("Exiting...")
        break