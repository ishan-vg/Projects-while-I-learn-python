menu = {
    "veg": [
        {"name": "Veg Burger", "price": 150},
        {"name": "Veg Pizza", "price": 200},
        {"name": "Dosa", "price": 80},
    ],
    "non-veg": [
        {"name": "Chicken Burger", "price": 200},
        {"name": "Chicken Pizza", "price": 250},
        {"name": "Chicken Fry", "price": 175},
    ],
}


def order(preference, order_list):
    print("Menu: ")
    for index, dish in enumerate(menu[preference]):
        print(f"{index + 1}. {dish['name']} - {dish['price']}")
    try:
        choice = int(input("Enter your choice: "))
    except:
        print("Invalid input")
        exit()
    if choice > 3 or choice < 1:
        print("Invalid input")
        exit()
    order_list.append(menu[preference][choice - 1])
    print("Your order: ")
    for index, dish in enumerate(order_list):
        print(f"{index + 1}. {dish['name']} - {dish['price']}")
    want_more = input("Do you want to order more? (y/n): ")
    if want_more == "y":
        order(preference, order_list)
    else:
        total = 0
        for dish in order_list:
            total += dish["price"]
        print(f"Thank you for ordering. Your total bill is: Rs. {total}")


order_list = []

try:
    choice = int(input("1. Veg\n2. Non-Veg\n3. Exit\nEnter your preference: "))
    if choice == 3:
        print("Exiting")
        exit()
    choices = {1: "veg", 2: "non-veg"}
    preference = choices[choice]
    order(preference, order_list)
except:
    print("Invalid input")
    exit()
