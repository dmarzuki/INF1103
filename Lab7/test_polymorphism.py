# test_polymorphism.py  -  Lab 8, section 7
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory

supplier = Supplier("S001", "TechSupply Pte Ltd", "sales@techsupply.com")

# both product types go into the SAME inventory
inventory = Inventory()
inventory.add_product(PhysicalProduct("P001", "Laptop", 1200.00, 15, supplier, 2.0))
inventory.add_product(DigitalProduct("D001", "Antivirus Licence", 49.90, 100, supplier, 350.0))
inventory.add_product(PhysicalProduct("P002", "Mouse", 25.50, 40, supplier, 0.1))

# Predict first: what will get_fulfilment_info() print for each product?
# ONE loop, no isinstance(): each object runs its own version of the method
for product in inventory.get_products():
    product.display_information()
    print("         Fulfilment:", product.get_fulfilment_info())
    print()