from Strategy.DriveStrategy import DriveStrategy

# Concrete implementation of SpecialDrive strategy
class SpecialDrive(DriveStrategy):

    def drive(self):
        print("Special Drive")