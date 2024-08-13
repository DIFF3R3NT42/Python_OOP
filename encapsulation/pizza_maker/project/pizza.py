from project.dough import Dough


class Pizza:
    def __init__(self, name: str, dough: Dough, toppings: dict):
        self.name = name
        self.dough = dough
        self.toppings = toppings

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")

    @property
    def toppings(self):
        return self.__toppings

    @.setter
    def (self, value):
        pass