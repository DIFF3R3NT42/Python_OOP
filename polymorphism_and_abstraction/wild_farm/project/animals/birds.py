from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit, Seed


class Owl(Bird):
    @staticmethod
    def make_sound() -> str:
        return "Hoot Hoot"

    @property
    def weight_increment(self):
        return 0.25

    @property
    def allowed_food(self):
        return [Meat]


class Hen(Bird):
    @staticmethod
    def make_sound() -> str:
        return "Cluck"

    @property
    def weight_increment(self):
        return 0.35

    @property
    def allowed_food(self):
        return [Vegetable, Fruit, Meat, Seed]
