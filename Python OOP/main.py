# ==========================================
#          BURGER YUM ORDERING SYSTEM
#               OOP VERSION
# ==========================================

from burger_yum import Menu, Order, Receipt


def show_title():
    print("\n" + "=" * 45)
    print("              BURGER YUM")
    print("         FAST FOOD ORDERING SYSTEM")
    print("=" * 45)


def main():
    show_title()

    menu = Menu()
    menu.show_menu()

    choice = input(
        "\nWould you like to order? (yes/no): "
    ).lower()

    if choice == "yes":
        order = Order(menu)
        order.take_order()

        if order.has_orders():
            receipt = Receipt(order)
            receipt.print_receipt()
        else:
            print("No items were ordered.")
    else:
        print("\nThank you! Have a nice day.")


if __name__ == "__main__":
    main()
