from Strategy.DriveStrategy import DriveStrategy

# Abstract class for vehicles
class Vehicle:
   
    def __init__(self, drive_strategy: DriveStrategy):
        self.drive_strategy = drive_strategy

    def drive(self):
        self.drive_strategy.drive()