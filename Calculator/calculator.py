import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def add(f, s):
    print(f"{f} + {s} = {f+s}")
    return f+s

def sub(f, s):
    print(f"{f} - {s} = {f-s}")
    return f-s

def mul(f, s):
    print(f"{f} * {s} = {f*s}")
    return f*s

def div(f, s):
    print(f"{f} / {s} = {f/s}")
    return f/s

operator_dict = {"+": add, "-": sub, "*": mul, "/": div}
repeat = "n"
while repeat == "n":
    clear()
    from art import logo
    print(logo)
    first = float(input("What's the first number?: "))
    Operator = input("+\n-\n*\n/\nPick an Operation: ")
    second = float(input("what's the second number?: "))
    function = operator_dict[Operator]
    result = function(first, second)
    repeat = input(f"Type 'y' to continue calculating with {result}, or Type 'exit' to exit or  Type 'n' to start new calculation: ")
    while repeat == "y":
        first = result
        Operator = input("+\n-\n*\n/\nPick an Operation: ")
        second = float(input("what's the second number?: "))
        function = operator_dict[Operator]
        result = function(first, second)
        repeat = input(f"Type 'y' to continue calculating with {result}, or Type 'n' to start new calculation: ")
        
print("Exiting...")