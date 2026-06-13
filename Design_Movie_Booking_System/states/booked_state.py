from typing import TYPE_CHECKING

from models.enums import SeatStatus
from patterns.state import SeatState

if TYPE_CHECKING:
    from models.seat import Seat


class BookedState(SeatState):

    def reserve(self, seat: "Seat") -> bool:
        return False

    def book(self, seat: "Seat") -> bool:
        return False

    def release(self, seat: "Seat") -> bool:
        return False

    def get_status(self) -> SeatStatus:
        return SeatStatus.BOOKED
