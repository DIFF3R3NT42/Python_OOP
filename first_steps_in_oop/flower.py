class Flower:
    def __init__(self, name, water_requirements: int):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False

    def water(self, quantity: int):
        if quantity >= self.water_requirements:
            self.is_happy = True

    def status(self) ->str:
        if self.is_happy == True:
            return f"{self.name} is happy"
        else:
            return f"{self.name} is not happy"
