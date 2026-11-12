# inventory.py
# The Inventory class: manages a COLLECTION of Product objects.
# AGGREGATION: the inventory holds references to products, but it does not
# create them or control their lifecycle. Removing a product from the
# inventory does not destroy the product.
# It does not load or save files, show menus or ask for input (SRP).

from product import Product


class Inventory:
    """Holds all the products in the store."""

    def __init__(self):
        self.__products: list[Product] = []      # any kind of Product, not just one subclass

    def add_product(self, product: Product) -> bool:
        """Add an existing Product. Refuses a duplicate ID and returns False."""
        if self.find_product(product.get_product_id()) is not None:
            return False
        self.__products.append(product)
        return True

    def remove_product(self, product_id: str) -> Product | None:
        """Take the product out of this inventory and hand it back.
        The product itself is NOT destroyed. Returns None if it isn't here."""
        product = self.find_product(product_id)
        if product is not None:
            self.__products.remove(product)
        return product

    def find_product(self, product_id: str) -> Product | None:
        """Return the Product with this ID, or None if there isn't one."""
        for product in self.__products:
            if product.get_product_id().upper() == product_id.upper():
                return product
        return None

    def display_all(self) -> None:
        """Print every product, or a message if the inventory is empty."""
        if len(self.__products) == 0:
            print("\n  The inventory is empty.\n")
            return
        print()
        print(f"  {'ID':<6} {'Name':<20} {'Price':>10}   Stock")
        print("  " + "-" * 50)
        for product in self.__products:
            product.display_information()
        print()

    def get_products(self) -> list[Product]:
        """A copy of the product list, so outside code can't change the real one."""
        return list(self.__products)
