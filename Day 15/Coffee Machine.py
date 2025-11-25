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

def report():
    print(f"Water: {resources["water"]}. ")
    print(f"Milk: {resources["milk"]}. ")
    print(f"Coffee: {resources["coffee"]}. ")
    print(f"Money: ${round(taken_coins,2)}. ")

def check_resources(drink, resource):
    not_enough = []
    for ingredient in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][ingredient] >= resource[ingredient]:
            not_enough.append(ingredient)
    if not not_enough:
        return True
    else:
        print(f"Sorry there's not enough {', '.join(not_enough)}. ")
        return False

def insert_coins():
    inserted_coins = 0
    print("Kindly insert coins. ")
    inserted_coins += int(input("How many quarters?: "))*0.25
    inserted_coins += int(input("How many dimes?: "))*0.1
    inserted_coins += int(input("How many nickles?: "))*0.05
    inserted_coins += int(input("How many pennies?: "))*0.01
    return inserted_coins

def make_a_coffee(coffee, coffee_type):
    global taken_coins
    if check_resources(user_choice, resources):
        insert = insert_coins()
        cost = coffee["cost"]
        if insert >= cost:
            for ingredient in coffee["ingredients"]:
                resources[ingredient] -= coffee["ingredients"][ingredient]
            taken_coins -= coffee["cost"]
            change = round(insert - coffee["cost"],2)
            if change == 0:
                print(f"Here is you {coffee_type}. Enjoy!\nNo change. Thank you! ")
            else:
                print(f"Here is ${change} in change.")
                print(f"Here is you {coffee_type}. Enjoy!")
        else:
            print("Sorry there's not enough money. Money refunded.")

def cappuccino():
    coffee = MENU["cappuccino"]
    make_a_coffee(coffee, "cappuccino")

def latte():
    coffee = MENU["latte"]
    make_a_coffee(coffee, "latte")

def espresso():
    coffee = MENU["espresso"]
    make_a_coffee(coffee, "espresso")

machine_on = True
while machine_on:
    taken_coins = 0
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        machine_on = False
    elif user_choice == 'latte':
        latte()
    elif user_choice == "espresso":
        espresso()
    elif user_choice == "cappuccino":
        cappuccino()
    elif user_choice == "report":
        report()
    else:
        print("Invalid command is entered. ")



