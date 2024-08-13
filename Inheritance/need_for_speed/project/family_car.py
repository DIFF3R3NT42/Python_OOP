from project.car import Car


class FamilyCar(Car):
    DEFAULT_FUEL_CONSUMPTION: float = 3

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)