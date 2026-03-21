from Strategy.DriveStrategy import DriveStrategy

# Concrete implementation of NormalDrive strategy
class NormalDrive(DriveStrategy):

    def drive(self):
        print("Normal Drive")