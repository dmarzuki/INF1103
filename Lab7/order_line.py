# order_line.py
# OrderLine: one product and how many of it, inside ONE Order.
# It is a PART of an Order (composition). Only Order should create it.
# It REFERS to a Product but does not own it (the Product lives on its own).

from product import Product


class OrderLine:
    def __init__(self, product: Product, quantity: int):
        self.product: Product = product      # a reference, not ownership
        self.quantity: int = quantity

    def calculate_subtotal(self) -> float:
        return self.product.get_price() * self.quantity

    def display_information(self) -> None:
        print(f"  {self.product.get_name():<20} x{self.quantity:<4} ${self.calculate_subtotal():>9.2f}")