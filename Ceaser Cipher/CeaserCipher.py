def encrypt(mes, shift):
    encoded =""
    for i in range(len(mes)):
        asc = ord(mes[i])
        asc += shift
        encoded += chr(asc)
    print(f"Here's the encoded result: {encoded}")
    
def decrypt(mes, shift):
    decoded = ""
    for i in range(len(mes)):
        asc = ord(mes[i])
        asc -= shift
        decoded += chr(asc)
    print(f"Here's the decoded result: {decoded}")

repeat = "yes"
from art import logo
print(logo)
while repeat == "yes":
    choice = input("Type 'encode' to encrypt, type 'decode to decrypt:\n")
    message = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    shift = shift%26
    if choice == "encode":
        encrypt(message, shift)
    elif choice == "decode":
        decrypt(message, shift)
    else:
        print('you have enterd wrong input')
    repeat = input("Type 'yes' if you want to go again. Otherwise type'no'.\n")
    if repeat == "no":
        print("Exiting...")