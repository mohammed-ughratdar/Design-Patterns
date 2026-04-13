from enums import VehicleSize

class Vehicle:

    def __init__(self, license_number: str, size: VehicleSize):
        self.license_number = license_number
        self.size = size

    def get_size(self):
        return self.size

    def get_license_number(self):
        return self.license_number


class Car(Vehicle):

    def __init__(self, license_number):
        super().__init__(license_number, VehicleSize.MEDIUM)


class Bike(Vehicle):

    def __init__(self, license_number):
        super().__init__(license_number, VehicleSize.SMALL)


class Truck(Vehicle):

    def __init__(self, license_number):
        super().__init__(license_number, VehicleSize.LARGE)


class VehicleFactory:

    @staticmethod
    def create_vehicle(license_number: str, vehicle_size: VehicleSize):
        if vehicle_size == VehicleSize.SMALL:
            return Bike(license_number)
        elif vehicle_size == VehicleSize.MEDIUM:
            return Car(license_number)
        elif vehicle_size == VehicleSize.LARGE:
            return Truck(license_number)
        else:
            raise ValueError(f"Invalid vehicle size: {vehicle_size}")