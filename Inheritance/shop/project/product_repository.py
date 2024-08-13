from typing import List

from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        for p in self.products:
            if product_name == self.products:
                return p

    def remove(self, product_name: str) -> bool:
        product_to_remove = self.find(product_name)
        if product_to_remove:
            self.products.remove(product_to_remove)
            return True
        return False  # If the product was not found and thus not removed

    def __repr__(self) -> str:
        return "\n".join([f"{product.name}: {product.quantity}" for product in self.products])
