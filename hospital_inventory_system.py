# Hospital Inventory Management System
inventory = {
    "Paracetamol": 100,
    "Aspirin": 50,
    "Insulin": 30,
    "Bandage": 200
}


def view_inventory():
    print("\n===== INVENTORY LIST =====")

    if not inventory:
        print("Inventory is empty.")
        return

    print(f"{'Medicine':<20}{'Quantity'}")
    print("-" * 30)

    for medicine, quantity in inventory.items():
        print(f"{medicine:<20}{quantity}")


def search_medicine():
    medicine = input("Enter medicine name: ").title()

    if medicine in inventory:
        print(f"{medicine} is available.")
        print(f"Quantity: {inventory[medicine]}")
    else:
        print("Medicine not found.")


def add_medicine():
    medicine = input("Enter new medicine name: ").title()

    if medicine in inventory:
        print("Medicine already exists.")
        return

    quantity = int(input("Enter quantity: "))
    inventory[medicine] = quantity

    print("Medicine added successfully.")


def update_stock():
    medicine = input("Enter medicine name: ").title()

    if medicine not in inventory:
        print("Medicine not found.")
        return

    print("\n1. Add Stock")
    print("2. Reduce Stock")

    option = input("Choose option: ")

    if option == "1":
        amount = int(input("Enter quantity to add: "))
        inventory[medicine] += amount
        print("Stock added successfully.")

    elif option == "2":
        amount = int(input("Enter quantity to remove: "))

        if amount > inventory[medicine]:
            print("Not enough stock available.")
        else:
            inventory[medicine] -= amount
            print("Stock reduced successfully.")

    else:
        print("Invalid option.")


def remove_medicine():
    medicine = input("Enter medicine name to remove: ").title()

    if medicine in inventory:
        del inventory[medicine]
        print("Medicine removed successfully.")
    else:
        print("Medicine not found.")

while True:
    print("\n===== HOSPITAL INVENTORY MANAGEMENT =====")
    print("1. View Inventory")
    print("2. Search Medicine")
    print("3. Add New Medicine")
    print("4. Update Stock")
    print("5. Remove Medicine")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_inventory()

    elif choice == "2":
        search_medicine()

    elif choice == "3":
        add_medicine()

    elif choice == "4":
        update_stock()

    elif choice == "5":
        remove_medicine()

    elif choice == "6":
        print("Thank you for using Hospital Inventory Management System.")
        break

    else:
        print("Invalid choice. Please try again.")
