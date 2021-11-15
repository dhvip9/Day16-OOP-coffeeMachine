from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_list = Menu()

coffee_process = CoffeeMaker()

payment_check = MoneyMachine()

is_on = True
while is_on:
    user_coffee = input(f"What Would you Like ?\n{menu_list.get_items()}\n>> ").lower()
    if user_coffee == "off":
        is_on = False
    elif user_coffee == "report/d":
        coffee_process.report()
        payment_check.report()
    else:
        drink = menu_list.find_drink(user_coffee)
        coffee_resource = coffee_process.is_resource_sufficient(drink)
        if coffee_resource:
            payable = payment_check.make_payment(drink.cost)
            coffee_process.make_coffee(drink)
