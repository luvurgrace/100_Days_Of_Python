from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO 1: Print report
# TODO 2: Check resources sufficient?
# TODO 3: Process coins
# TODO 4: Check transaction successful?
# TODO 5: Make Coffee

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    user_choice = input(f"What would you like? {options}")
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
