# Tip Clculator

print("Welcome to the Tip Calculator!")
total_Bill = input("What was the total bill?\n$")
tip_percent = input("How much percent of whole bill would you like to give as a tip?\n")
num_people = input("How many people to split the bill?\n")

tb = float(total_Bill)
tp = float(tip_percent)
np = int(num_people)
individual_bill = round((tb + (tb * (tp / 100))) / np, 2)
print(f"Each person should pay: ${individual_bill}")