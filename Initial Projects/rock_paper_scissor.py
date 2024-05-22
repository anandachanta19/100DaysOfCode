import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

moves = [rock, paper, scissors]
choice = int(input('''What would you choose?\nType:\n0 for Rock.\n1 for Paper.\n2 for Scissors.\n'''))
print(moves[choice])
computer_choice = random.randint(0, 2)
print("Computer choose:")
print(moves[computer_choice])

if choice == computer_choice:
    print ("Draw")
elif choice > computer_choice:
    print("You win!")
elif choice < computer_choice:
    print("You lose!")
else:
    print("You have chosen an invalid number")
