from abc import ABC, abstractmethod
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from models.seat import Seat
    from models.show import Show


class SeatAvailabilityObserver(ABC):

    @abstractmethod
    def on_seat_availability_change(self, seat: "Seat", show: Optional["Show"] = None):
        pass
