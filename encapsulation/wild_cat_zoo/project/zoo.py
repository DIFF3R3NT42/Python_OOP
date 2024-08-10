from project.animal import Animal


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: list = []
        self.workers: list = []

    def add_animal(self, animal: Animal, price: int):
        if self.__budget <= price:
            return f"Not enough budget"

        if animal <= len(self.animals):