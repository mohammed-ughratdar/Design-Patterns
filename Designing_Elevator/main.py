from elevator_system import ElevatorSystem
from models.elevator import Elevator
from enums import Direction
from ui_observer import UiObserver


def main():
    elevator_system = ElevatorSystem()

    elevator_one = Elevator(1)
    elevator_two = Elevator(2)

    # Register the same elevator objects that own observers.
    elevator_system.add_elevator(elevator_one.id, elevator_one)
    elevator_system.add_elevator(elevator_two.id, elevator_two)

    observer_one = UiObserver()
    observer_two = UiObserver()

    elevator_one.add_observer(observer_one)
    elevator_one.add_observer(observer_two)
    elevator_two.add_observer(observer_one)
    elevator_two.add_observer(observer_two)

    elevator_system.add_request(10, Direction.UP)
    elevator_system.add_request(5, Direction.DOWN)

    elevator_one.simulate_movement()
    elevator_two.simulate_movement()


if __name__ == "__main__":
    main()