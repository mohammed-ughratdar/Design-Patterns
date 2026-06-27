from threading import Lock
from typing import Dict

from models.enums import PaymentMethod, PaymentStatus
from patterns.payment_strategy import PaymentStrategy


class Payment:
    def __init__(self, id: str, amount: float, payment_method: PaymentMethod, payment_strategy: PaymentStrategy):
        self.id = id
        self.amount = amount
        self.payment_method = payment_method
        self.payment_strategy = payment_strategy
        self.status = PaymentStatus.PENDING
        self.payment_details: Dict = {}
        self.lock = Lock()

    def get_id(self):
        return self.id

    def get_amount(self):
        return self.amount
    
    def get_payment_method(self):
        return self.payment_method

    def get_payment_strategy(self):
        return self.payment_strategy

    def get_status(self):
        return self.status

    def get_payment_details(self):
        return self.payment_details

    def set_payment_details(self, payment_details: Dict):
        with self.lock:
            self.payment_details = payment_details

    def process(self):
        with self.lock:
            self.status = PaymentStatus.PROCESSING
            success = self.payment_strategy.process_payment(self.amount, self.payment_details)
            self.status = PaymentStatus.SUCCESS if success else PaymentStatus.FAILED
            return success
    