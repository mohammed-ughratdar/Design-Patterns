from patterns.state import ElevatorState
from enums import Direction
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.elevator import Elevator
    from models.request import Request


class IdleState(ElevatorState):

    def add_request(self, elevator: 'Elevator', request: 'Request'):
        from patterns.moving_up_state import MovingUpState
        from patterns.moving_down_state import MovingDownState

        if request.target_floor > elevator.current_floor:
            elevator.set_state(MovingUpState())
            elevator.up_requests.add(request.target_floor)
        else:
            elevator.set_state(MovingDownState())
            elevator.down_requests.add(request.target_floor)

    def move(self, elevator: 'Elevator'):
        pass

    def get_direction(self):
        return Direction.IDLE