# Calculate the ticket price using age and matinee status.
def main():
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Error: age must be an integer.")
        return
    if age < 0:
        print("Error: age must be non-negative.")
        return

    answer = input("Is this a matinee showing? (yes/no): ")
    answer = answer.strip().lower()
    if answer not in ["yes", "no"]:
        print("Error: enter yes or no.")
        return
    matinee = True if answer == "yes" else False

    # The outer conditions select age; inner conditions select price.
    if age < 13:
        group = "Child"
        if matinee:
            price = 6.00
        else:
            price = 8.00
    elif age < 18:
        group = "Teen"
        if matinee:
            price = 7.00
        else:
            price = 10.00
    elif age < 65:
        group = "Adult"
        if matinee:
            price = 8.00
        else:
            price = 13.00
    else:
        group = "Senior"
        if matinee:
            price = 6.00
        else:
            price = 7.00

    print(f"Age group: {group}")
    print(f"Ticket price: ${price:.2f}")


if __name__ == "__main__":
    main()
