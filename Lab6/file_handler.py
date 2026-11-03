# file_handler.py
# File handling only: loads and saves the inventory as JSON.
# Kept out of Product and Inventory so each class has one responsibility.

import json
import os

from product import Product
from inventory import Inventory

FILE_NAME = "inventory.json"


def load_inventory(file_name: str = FILE_NAME) -> Inventory:
    """Read the JSON file and rebuild the Inventory of Product objects."""
    inventory = Inventory()
    if not os.path.exists(file_name):
        return inventory                       # first run: start empty

    try:
        with open(file_name, "r") as file:
            data = json.load(file)
    except (json.JSONDecodeError, OSError):
        print("  (Could not read " + file_name + ", starting with an empty inventory.)")
        return inventory

    for item in data:
        product = Product(item["id"], item["name"], float(item["price"]), int(item["stock"]))
        inventory.add_product(product)
    return inventory


def save_inventory(inventory: Inventory, file_name: str = FILE_NAME) -> None:
    """Turn every Product into a dictionary and write them all to the JSON file."""
    data = []
    for product in inventory.get_products():
        data.append(product.to_dict())
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)
