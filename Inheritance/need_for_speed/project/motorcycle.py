from project.vehicle import Vehicle


class Motorcycle(Vehicle):
    DEFAULT_FUEL_CONSUMPTION: float = 1.25

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)
