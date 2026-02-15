'''

You are tasked with creating a simple inventory management system for a market. The system should allow users to add, update, view, and remove items from the inventory. Each item in the inventory will have a name, price, quantity, and category.
Functionality:

Add Item: Create a function add_item that allows users to add a new item to the inventory. Users should input the name, price, quantity, and category of the item.
Update Item: Implement a function update_item that allows users to update the details of an existing item in the inventory. Users should be able to update the price, quantity, and category of the item.
View Inventory: Develop a function view_inventory that displays all items in the inventory along with their details (name, price, quantity, and category).
Remove Item: Create a function remove_item that allows users to remove an item from the inventory based on its name.
Search by Category: Implement a function search_by_category that allows users to search for items in the inventory based on their category. The function should display all items belonging to the specified category.

Project Structure:
Define a list inventory to store the items in the market inventory. Each item should be represented as a dictionary with keys for name, price, quantity, and category.
Implement the functions add_item, update_item, view_inventory, remove_item, and search_by_category to manage the inventory.
Create a main loop to interact with the user. The loop should prompt the user to choose from various options such as adding, updating, viewing, removing items, or searching by category.
'''

# Inventory storage
inventory = []


def add_item():
    name = input("Enter item name: ").strip()

    # Prevent duplicate item names
    for item in inventory:
        if item["name"].lower() == name.lower():
            print("Item already exists.")
            return

    try:
        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))
    except ValueError:
        print("Invalid price or quantity.")
        return

    category = input("Enter item category: ").strip()

    inventory.append({
        "name": name,
        "price": price,
        "quantity": quantity,
        "category": category
    })

    print("Item added successfully.")


def update_item():
    name = input("Enter item name to update: ").strip()

    for item in inventory:
        if item["name"].lower() == name.lower():
            try:
                price = float(input("Enter new price: "))
                quantity = int(input("Enter new quantity: "))
            except ValueError:
                print("Invalid price or quantity.")
                return

            category = input("Enter new category: ").strip()

            item["price"] = price
            item["quantity"] = quantity
            item["category"] = category

            print("Item updated successfully.")
            return

    print("Item not found.")


def view_inventory():
    if not inventory:
        print("Inventory is empty.")
        return

    print("\n--- Inventory ---")
    for item in inventory:
        print(f"Name: {item['name']}")
        print(f"Price: ${item['price']:.2f}")
        print(f"Quantity: {item['quantity']}")
        print(f"Category: {item['category']}")
        print("-----------------")


def remove_item():
    name = input("Enter item name to remove: ").strip()

    for item in inventory:
        if item["name"].lower() == name.lower():
            inventory.remove(item)
            print("Item removed successfully.")
            return

    print("Item not found.")


def search_by_category():
    category = input("Enter category to search: ").strip().lower()

    found = False
    for item in inventory:
        if item["category"].lower() == category:
            print(f"Name: {item['name']}")
            print(f"Price: ${item['price']:.2f}")
            print(f"Quantity: {item['quantity']}")
            print("-----------------")
            found = True

    if not found:
        print("No items found in this category.")


def main():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Update Item")
        print("3. View Inventory")
        print("4. Remove Item")
        print("5. Search by Category")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_item()
        elif choice == "2":
            update_item()
        elif choice == "3":
            view_inventory()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            search_by_category()
        elif choice == "6":
            print("Exiting system.")
            break
        else:
            print("Invalid option. Please choose between 1 and 6.")


if __name__ == "__main__":
    main()
