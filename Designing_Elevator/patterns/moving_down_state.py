from patterns.state import ElevatorState
from enums import Direction
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.elevator import Elevator
    from models.request import Request

class MovingDownState(ElevatorState):
    def add_request(self, elevator: 'Elevator', request: 'Request'):
        if request.get_target_floor() < elevator.current_floor:
            elevator.get_down_requests().add(request.get_target_floor())
        else:
            elevator.add_up_request(request.get_target_floor())

    def move(self, elevator: 'Elevator'):
        if not elevator.get_down_requests():
            if elevator.get_up_requests():
                from patterns.moving_up_state import MovingUpState

                elevator.set_state(MovingUpState())
                return
            else:
                from patterns.idle_state import IdleState

                elevator.set_state(IdleState())
                return
        next_floor = max(elevator.get_down_requests())
        if elevator.get_current_floor() > next_floor:
            elevator.set_current_floor(elevator.get_current_floor() - 1)
        if elevator.get_current_floor() == next_floor:
            elevator.get_down_requests().remove(next_floor)

    def get_direction(self):
        return Direction.DOWN