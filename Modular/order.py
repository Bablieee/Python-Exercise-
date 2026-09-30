# ==========================================
#         BURGER YUM - ORDER MODULE
# ==========================================

from menu import menu


def take_order():
    orders = {}

    while True:
        item = input("\nEnter menu item: ").title()

        if item not in menu:
            print("Sorry, that item is not on the menu.")
            continue

        try:
            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue

        except ValueError:
            print("Please enter a valid number.")
            continue

        if item in orders:
            orders[item] += quantity
        else:
            orders[item] = quantity

        again = input(
            "Do you want to order another item? (yes/no): "
        ).lower()

        if again != "yes":
            break

    return orders


def calculate_item_total(item, quantity):
    return menu[item] * quantity


def calculate_total(orders):
    total = 0

    for item, quantity in orders.items():
        total += calculate_item_total(item, quantity)

    return total
