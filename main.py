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


def check_money(drink, money_paid):  # nepouzivat money jako grlobalni promennou, normalne to predat v ramci ty funkce
    if money_paid > MENU[drink]["cost"]:
        change_money = round(money_paid - MENU[drink]["cost"], 2)
        print(f"You have inserted ${money_paid}. Here is ${change_money} in change.")
        return True
    else:
        print(
            f"You have inserted ${money_paid}. The {drink} is {MENU[drink]['cost']}. That's not enough money. Money refunded.")
        return False


def check_leftovers(drink):
    for ingredient in resources.keys():
        resources[ingredient] -= MENU[drink]["ingredients"][ingredient]
    print(f"Here is your {drink}. Enjoy")


def profit(drink):
    return MENU[drink]["cost"]


def main():
    profit_made = 0
    machine_on = True  # pouzil bych vystiznejsi nazev, aby bylo jasno, co ta condition dela.
    while machine_on:  # to  == True je tu zbytecny.
        ask_question = input("What would you like? espresso/latte/cappuccino (or type 'report' or 'off'): ")
        if ask_question == "off":  # tady by bylo vhodnejsi pouzit konstrukci case - match misto if-elif, ktera je v pythonu od verze 3.10
            machine_on = False
        elif ask_question == "report":
            print(
                f"Water: {resources['water']} ml \nMilk: {resources['milk']} ml \nCoffee: {resources['coffee']} g \nMoney: ${profit_made}")
        elif ask_question in MENU.keys():
            if check_resources(ask_question):
                print("Please insert coins: ")
                # type by mohlo bejt asi i int, protoze jsou to cele mince
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickles = int(input("How many nickles?: "))
                pennies = int(input("How many pennies?: "))
                money = round(quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01, 2)
                if check_money(ask_question, money):
                    check_leftovers(ask_question)
                    profit_made += profit(ask_question)


if __name__ == "__main__":
    main()
