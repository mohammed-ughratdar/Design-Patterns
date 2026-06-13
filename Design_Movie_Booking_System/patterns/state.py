from abc import ABC, abstractmethod

from models.enums import SeatStatus
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.seat import Seat


class SeatState(ABC):

    @abstractmethod
    def reserve(self, seat: "Seat") -> bool:
        pass

    @abstractmethod
    def book(self, seat: "Seat") -> bool:
        pass

    @abstractmethod
    def release(self, seat: "Seat") -> bool:
        pass

    @abstractmethod
    def get_status(self) -> SeatStatus:
        pass
