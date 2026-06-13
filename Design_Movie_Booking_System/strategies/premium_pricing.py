from typing import TYPE_CHECKING

from models.enums import SeatType
from patterns.strategy import PricingStrategy

if TYPE_CHECKING:
    from models.show import Show


class PremiumPricingStrategy(PricingStrategy):
    BASE_PRICE = 150

    def calculate_price(self, seat_type: SeatType, show: "Show") -> float:
        if seat_type == SeatType.PREMIUM:
            return self.BASE_PRICE * 1.5

        return 0.0
