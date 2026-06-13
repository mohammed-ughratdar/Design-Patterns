from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from models.enums import SeatType

if TYPE_CHECKING:
    from models.show import Show


class PricingStrategy(ABC):

    @abstractmethod
    def calculate_price(self, seat_type: SeatType, show: "Show") -> float:
        pass
