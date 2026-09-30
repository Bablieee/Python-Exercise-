# ==========================================
#        BURGER YUM - RECEIPT MODULE
# ==========================================

from menu import menu
from order import calculate_item_total, calculate_total


def print_receipt(orders):
    print("\n" + "=" * 55)
    print("                  BURGER YUM")
    print("                     RECEIPT")
    print("=" * 55)

    print(f"{'Item':<20}{'Qty':>5}{'Price':>12}{'Total':>12}")
    print("-" * 55)

    for item, quantity in orders.items():
        price = menu[item]
        item_total = calculate_item_total(item, quantity)

        print(
            f"{item:<20}"
            f"{quantity:>5}"
            f"{price:>12.2f}"
            f"{item_total:>12.2f}"
        )

    total = calculate_total(orders)

    print("-" * 55)
    print(f"{'TOTAL:':>43} PHP {total:>7.2f}")
    print("=" * 55)
    print("        Thank you for ordering at BURGER YUM!")
    print("=" * 55)
