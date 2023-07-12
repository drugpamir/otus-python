"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class VehicleException(BaseException):
    pass


class LowFuelError(VehicleException):
    print("Fuel is low")


class NotEnoughFuel(VehicleException):
    print("Fuel is not enough")


class CargoOverload(VehicleException):
    print("Cargo is overloaded")