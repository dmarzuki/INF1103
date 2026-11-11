# file_handler.py
# File handling only: loads and saves the inventory as JSON.
# Kept out of Product and Inventory so each class has one responsibility.

import json
import os

from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from supplier import Supplier

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
    suppliers = {}
    for item in data:
        try:
            inventory.add_product(product_from_dict(item, suppliers))
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

DEFAULT_SUPPLIER = Supplier("S000", "Unknown Supplier", "-")


def supplier_from_dict(data: dict, suppliers: dict) -> Supplier:
    """Rebuild a Supplier, reusing the same object if that ID was already loaded."""
    supplier_id = data["supplier_id"]
    if supplier_id not in suppliers:
        suppliers[supplier_id] = Supplier(supplier_id, data["name"], data["contact_email"])
    return suppliers[supplier_id]


def product_from_dict(item: dict, suppliers: dict):
    """Rebuild the correct kind of Product from one saved dictionary."""
    if "supplier" in item:
        supplier = supplier_from_dict(item["supplier"], suppliers)
    else:
        supplier = DEFAULT_SUPPLIER        # older files saved before Lab 8
    product_type = item.get("type", "physical")
    product_id = item["id"]
    name = item["name"]
    price = float(item["price"])
    stock = int(item["stock"])

    if product_type == "digital":
        return DigitalProduct(product_id, name, price, stock, supplier, float(item["download_size"]))
    return PhysicalProduct(product_id, name, price, stock, supplier, float(item.get("weight", 0)))