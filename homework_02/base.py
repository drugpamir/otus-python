from abc import ABC

from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight: int = 1000, fuel: int = 0, fuel_consumption: int = 10):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.fuel > 0:
            self.started = True
        else:
            raise LowFuelError

    def move(self, distance: int):
        fuel_needed = self.fuel_consumption * distance
        if self.fuel < fuel_needed:
            raise NotEnoughFuel
        self.fuel -= fuel_needed
