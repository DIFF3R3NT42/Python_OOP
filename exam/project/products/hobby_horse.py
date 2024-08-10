from project.products.base_product import BaseProduct


class HobbyHorse(BaseProduct):
    def __init__(self, model: str, price: float):
        super().__init__(model, price, material='Wood/Plastic', sub_type='Toys')

    def discount(self):
        self.price *= 0.8  # Reduce price by 20%
        return self.price
