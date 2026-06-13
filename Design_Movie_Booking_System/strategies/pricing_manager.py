from typing import TYPE_CHECKING

from models.enums import SeatType
from strategies.premium_pricing import PremiumPricingStrategy
from strategies.regular_pricing import RegularPricingStrategy
from strategies.vip_pricing import VipPricingStrategy

if TYPE_CHECKING:
    from models.show import Show


class PricingManager:
    def __init__(self):
        self.strategies = {
            SeatType.PREMIUM: PremiumPricingStrategy(),
            SeatType.REGULAR: RegularPricingStrategy(),
            SeatType.VIP: VipPricingStrategy(),
        }

    def calculate_price(self, seat_type: SeatType, show: "Show") -> float:
        strategy = self.strategies.get(seat_type)
        return strategy.calculate_price(seat_type, show) if strategy else 0.0
