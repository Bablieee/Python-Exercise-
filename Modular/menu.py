# ==========================================
#          BURGER YUM - MENU MODULE
# ==========================================

menu = {
    "Burger": 80,
    "Cheese Burger": 100,
    "Chicken Burger": 90,
    "Fries": 50,
    "Soft Drink": 30
}


def show_menu():
    print("\n" + "-" * 45)
    print("                    MENU")
    print("-" * 45)

    for item, price in menu.items():
        print(f"{item:<25} PHP {price:.2f}")

    print("-" * 45)
