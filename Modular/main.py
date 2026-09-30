# ==========================================
#          BURGER YUM ORDERING SYSTEM
#              MODULAR VERSION
# ==========================================

from menu import show_menu
from order import take_order
from receipt import print_receipt


def show_title():
    print("\n" + "=" * 45)
    print("              BURGER YUM")
    print("         FAST FOOD ORDERING SYSTEM")
    print("=" * 45)


def main():
    show_title()
    show_menu()

    order = input(
        "\nWould you like to order? (yes/no): "
    ).lower()

    if order == "yes":
        orders = take_order()

        if orders:
            print_receipt(orders)
        else:
            print("No items were ordered.")
    else:
        print("\nThank you! Have a nice day.")


if __name__ == "__main__":
    main()
