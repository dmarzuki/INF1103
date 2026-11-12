# test_composition.py  -  Lab 8, section 4
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from order import Order

supplier = Supplier("S001", "TechSupply Pte Ltd", "sales@techsupply.com")
laptop = PhysicalProduct("P001", "Laptop", 1200.00, 15, supplier, 2.0)
mouse = PhysicalProduct("P002", "Mouse", 25.50, 40, supplier, 0.1)
antivirus = DigitalProduct("D001", "Antivirus Licence", 49.90, 100, supplier, 350.0)

# 1. create an Order and add products through add_order_line()
order1 = Order("O001")
order1.add_order_line(laptop, 1)
order1.add_order_line(mouse, 2)
order1.add_order_line(antivirus, 1)

# 2. display each line and the total
order1.display_order()      # expected total: 1200 + 51 + 49.90 = 1300.90

# 3. add the SAME product (laptop) to a different order
# Predict first: how many OrderLine objects and how many Product objects?
order2 = Order("O002")
order2.add_order_line(laptop, 3)
order2.display_order()

line_in_order1 = order1.get_order_lines()[0]
line_in_order2 = order2.get_order_lines()[0]
print("\nSame OrderLine object in both orders?", line_in_order1 is line_in_order2)
print("Same Product object in both lines?  ", line_in_order1.product is line_in_order2.product)
print("OrderLine ids:", id(line_in_order1), id(line_in_order2))
print("Product ids:  ", id(line_in_order1.product), id(line_in_order2.product))

# 4. remove an order line through an Order method
order1.remove_order_line("P002")
print("\nAfter removing the Mouse line from O001:")
order1.display_order()

# 5. remove the whole order: its lines go with it, but the products do not
del order1
print("\nAfter 'del order1', the laptop still exists:")
laptop.display_information()