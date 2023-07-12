"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo: int
    max_cargo: int

    def __init__(self, weight: int = 10000, fuel: int = 0, fuel_consumption: int = 1000, max_cargo: int = 5000):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, cargo: int):
        if self.max_cargo - self.cargo >= cargo:
            self.cargo += cargo
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo
