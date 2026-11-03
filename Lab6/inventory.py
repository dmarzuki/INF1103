# inventory.py
# The Inventory class: manages a COLLECTION of Product objects.
# It does not load or save files, show menus or ask for input (SRP).

from product import Product


class Inventory:
    """Holds all the products in the store."""

    def __init__(self):
        self.__products = []          # a list of Product objects

    def add_product(self, product: Product) -> bool:
        """Add a product. Refuses a duplicate ID and returns False."""
        if self.search_product(product.get_product_id()) is not None:
            return False
        self.__products.append(product)
        return True

    def search_product(self, product_id: str):
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

    def get_products(self) -> list:
        """A copy of the product list, so outside code can't change the real one."""
        return list(self.__products)
