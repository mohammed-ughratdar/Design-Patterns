from abc import ABC, abstractmethod
from enums import Direction

class ElevatorState(ABC):

    @abstractmethod
    def add_request(self, elevator: 'Elevator', request: 'Request'):
        pass

    @abstractmethod
    def move(self, elevator: 'Elevator'):
        pass

    @abstractmethod
    def get_direction(self) -> Direction:
        pass
