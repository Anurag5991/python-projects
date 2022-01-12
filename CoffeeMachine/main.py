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

profit = 0


def is_sufficient(req_ingredients):
    for item in req_ingredients:
        count = 0
        if req_ingredients[item] <= resources[item]:
            count += 1
        else:
            return False
        return True


def process_coins():
    price = 0
    quarters = int(input("Enter the number of quarters: "))
    dimes = int(input("Enter the number of dimes: "))
    nickel = int(input("Enter the number of nickel: "))
    pennies = int(input("Enter the numbers of pennies: "))
    price = (quarters * 0.25) + (dimes * 0.10) + (nickel * 0.05) + (pennies * 0.01)
    return price


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print("Water : ", resources["water"])
        print("Milk : ", resources["milk"])
        print("Coffee : ", resources["coffee"])
        print("Money : ", profit)
    else:
        ingredients = MENU[choice]

        if is_sufficient(ingredients["ingredients"]):
            for key in ingredients["ingredients"]:
                resources[key] = resources[key] - ingredients["ingredients"][key]
            price_choice = process_coins()
            if ingredients["cost"] == price_choice:
                profit += price_choice
            elif ingredients["cost"] < price_choice:
                print("Please Have your change ", (price_choice - ingredients["cost"]))
                profit += ingredients["cost"]
            else:
                print("Sorry not Enough money")
            print(f"Here's your {choice}")
        else:
            print("Not enough ingredients")

