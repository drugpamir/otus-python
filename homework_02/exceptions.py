"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(BaseException):
    print("Fuel is low")


class NotEnoughFuel(BaseException):
    print("Fuel is not enough")


class CargoOverload(BaseException):
    print("Cargo is overloaded")