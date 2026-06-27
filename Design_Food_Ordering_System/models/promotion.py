from threading import Lock

from models.enums import PromotionType


class Promotion:
    def __init__(self, id: str, code: str, promotion_type: PromotionType, value: float, min_order_value: float = 0.0):
        self.id = id
        self.code = code
        self.promotion_type = promotion_type
        self.value = value
        self.min_order_value = min_order_value
        self.is_active = True
        self.lock = Lock()

    def get_id(self):
        return self.id

    def get_code(self):
        return self.code

    def get_promotion_type(self):
        return self.promotion_type

    def get_value(self):
        return self.value

    def get_min_order_value(self):
        return self.min_order_value

    def is_valid(self, order_amount: float)-> bool:
        return self.is_active and order_amount >= self.min_order_value

    def apply_discount(self, order_amount: float)-> float:
        if not self.is_valid(order_amount):
            return 0.0

        if self.promotion_type == PromotionType.PERCENTAGE_DISCOUNT:
            return order_amount * (self.value / 100)
        elif self.promotion_type == PromotionType.FIXED_AMOUNT_DISCOUNT:
            return min(self.value, order_amount)
        return 0.0