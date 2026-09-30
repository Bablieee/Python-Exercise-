# ==========================================
#          BURGER YUM - OOP MODULE
# ==========================================


class Menu:
    def __init__(self):
        self.menu = {
            "Burger": 80,
            "Cheese Burger": 100,
            "Chicken Burger": 90,
            "Fries": 50,
            "Soft Drink": 30
        }

    def show_menu(self):
        print("\n" + "-" * 45)
        print("                    MENU")
        print("-" * 45)

        for item, price in self.menu.items():
            print(f"{item:<25} PHP {price:.2f}")

        print("-" * 45)

    def item_exists(self, item):
        return item in self.menu

    def get_price(self, item):
        return self.menu[item]


class Order:
    def __init__(self, menu):
        self.menu = menu
        self.orders = {}

    def add_item(self, item, quantity):
        if item in self.orders:
            self.orders[item] += quantity
        else:
            self.orders[item] = quantity

    def take_order(self):
        while True:
            item = input("\nEnter menu item: ").title()

            if not self.menu.item_exists(item):
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

            self.add_item(item, quantity)

            again = input(
                "Do you want to order another item? (yes/no): "
            ).lower()

            if again != "yes":
                break

    def calculate_item_total(self, item, quantity):
        return self.menu.get_price(item) * quantity

    def calculate_total(self):
        total = 0

        for item, quantity in self.orders.items():
            total += self.calculate_item_total(item, quantity)

        return total

    def has_orders(self):
        return len(self.orders) > 0


class Receipt:
    def __init__(self, order):
        self.order = order

    def print_receipt(self):
        print("\n" + "=" * 55)
        print("                  BURGER YUM")
        print("                     RECEIPT")
        print("=" * 55)

        print(
            f"{'Item':<20}"
            f"{'Quantity':>5}"
            f"{'Price':>12}"
            f"{'Total':>12}"
        )

        print("-" * 55)

        for item, quantity in self.order.orders.items():
            price = self.order.menu.get_price(item)
            item_total = self.order.calculate_item_total(
                item, quantity
            )

            print(
                f"{item:<20}"
                f"{quantity:>5}"
                f"{price:>12.2f}"
                f"{item_total:>12.2f}"
            )

        total = self.order.calculate_total()

        print("-" * 55)
        print(f"{'TOTAL:':>43} PHP {total:>7.2f}")
        print("=" * 55)
        print("        Thank you for ordering at BURGER YUM!")
        print("=" * 55)
