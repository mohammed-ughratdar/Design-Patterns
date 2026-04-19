from abc import ABC, abstractmethod
from typing import Iterable, Optional

from models.elevator import Elevator

class ElevatorStrategy(ABC):
    
    @abstractmethod
    def find_elevator(self, elevators: Iterable[Elevator]) -> Optional[Elevator]:
        raise NotImplementedError
