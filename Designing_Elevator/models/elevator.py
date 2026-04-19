from typing import List, Set
from patterns.observer import ElevatorObserver
from patterns.idle_state import IdleState
from patterns.state import ElevatorState
from models.request import Request
import time

class Elevator:
    def __init__(self, id: str):
        self.id = id
        self.current_floor = 0
        self.state = IdleState()
        self.observers: List[ElevatorObserver] = []
        self.up_requests: Set[int] = set()
        self.down_requests: Set[int] = set()
        
    def add_observer(self, observer: ElevatorObserver):
        self.observers.append(observer)
        
    def remove_observer(self, observer: ElevatorObserver):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)

    def add_request(self, request: Request):
        self.state.add_request(self, request)
        self.notify_observers()

    def move(self):
        self.state.move(self)
        self.notify_observers()

    def get_direction(self):
        return self.state.get_direction()

    def get_current_floor(self):
        return self.current_floor

    def set_current_floor(self, floor: int):
        self.current_floor = floor

    def set_state(self, state: ElevatorState):
        self.state = state

    def get_up_requests(self):
        return self.up_requests

    def get_down_requests(self):
        return self.down_requests

    def set_up_requests(self, requests: Set[int]):
        self.up_requests = requests

    def set_down_requests(self, requests: Set[int]):
        self.down_requests = requests

    def simulate_movement(self):
        for _ in range(10):
            self.move()
            time.sleep(1)

