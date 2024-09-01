from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    @staticmethod
    def make_sound() -> str:
        return "Squeak"

    @property
    def weight_increment(self):
        return 0.10

    @property
    def allowed_food(self):
        return [Vegetable, Fruit]


class Dog(Mammal):
    @staticmethod
    def make_sound() -> str:
        return "Woof!"

    @property
    def weight_increment(self):
        return 0.40

    @property
    def allowed_food(self):
        return [Meat]


class Cat(Mammal):
    @staticmethod
    def make_sound() -> str:
        return "Meow"

    @property
    def weight_increment(self):
        return 0.30

    @property
    def allowed_food(self):
        return [Meat, Vegetable]


class Tiger(Mammal):
    @staticmethod
    def make_sound() -> str:
        return "ROAR!!!"

    @property
    def weight_increment(self):
        return 1.00

    @property
    def allowed_food(self):
        return [Meat]
