# test_aggregation.py  -  Lab 8, section 3
from supplier import Supplier
from physical_product import PhysicalProduct
from inventory import Inventory

supplier = Supplier("S001", "TechSupply Pte Ltd", "sales@techsupply.com")

# 1. create the Product BEFORE any Inventory exists
mouse = PhysicalProduct("P002", "Mouse", 25.50, 40, supplier, 0.1)
print("1. Product created on its own, before any inventory:")
mouse.display_information()

# 2. add it to Inventory A
inventory_a = Inventory()
inventory_b = Inventory()
inventory_a.add_product(mouse)
print("\n2. Added to Inventory A. Products in A:", len(inventory_a.get_products()))

# 3. remove it from Inventory A, then check the product still works
# Predict first: will the product still work after this?
removed = inventory_a.remove_product("P002")
print("\n3. Removed from Inventory A. Products in A:", len(inventory_a.get_products()))
print("   Found in A?", inventory_a.find_product("P002"))
print("   Product still works after removal:")
mouse.display_information()
mouse.update_stock(35)
print("   Stock updated to:", mouse.get_stock())

# 4. add the SAME product object to Inventory B
inventory_b.add_product(removed)
print("\n4. Added to Inventory B. Products in B:", len(inventory_b.get_products()))

# 5. confirm it is the same object, not a copy, and nothing was destroyed
print("\n5. Same object that was in A?", inventory_b.find_product("P002") is mouse)
print("   Stock carried over (35)?", inventory_b.find_product("P002").get_stock())

# what if an inventory is emptied completely?
inventory_b.remove_product("P002")
print("\n   Inventory B emptied. Products in B:", len(inventory_b.get_products()))
print("   Mouse still exists:", mouse.get_name())