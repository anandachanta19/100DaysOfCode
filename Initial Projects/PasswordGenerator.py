import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
l = int(input("How many letters would you like in your password?\n"))
s = int(input("How many symbols would you like in your password?\n"))
n = int(input("How many numbers would you like in your password?\n"))
password_length = l + s + n
l_count = 0
s_count = 0
n_count = 0

password = ""
length = 0
for count in range(10000):
    if length == password_length:
        break
    choice = random.randint(0, 2)
    if choice == 0 and l_count < l:
        password += letters[random.randint(0, len(letters) - 1)]
        l_count += 1
        length += 1
    elif choice == 1 and s_count < s:
        password += symbols[random.randint(0, len(symbols) - 1)]
        s_count += 1
        length += 1
    elif choice == 2 and n_count < n:
        password += numbers[random.randint(0, len(numbers) - 1)]
        n_count += 1
        length += 1


print("here is your password: " + password)