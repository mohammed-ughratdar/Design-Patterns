from abc import abstractmethod
# Abstract class for drive strategies
class DriveStrategy:

    @abstractmethod
    def drive(self):
        pass