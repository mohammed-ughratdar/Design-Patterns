from typing import TYPE_CHECKING

from models.enums import SeatType
from patterns.strategy import PricingStrategy

if TYPE_CHECKING:
    from models.show import Show


class RegularPricingStrategy(PricingStrategy):
    BASE_PRICE = 100

    def calculate_price(self, seat_type: SeatType, show: "Show") -> float:
        if seat_type == SeatType.REGULAR:
            return self.BASE_PRICE

        return 0.0
