MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# TODO: 0. Create function [report] that reports resources of the machine


def report(resources):
    """Returns quantity of water, milk & coffee in the machine"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['Money']}")


def resource_check(drink):
    """Compares the quantity of resources needed in recipe vs in the machine
    Returns True if there's enough quantity and false otherwise"""
    ing_qt_water = MENU[drink]["ingredients"]["water"]
    ing_qt_coffee = MENU[drink]["ingredients"]["coffee"]

    if drink != "espresso":
        ing_qt_milk = MENU[drink]["ingredients"]["milk"]
    if ing_qt_water < resources['water'] and ing_qt_coffee < resources['coffee']:
        return True
    elif ing_qt_water < resources['water'] and ing_qt_coffee < resources['coffee'] and ing_qt_milk < resources['milk']:
        return True
    elif ing_qt_water > resources['water']:
        print("Sorry, there's not enough water")
        return False
    elif ing_qt_milk > resources['milk']:
        print("Sorry, there's not enough milk")
        return False
    elif ing_qt_coffee > resources['coffee']:
        print("Sorry, there's not enough coffee")
        return False


def money_sum():
    """Asks user for number of coins, adds them up and returns the total"""
    # TODO: 2.1 input how many quarters, dimes, nickles and pennies
    num_of_quarters = int(input("how many quarters?: "))
    num_of_dimes = int(input("how many dimes?: "))
    num_of_nickles = int(input("how many nickles?: "))
    num_of_pennies = int(input("how many pennies: "))

    # TODO: 3. Calculate the value of the coins.
    quarters = num_of_quarters * 0.25
    dimes = num_of_dimes * 0.10
    nickles = num_of_nickles * 0.05
    pennies = num_of_pennies * 0.01
    total = quarters + dimes + nickles + pennies
    return total


def resource_update(drink, resources, MENU, total,change):
    """Updates the resource quantity in the Machine, including money."""
    ing_qt_water = MENU[drink]["ingredients"]["water"]
    ing_qt_coffee = MENU[drink]["ingredients"]["coffee"]
    machine_water = resources["water"] - ing_qt_water
    resources["water"] = machine_water
    machine_coffee = resources["coffee"] - ing_qt_coffee
    resources["coffee"] = machine_coffee
    if drink != "espresso":
        ing_qt_milk = MENU[drink]["ingredients"]["milk"]
        machine_milk = resources['milk']-ing_qt_milk
        resources['milk'] = machine_milk
    resources["Money"] += MENU[drink]["cost"]


def change(total,drink):
    """Checks if the total money inserted is enough to cover the price of the coffee
    Returns the change and 'Here is your Drink' message"""
    price = MENU[drink]["cost"]
    if price > total:
        print("Sorry, that's not enough money. Money refunded.")
        proceed = False
        return proceed
    elif price <= total:
        change = round(total - price, 2)
        print(f"Here is your ${change} in change.")
        print(f"Here is your {drink}☕. Enjoy!")
        return change


# TODO: 1. Ask user what he would like (espresso,latte,cappuccino or report)
resources["Money"]=0
should_continue = True
while should_continue:
    drink = input("What would you like? (espresso, latte, cappuccino) ")
    if drink == "report":
        not_stop=True
        while not_stop:
            report(resources)
            drink = input("What would you like? (espresso, latte, cappuccino) ")
            if drink != "report":
                not_stop=False
    # TODO: 1.1 Check resources. If resources too low, inform user so
    if resource_check(drink):

        # TODO: 2. Inform user to insert coins.

        print("Please insert coins")

        # TODO: 3.1 Cancel transaction if too low, give back change if too high
        total = money_sum()
        if change(total, drink):
            resource_update(drink, resources, MENU, total, change)
