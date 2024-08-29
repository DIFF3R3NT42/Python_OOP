from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance: int):
        pass

    @abstractmethod
    def refuel(self, fuel: int):
        pass


class Car(Vehicle):
    AC_CONSUMPTION = 0.9

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: int) -> None:
        fuel_needed = distance * (self.fuel_consumption * self.AC_CONSUMPTION)
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel: int) -> None:
        self.fuel_quantity += fuel

class Truck(Vehicle):
    AC_CONSUMPTION = 1.6
    HOLE_IN_FUEL_TANK = 0.95

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: int) -> None:
        fuel_needed = distance * (self.fuel_consumption * self.AC_CONSUMPTION)
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel: int) -> None:
        self.fuel_quantity += fuel * self.HOLE_IN_FUEL_TANK
