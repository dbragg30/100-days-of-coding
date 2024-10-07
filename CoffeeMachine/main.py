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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# TODO: 1. print report of all coffee machine resources
# TODO: 2. check for sufficient resources:


def checkResources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"there is not enough {order_ingredients}")
            return False
    return True


# TODO: 3. Prompt user by asking “What would you like?

# TODO 4. process coin


def process_coins():
    total = int(input("how many quarters?: ")) * .025
    total += int(input("how many dimes?: ")) * .1
    total += int(input("how many nickel?: ")) * .05
    total += int(input("how many pennies?: ")) * .01
    return total


# TODO: 5. check transaction is successful

def is_transaction_successful(money_rvd, drink_cost):
    if money_rvd >= drink_cost:
        change = round(money_rvd - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that is not enough money. Money refunded")
        return False
# TODO: #make coffee


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}  . Enjoy!")
#  TODO: deduct money from user.
# TODO: Turn coffee port off


is_on = True
while is_on:
    choice = input("What would you like?(espresso/latte/cappuccino:")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Water: {resources['milk']}ml")
        print(f"Water: {resources['coffee']}ml")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if checkResources(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink["ingredients"])
