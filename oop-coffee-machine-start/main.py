from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
coffeeMachine = CoffeeMaker()
moneyMachine = MoneyMachine()
menu = Menu()
while is_on:
    choice = input(f"What would you like to have? ({menu.get_items()}): ")
    if choice == "report":
        coffeeMachine.report()
    elif choice == "off":
        is_on = False
    else:
        order = menu.find_drink(choice)
        cost = 0
        if order is not None:
            if coffeeMachine.is_resource_sufficient(order):
                for item in menu.menu:
                    if item.name == order.name:
                        cost = item.cost
                if moneyMachine.make_payment(cost):
                    coffeeMachine.make_coffee(order)