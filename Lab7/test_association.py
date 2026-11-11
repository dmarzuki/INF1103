from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

# 1. create the Supplier on its own first
supplier = Supplier("S001", "TechSupply Pte Ltd", "sales@techsupply.com")

# 2. create one of each product type, giving both the SAME supplier object
laptop = PhysicalProduct("P006", "Laptop", 1200.00, 15, supplier, 2.0)
antivirus = DigitalProduct("D009", "Antivirus Licence", 49.90, 100, supplier, 350.0)

# 3. show the supplier through each product
print("Laptop's supplier:")
laptop.get_supplier().display_information()
print("\nAntivirus's supplier:")
antivirus.get_supplier().display_information()

# 4. separate objects, but both products point to the same supplier
print("\nBoth products share one Supplier object:", laptop.get_supplier() is antivirus.get_supplier())
print("Supplier is a different object from the product:", laptop.get_supplier() is not laptop)

# Predict first: what happens after del supplier?
del supplier
print("\nAfter 'del supplier':")
laptop.get_supplier().display_information()