from typing import Iterable, Optional

from strategies.interfaces import ElevatorStrategy
from models.elevator import Elevator


class NearestElevatorStrategy(ElevatorStrategy):

    def find_elevator(self, elevators: Iterable[Elevator]) -> Optional[Elevator]:
        return next(iter(elevators), None)