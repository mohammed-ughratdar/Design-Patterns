from datetime import datetime
from typing import TYPE_CHECKING

from models.enums import SeatStatus
from patterns.state import SeatState

if TYPE_CHECKING:
    from models.seat import Seat


class AvailableState(SeatState):

    def reserve(self, seat: "Seat") -> bool:
        from states.reserved_state import ReservedState

        seat.set_state(ReservedState())
        seat.set_reservation_time(datetime.now())
        return True

    def book(self, seat: "Seat") -> bool:
        return False

    def release(self, seat: "Seat") -> bool:
        return False

    def get_status(self) -> SeatStatus:
        return SeatStatus.AVAILABLE
