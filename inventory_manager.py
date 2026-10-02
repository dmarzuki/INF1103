import json
import os

FILE_NAME = "inventory.json"


def format_price(price):
    # turns 25.5 into "25.50" and 1200.0 into "1200.00"
    text = str(round(price, 2))
    parts = text.split(".")
    if len(parts) == 1:
        return text + ".00"
    if len(parts[1]) == 1:
        return text + "0"
    return text


def load_inventory():
    if os.path.exists(FILE_NAME):
        print("inventory.json found.")
        with open(FILE_NAME, "r") as file:
            inventory = json.load(file)
        print("Inventory loaded successfully.")
        return inventory
    else:
        print("inventory.json not found. Starting with an empty inventory.")
        return []


def save_inventory(inventory):
    with open(FILE_NAME, "w") as file:
        json.dump(inventory, file)


def display_all(inventory):
    print("Current Inventory")
    print("------------------------------------------------")
    if len(inventory) == 0:
        print("No products yet.")
    for product in inventory:
        print("ID:", product["id"], "| Name:", product["name"],
              "| Price: $" + format_price(product["price"]),
              "| Stock:", product["stock"])
    print("------------------------------------------------")


def search_product(inventory, product_id):
    for product in inventory:
        if product["id"] == product_id:
            return product
    return None


def add_product(inventory, product_id, name, price, stock):
    if search_product(inventory, product_id) is not None:
        return False
    product = {"id": product_id, "name": name, "price": price, "stock": stock}
    inventory.append(product)
    return True


def update_stock(inventory, product_id, new_stock):
    product = search_product(inventory, product_id)
    if product is None:
        return False
    product["stock"] = new_stock
    return True


def is_number(text):
    # True for "299.99" or "10", False for "abc" or ""
    parts = text.split(".")
    if len(parts) == 1:
        return parts[0].isdigit()
    if len(parts) == 2:
        return parts[0].isdigit() and parts[1].isdigit()
    return False


def print_menu():
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


def main():
    print("========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================")
    inventory = load_inventory()
    print_menu()

    while True:
        option = input("Enter option: ")

        if option == "1":
            display_all(inventory)

        elif option == "2":
            print("Add New Product")
            product_id = input("Product ID: ")
            name = input("Product Name: ")
            price_text = input("Price: ")
            stock_text = input("Stock Quantity: ")
            if not is_number(price_text) or not stock_text.isdigit():
                print("Error: price and stock must be numbers.")
                continue
            added = add_product(inventory, product_id, name,
                                float(price_text), int(stock_text))
            if added:
                print("Product added successfully!")
            else:
                print("Error: that Product ID already exists.")

        elif option == "3":
            print("Update Stock")
            product_id = input("Enter Product ID: ")
            product = search_product(inventory, product_id)
            if product is None:
                print("Product not found.")
                continue
            print("Product Found:")
            print("Name:", product["name"])
            print("Current Stock:", product["stock"])
            stock_text = input("New Stock Quantity: ")
            if not stock_text.isdigit():
                print("Error: stock must be a whole number.")
                continue
            update_stock(inventory, product_id, int(stock_text))
            print("Stock updated successfully!")

        elif option == "4":
            print("Search Product")
            product_id = input("Enter Product ID: ")
            product = search_product(inventory, product_id)
            if product is None:
                print("Product not found.")
            else:
                print("Product Found")
                print("------------------------------------------------")
                print("ID:", product["id"])
                print("Name:", product["name"])
                print("Price: $" + format_price(product["price"]))
                print("Stock:", product["stock"])
                print("------------------------------------------------")

        elif option == "5":
            print("Saving inventory...")
            save_inventory(inventory)
            print("Inventory saved successfully to inventory.json.")

        elif option == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Inventory saved successfully.")
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break

        else:
            print("Invalid option. Enter a number from 1 to 6.")


if __name__ == "__main__":
    main()