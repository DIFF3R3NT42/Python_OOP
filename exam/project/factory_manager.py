from collections import defaultdict

from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:
    def __init__(self, name: str):
        self.name = name
        self.income = 0.0
        self.products = []
        self.stores = []

    def produce_item(self, product_type: str, model: str, price: float):
        if product_type == "Chair":
            product = Chair(model=model, price=price)
        elif product_type == "HobbyHorse":
            product = HobbyHorse(model=model, price=price)
        else:
            raise Exception("Invalid product type!")

        self.products.append(product)
        return f"A product of sub-type {product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        if any(store.name == name for store in self.stores):
            raise Exception("Store with this name already registered!")

        if store_type == "FurnitureStore":
            store = FurnitureStore(name=name, location=location)
        elif store_type == "ToyStore":
            store = ToyStore(name=name, location=location)
        else:
            raise Exception(f"{store_type} is an invalid type of store!")

        self.stores.append(store)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."

        matching_products = [p for p in products if
                             (p.sub_type == "Furniture" and isinstance(store, FurnitureStore)) or (
                                         p.sub_type == "Toys" and isinstance(store, ToyStore))]

        if not matching_products:
            return "Products do not match in type. Nothing sold."

        for product in matching_products:
            self.products.remove(product)
            store.products.append(product)
            store.capacity -= 1
            self.income += product.price

        return f"Store {store.name} successfully purchased {len(matching_products)} items."

    def unregister_store(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)

        if store is None:
            raise Exception("No such store!")

        if store.products:
            return "The store is still having products in stock! Unregistering is inadvisable."

        self.stores.remove(store)
        return f"Successfully unregistered store {store.name}, location: {store.location}."

    def discount_products(self, product_model: str):
        discount_count = 0

        for product in self.products:
            if product.model == product_model:
                product.discount()
                discount_count += 1

        return f"Discount applied to {discount_count} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)

        if store is None:
            return "There is no store registered under this name!"

        return store.store_stats()

    def statistics(self):
        product_summary = defaultdict(int)
        total_net_price = 0.0

        for product in self.products:
            product_summary[product.model] += 1
            total_net_price += product.price

        unsold_products = "\n".join([f"{model}: {count}" for model, count in sorted(product_summary.items())])

        partner_stores = "\n".join(sorted(store.name for store in self.stores))

        return (
            f"Factory: {self.name}\n"
            f"Income: {self.income:.2f}\n"
            f"***Products Statistics***\n"
            f"Unsold Products: {len(self.products)}. Total net price: {total_net_price:.2f}\n"
            f"{unsold_products}\n"
            f"***Partner Stores: {len(self.stores)}***\n"
            f"{partner_stores}"
        )
