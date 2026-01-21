from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffee = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
is_on = True

while is_on:
    option = input("What would you like? (espresso / latte / cappuccino): ")
    if option == "report":
        coffee.report()
        money_machine.report()
    elif option == "off":
        is_on = False
        break
    else:
        drink = menu.find_drink(option)
        if drink is not None:
            if coffee.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee.make_coffee(drink)