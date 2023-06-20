from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
menu_items = menu.get_items()

is_on = True

while is_on:
    order = input(f"What do you like to order? ({menu_items}): ")
    if order == "off":
        is_on = False
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink):
            drink_cost = drink.cost
            transaction = money_machine.make_payment(drink_cost)
            if transaction:
                coffee_maker.make_coffee(drink)
