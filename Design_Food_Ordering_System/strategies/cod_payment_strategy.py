from typing import Dict

from patterns.payment_strategy import PaymentStrategy


class CODPaymentStrategy(PaymentStrategy):
    def process_payment(self, amount: float, payment_details: Dict) -> bool:
        print(f"Processing payment of {amount} using COD")
        return True