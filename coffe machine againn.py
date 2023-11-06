resource = {
    "milk": 100,
    "coffe": 76,
    "water": 200,
}

cost = {
    "espresso": 150,
    "cappucino": 180,
    "latte": 200,
}
menu = {
        "cappucino": {
        "milk": 20,
        "coffe": 16,
        "water": 100,

        },
        "latte": {
        "milk": 30,
        "coffe": 46,
        "water": 100,
        },
        "espresso"  : {
        "milk": 100,
        "coffe": 66,
        "water": 100,
        },
    }
profit = 0


def enough(choice):
    print(f"nos {len(choice)}")
    for item in choice:
        if choice[item] <= resource[item]:
            print(f"enough {choice[item]} - {resource[item]}")
            return True
        else:
            print(f"not enough {choice[item]}")
            return False


def bills(money):
    if money < cost[drink]:
        print(f"not enough money.")
        return False
    elif money > cost[drink]:
        balance = money - cost[drink]
        print(f"here is ur {balance}")
        return True
    else:
        return True


def sub(choice):
    for item in choice:
        resource[item] -= choice[item]

run = True
while run:
    drink = input("what would u like? 'espresso', 'latte', 'cappucino'")
    if drink == "off":
        print("Machine under maintainance")
        run = False
    elif drink == "report":
        for key, value in resource.items():
            print(f"{key} : {value}")
    else:
        choice = menu[drink]

        if enough(choice):
            print(f"that would be {cost[drink]}")
            money = int(input(f"please make payment"))
            if bills(money):
                profit += cost[drink]
                sub(choice)
                print(f"here is your {drink}")
                print(f"come again")






