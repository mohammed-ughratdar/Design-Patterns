from Vehicle import Vehicle
from Strategy.SpecialDrive import SpecialDrive

# Concrete implementation of OffRoadVehicle class
class OffRoadVehicle(Vehicle):
    def __init__(self):
        super().__init__(SpecialDrive())

    def drive(self):
        print("Off Road Vehicle")
        super().drive()