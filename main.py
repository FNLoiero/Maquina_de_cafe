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
is_on = True


def verify_resources(drink_v):
    for item in drink_v:
        if drink_v[item] >= resources[item]:
            print(f"sorry, not enough {item} ")
            return False
    return True


def colect_money():
    quarter = int(input("how many quarters: "))
    dimes = int(input("how many dimes: "))
    nickles = int(input("how many nickles: "))
    pennies = int(input("how many pennies: "))
    return quarter*0.25+dimes*0.1+nickles*0.05+pennies*0.01



while(is_on):
    choice = input("what would you like? (espresso/latte/cappuccino): ")

    if choice == "report":
        print(f"water {resources["water"]}")
        print(f"milk {resources["milk"]}")
        print(f"coffee {resources["coffee"]}")
        print(f"profit {profit}")
    elif choice == "off":
        is_on = False
    else:
        drink = MENU[choice]
        if verify_resources(drink["ingredients"]):
            total = colect_money()
            if total >= drink["cost"]:
                profit += drink["cost"]
                for item in drink["ingredients"]:
                    resources[item] -= drink["ingredients"][item]
                print(f"here is your change {total-drink["cost"]}")
                print(f"Enjoy your {choice}")
            else:
                print("sorry, not enough money. Money refunded")

