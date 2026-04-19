from patterns.observer import ElevatorObserver
from models.elevator import Elevator

class UiObserver(ElevatorObserver):
    
    def update(self, elevator: Elevator):
        print(f"Elevator {elevator.id} is at floor {elevator.current_floor}")