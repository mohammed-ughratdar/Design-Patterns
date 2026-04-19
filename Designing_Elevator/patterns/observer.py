from abc import abstractmethod, ABC

class ElevatorObserver(ABC):

    @abstractmethod
    def update(self, elevator):
        pass