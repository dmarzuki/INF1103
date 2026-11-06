# file_handler.py
# File handling only: loads and saves the inventory as JSON.
# Kept out of Product and Inventory so each class has one responsibility.

import json
import os

from physical_product import PhysicalProduct
from digital_product import DigitalProduct
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
        try:
            inventory.add_product(product_from_dict(item))
        except (KeyError, ValueError):
            print("  (Skipped a product that could not be read.)")
    return inventory


def save_inventory(inventory: Inventory, file_name: str = FILE_NAME) -> None:
    """Turn every Product into a dictionary and write them all to the JSON file."""
    data = []
    for product in inventory.get_products():
        data.append(product.to_dict())
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

def product_from_dict(item: dict):
    """Rebuild the correct kind of Product from one saved dictionary."""
    product_type = item.get("type", "physical")
    product_id = item["id"]
    name = item["name"]
    price = float(item["price"])
    stock = int(item["stock"])

    if product_type == "digital":
        return DigitalProduct(product_id, name, price, stock, float(item["download_size"]))
    return PhysicalProduct(product_id, name, price, stock, float(item.get("weight", 0)))
