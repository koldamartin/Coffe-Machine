MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
profit_made = 0

def check_resources(drink):
    if resources["water"] < MENU[drink]["ingredients"]["water"]:
        print("Sorry, there is not enough water.")
        return False
    if resources["milk"] < MENU[drink]["ingredients"]["milk"]:
        print("Sorry, there is not enough milk.")
        return False
    if resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
        print("Sorry, there is not enough coffee.")
        return False
    else:
        return True


def check_money(drink):
    if money > MENU[drink]["cost"]:
        change_money = round(money - MENU[drink]["cost"], 2)
        print(f"You have inserted ${money}. Here is ${change_money} in change.")
        return True
    else:
        print(
            f"You have inserted ${money}. The {drink} is {MENU[drink]['cost']}. That's not enough money. Money refunded.")
        return False


def check_leftovers(drink):
    for ingredient in resources.keys():
        resources[ingredient] -= MENU[drink]["ingredients"][ingredient]
    print(f"Here is your {drink}. Enjoy")


def profit(drink):
    return MENU[drink]["cost"]


condition = True
while condition == True:
    ask_question = input("What would you like? espresso/latte/cappuccino (or type 'report' or 'off'): ")
    if ask_question == "off":
        condition = False
    elif ask_question == "report":
        print(f"Water: {resources['water']} ml \nMilk: {resources['milk']} ml \nCoffee: {resources['coffee']} g \nMoney: ${profit_made}")
    elif ask_question == "latte" or ask_question == "espresso" or ask_question == "cappuccino":
        if check_resources(drink=ask_question) == True:
            print("Please insert coins: ")
            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickles = float(input("How many nickles?: "))
            pennies = float(input("How many pennies?: "))
            money = round(quarters * float(0.25) + dimes * float(0.1) + nickles * float(0.05) + pennies * float(0.01), 2)
            if check_money(drink=ask_question) == True:
                check_leftovers(drink=ask_question)
                profit_made += profit(drink=ask_question)
