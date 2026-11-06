# product.py
# The Product class: represents and manages ONE product.
# It does not load or save files, show menus or ask for input (SRP).
from abc import ABC, abstractmethod

class Product(ABC):
    """One item in the store, with its own ID, name, price and stock."""
    
    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass

    def __init__(self, product_id: str, name: str, price: float, stock: int):
        # double underscore = treat as private; change only through methods
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    # ---------- getters: let other code read the data, not change it ----------

    def get_product_id(self) -> str:
        return self.__product_id

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price

    def get_stock(self) -> int:
        return self.__stock

    # ---------- behaviour ----------

    def update_stock(self, quantity: int) -> bool:
        """Set a new stock level. Refuses negative values, so stock is never invalid."""
        if quantity < 0:
            return False
        self.__stock = quantity
        return True

    def display_information(self) -> None:
        """Print this product's details on one line."""
        print(f"  {self.__product_id:<6} {self.__name:<20} ${self.__price:>9.2f}   Stock: {self.__stock}")

    def to_dict(self) -> dict:
        """The product's data as a dictionary, so it can be saved as JSON."""
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
        }
