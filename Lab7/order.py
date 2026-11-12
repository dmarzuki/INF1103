# order.py
# Order: a customer order made up of OrderLine objects.
# COMPOSITION: the Order creates and owns its OrderLines. An OrderLine is
# never created outside an Order, never passed in, and never moved to
# another Order. When the Order goes, its OrderLines go with it.

from product import Product
from order_line import OrderLine


class Order:
    def __init__(self, order_id: str):
        self.order_id: str = order_id
        self.__order_lines: list[OrderLine] = []     # private: only Order manages its lines

    def add_order_line(self, product: Product, quantity: int) -> None:
        """Create the OrderLine HERE, inside the Order, and keep it."""
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def remove_order_line(self, product_id: str) -> bool:
        """Remove the line for this product. Returns False if there isn't one."""
        for order_line in self.__order_lines:
            if order_line.product.get_product_id() == product_id:
                self.__order_lines.remove(order_line)
                return True
        return False

    def calculate_total(self) -> float:
        """Ask each OrderLine for its subtotal and add them up."""
        total = 0.0
        for order_line in self.__order_lines:
            total += order_line.calculate_subtotal()
        return total

    def get_order_lines(self) -> list[OrderLine]:
        """A copy of the list, so outside code can't add or remove lines directly."""
        return list(self.__order_lines)

    def display_order(self) -> None:
        print(f"\n  Order {self.order_id}")
        print("  " + "-" * 40)
        for order_line in self.__order_lines:
            order_line.display_information()
        print("  " + "-" * 40)
        print(f"  {'Total':<26} ${self.calculate_total():>9.2f}")