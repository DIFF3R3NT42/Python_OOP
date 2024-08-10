from collections import defaultdict
from statistics import mean

from project.stores.base_store import BaseStore


class ToyStore(BaseStore):
    def __init__(self, name: str, location: str):
        super().__init__(name, location, capacity=100)  # Initial capacity is set to 100

    @property
    def store_type(self) -> str:
        return "ToyStore"

    def store_stats(self) -> str:
        product_summary = defaultdict(list)
        for product in self.products:
            product_summary[product.model].append(product.price)

        detailed_stats = "\n**Toys for sale:\n"

        # Sort models by name and compute stats
        for model in sorted(product_summary.keys()):
            prices = product_summary[model]
            num_of_product_pieces = len(prices)
            avg_price_per_model = mean(prices)
            detailed_stats += f"{model}: {num_of_product_pieces}pcs, average price: {avg_price_per_model:.2f}\n"

        estimated_profit = self.get_estimated_profit()

        store_information = (
            f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}\n"
            f"{estimated_profit}\n"
            f"{detailed_stats.strip()}"
        )

        return store_information