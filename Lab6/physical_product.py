from product import Product
from can_be_shipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def display_information(self):
        super().display_information()
        print(f"        Type: Physical  Weight: {self.__weight} kg")

    def get_fulfilment_info(self) -> str:
        return "Requires physical shipping from our warehouse."

    def calculate_shipping_cost(self):
        return round(5.00 + 2.00 * self.__weight, 2)

    def to_dict(self) -> dict:
        data = super().to_dict()      # id, name, price, stock from Product
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data    