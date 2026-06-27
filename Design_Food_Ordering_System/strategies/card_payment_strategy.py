from typing import Dict

from patterns.payment_strategy import PaymentStrategy


class CardPaymentStrategy(PaymentStrategy):
    def process_payment(self, amount: float, payment_details: Dict) -> bool:
        card_number = payment_details.get("card_number")
        cvv = payment_details.get("cvv")
        print(f"Processing payment of {amount} using card")
        return True