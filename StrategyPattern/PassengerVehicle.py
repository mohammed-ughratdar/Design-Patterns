from Vehicle import Vehicle
from Strategy.NormalDrive import NormalDrive

# Concrete implementation of PassengerVehicle class
class PassengerVehicle(Vehicle):
    def __init__(self):
        super().__init__(NormalDrive())

    def drive(self):
        print("Passenger Vehicle")
        super().drive()