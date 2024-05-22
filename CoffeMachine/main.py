from data import resources, MENU, units


def prompt():
    decision = input("What would you like? (espresso/latte/cappuccino): ")
    return decision


def coffee(choice):
    for key in MENU[choice]["ingredients"]:
        for opt in resources:
            if key == opt:
                resources[opt] -= MENU[choice]["ingredients"][key]


def report(resources):
    for key in resources:
        print(f"{key} : {resources[key]} {units[key]}")


def check(choice):
    for key in MENU[choice]["ingredients"]:
        for opt in resources:
            if key == opt:
                if MENU[choice]["ingredients"][key] < resources[opt]:
                    continue
                else:
                    print(f"Sorry there is not enough {opt}.")
                    return False
    return True


def process(q, d, n, p, choice):
    total = (q * 0.25) + (d * 0.1) + (n * 0.05) + (n * 0.01)
    if total >= MENU[choice]["cost"]:
        return total - MENU[choice]["cost"]
    else:
        return None


def coin_prompt():
    print("Please insert coins.")
    q = int(input("How many quarters?: "))
    d = int(input("How many dimes?: "))
    n = int(input("How many nickles?: "))
    p = int(input("How many pennies?: "))
    return q, d, n, p


switch = "on"
while switch != "off":
    option = prompt()
    if option == "report":
        report(resources)
    elif option == "off":
        switch = "off"
        break
    else:
        if option not in MENU:
            print("Entered Invalid Input Try Again")
            continue
        if check(option):
            q, d, n, p = coin_prompt()
            if process(q, d, n, p, option) is not None:
                if process(q, d, n, p, option) != 0:
                    print(f"Here is your change: ${process(q, d, n, p, option)}")
                coffee(option)
                print(f"Enjoy your {option}")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Try after sometime...")
if switch == "off":
    print("Signing Off!")
