from abc import ABC, abstractmethod
from typing import Dict


class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self, amount: float, payment_details: Dict) -> bool:
        pass