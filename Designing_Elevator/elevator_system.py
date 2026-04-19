from typing import List, Dict
from models.elevator import Elevator
from models.request import Request
from enums import Direction, RequestType
from strategies.implementations import NearestElevatorStrategy
class ElevatorSystem:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        
        return cls._instance


    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self.elevators: Dict[int, Elevator] = {}
        self.elevator_strategy: ElevatorStrategy = NearestElevatorStrategy()


    def add_elevator(self, id: int, elevator: Elevator):
        self.elevators[elevator.id] = elevator

    def remove_elevator(self, elevator: Elevator):
        del self.elevators[elevator.id]

   
    def add_request(self, target_floor: int, direction: Direction):
        request = Request(target_floor, direction, RequestType.EXTERNAL)
        elevator = self.elevator_strategy.find_elevator(self.elevators.values())
        if elevator:
            elevator.add_request(request)
        else:
            print("No elevator available")
  
