# test_lsp.py  -  Lab 8, section 6 (Liskov Substitution Principle)
from supplier import Supplier
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory


# 6.2 a function that only knows about Product, not the subclasses
def show_product_details(product: Product) -> None:
    product.display_information()
    print("         Fulfilment:", product.get_fulfilment_info())


supplier = Supplier("S001", "TechSupply Pte Ltd", "sales@techsupply.com")
laptop = PhysicalProduct("P001", "Laptop", 1200.00, 15, supplier, 2.0)
antivirus = DigitalProduct("D001", "Antivirus Licence", 49.90, 100, supplier, 350.0)

print("=== 6.2 Same function, both product types ===")
show_product_details(laptop)
show_product_details(antivirus)

print("\n=== 6.2 Both types work with Inventory's normal operations ===")
inventory = Inventory()
print("add laptop:   ", inventory.add_product(laptop))
print("add antivirus:", inventory.add_product(antivirus))
inventory.display_all()
print("find D001:    ", inventory.find_product("D001").get_name())
print("remove P001:  ", inventory.remove_product("P001").get_name())
print("left in inventory:", len(inventory.get_products()))

print("\n=== 6.3 Product's expectation: update_stock refuses negatives, returns bool ===")
for product in [laptop, antivirus]:
    ok = product.update_stock(20)
    bad = product.update_stock(-5)
    print(f"{product.get_name():<18} update_stock(20) -> {ok}, update_stock(-5) -> {bad}, stock = {product.get_stock()}")


print("\n=== 6.3 Diagnose: the teammate's DigitalProduct breaks LSP ===")
class BadDigitalProduct(DigitalProduct):
    def update_stock(self, quantity: int) -> None:
        raise NotImplementedError("Digital products have no stock")

ebook = BadDigitalProduct("D999", "E-book", 9.90, 50, supplier, 5.0)
show_product_details(ebook)                  # still fine here...
try:
    ebook.update_stock(10)                   # ...but crashes on normal Product behaviour
except NotImplementedError as error:
    print("update_stock crashed:", error)