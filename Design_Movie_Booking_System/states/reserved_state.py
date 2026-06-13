from typing import TYPE_CHECKING

from models.enums import SeatStatus
from patterns.state import SeatState

if TYPE_CHECKING:
    from models.seat import Seat


class ReservedState(SeatState):

    def reserve(self, seat: "Seat") -> bool:
        return False

    def book(self, seat: "Seat") -> bool:
        from states.booked_state import BookedState

        seat.set_state(BookedState())
        return True

    def release(self, seat: "Seat") -> bool:
        from states.available_state import AvailableState

        seat.set_state(AvailableState())
        seat.set_reservation_time(None)
        return True

    def get_status(self) -> SeatStatus:
        return SeatStatus.RESERVED
