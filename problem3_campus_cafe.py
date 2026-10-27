# Use integer cents so all prices and tax round consistently.
def main():
    print("=" * 30)
    print("    CAMPUS CAFE ORDER SYSTEM")
    print("=" * 30)
    print("  1. Coffee   - $3.50")
    print("  2. Sandwich - $6.00")
    print("  3. Salad    - $5.50")
    print("  4. Combo    - $8.00")
    print("  5. Exit")
    print("=" * 30)
    choice = input("Enter your choice (1-5): ").strip()
    if choice == "5":
        print("Goodbye!")
        return
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Please select 1-5.")
        return

    # Set the base price, then customize inside the selected branch.
    if choice in ["1", "4"]:
        if choice == "1":
            item, cents = "Coffee", 350
        else:
            item, cents = "Combo (Sandwich + Coffee)", 800
        size = input("Coffee size (small/medium/large): ").strip().lower()
        if size == "medium":
            cents += 100
        elif size == "large":
            cents += 200
        elif size != "small":
            print("Invalid size. Defaulting to Small.")
            size = "small"
        item += f" ({size.title()})"
    elif choice == "2":
        item, cents = "Sandwich", 600
    else:
        item, cents = "Salad", 550
        dressing = input("Dressing (ranch/italian/vinaigrette/none): ")
        dressing = dressing.strip().lower()
        if dressing not in ["ranch", "italian", "vinaigrette", "none"]:
            print("Invalid dressing. Defaulting to none.")
            dressing = "none"
        item += f" (dressing: {dressing})"

    # Both the sandwich and combo offer cheese.
    if choice in ["2", "4"]:
        cheese = input("Add cheese? (yes/no): ").strip().lower()
        while cheese not in ["yes", "no"]:
            print("Please enter yes or no.")
            cheese = input("Add cheese? (yes/no): ").strip().lower()
        if cheese == "yes":
            cents += 75
            item += " + Cheese"

    name = input("Enter your name: ").strip()
    while not name:
        print("Name cannot be empty.")
        name = input("Enter your name: ").strip()

    # Retry until quantity is an integer greater than zero.
    while True:
        try:
            quantity = int(input("How many? "))
            if quantity > 0:
                break
            print("Quantity must be positive.")
        except ValueError:
            print("Quantity must be a valid integer.")

    subtotal = cents * quantity
    # Round 7% tax to the nearest cent, rounding half a cent up.
    tax = (subtotal * 7 + 50) // 100
    total = subtotal + tax
    print("=" * 30)
    print("        ORDER RECEIPT")
    print("=" * 30)
    print(f"  Customer: {name}")
    print(f"  Item:     {item}")
    print(f"  Quantity: {quantity}")
    print(f"  Unit Price: ${cents / 100:.2f}")
    print(f"  Subtotal:   ${subtotal / 100:.2f}")
    print(f"  Tax (7%):   ${tax / 100:.2f}")
    print(f"  Total:      ${total / 100:.2f}")
    print("=" * 30)
    print("Thank you for your order!")


if __name__ == "__main__":
    main()
