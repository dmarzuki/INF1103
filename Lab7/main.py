# main.py
# The main program: shows the menu, gets user input,
# and calls the right Inventory / Product methods.

from physical_product import PhysicalProduct
from digital_product import DigitalProduct 
from can_be_shipped import CanBeShipped
from file_handler import load_inventory, save_inventory
from supplier import Supplier


def is_positive_number(text: str) -> bool:
     """True if the text is a number of 0 or more, e.g. '25.50'."""
     try:
        return float(text) >= 0
     except ValueError:
        return False

def print_menu() -> None:
    print("===== Inventory Management System =====")
    print("1. Display all products")
    print("2. Add a product")
    print("3. Update stock")
    print("4. Search for a product")
    print("5. Save inventory")
    print("6. Exit")


def add_new_product(inventory) -> None:
    kind = input("Physical or digital product? (P/D): ").strip().upper()
    if kind not in ("P", "D"):
        print("Please enter P or D.\n")
        return
    
    product_id = input("Enter product ID: ").strip().upper()
    if product_id == "":
        print("Product ID cannot be empty.\n")
        return
    if inventory.search_product(product_id) is not None:
        print("A product with ID " + product_id + " already exists.\n")
        return

    name = input("Enter product name: ").strip()
    if name == "":
        print("Product name cannot be empty.\n")
        return

    price_text = input("Enter price: ").strip()
    if not is_positive_number(price_text) or float(price_text) < 0:
        print("Price must be a positive number.\n")
        return

    stock_text = input("Enter stock quantity: ").strip()
    if not stock_text.isdigit():
        print("Stock must be a whole number of 0 or more.\n")
        return

    if kind == "P":
        extra = input("Enter weight (kg): ").strip()
        if not is_positive_number(extra):
            print("Weight must be a number of 0 or more.\n")
            return
        product = PhysicalProduct(product_id, name, float(price_text), int(stock_text), MAIN_SUPPLIER, float(extra))
    else:
        extra = input("Enter download size (MB): ").strip()
        if not is_positive_number(extra):
            print("Download size must be a number of 0 or more.\n")
            return
        product = DigitalProduct(product_id, name, float(price_text), int(stock_text), MAIN_SUPPLIER, float(extra))

    inventory.add_product(product)
    print("Product " + product_id + " added.\n")

def update_product_stock(inventory) -> None:
    product_id = input("Enter product ID: ").strip()
    product = inventory.search_product(product_id)
    if product is None:
        print("Product not found.\n")
        return

    stock_text = input("Enter new stock quantity: ").strip()
    if not stock_text.isdigit():
        print("Stock must be a whole number of 0 or more.\n")
        return

    if product.update_stock(int(stock_text)):
        print("Stock for " + product.get_name() + " updated to " + stock_text + ".\n")
    else:
        print("Stock could not be updated.\n")


def find_product(inventory) -> None:
    product_id = input("Enter product ID to search: ").strip()
    product = inventory.search_product(product_id)
    if product is None:
        print("Product not found.\n")
    else:
        print()
        product.display_information()
        print("         Fulfilment: " + product.get_fulfilment_info())
    # only products that signed the CanBeShipped contract have a shipping cost
    if isinstance(product, CanBeShipped):
        print(f"         Shipping cost: ${product.calculate_shipping_cost():.2f}")
    print()



def main() -> None:
    inventory = load_inventory()

    # first run: start with some sample products
    if len(inventory.get_products()) == 0:
        inventory.add_product(PhysicalProduct("P001", "Laptop", 1200.00, 15, supplier, 2.0))
        inventory.add_product(PhysicalProduct("P002", "Mouse", 25.50, 40, supplier, 0.1))
        inventory.add_product(DigitalProduct("D003", "Antivirus License", 49.90, 100, supplier, 350))

    while True:
        print_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            inventory.display_all()
        elif choice == "2":
            add_new_product(inventory)
        elif choice == "3":
            update_product_stock(inventory)
        elif choice == "4":
            find_product(inventory)
        elif choice == "5":
            save_inventory(inventory)
            print("Inventory saved.\n")
        elif choice == "6":
            save_inventory(inventory)
            print("Inventory saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.\n")


if __name__ == "__main__":
    main()
