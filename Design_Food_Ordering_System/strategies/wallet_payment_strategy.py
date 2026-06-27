from typing import Dict

from patterns.payment_strategy import PaymentStrategy


class WalletPaymentStrategy(PaymentStrategy):
    def process_payment(self, amount: float, payment_details: Dict) -> bool:
        wallet_number = payment_details.get("wallet_number")
        pin = payment_details.get("pin")
        print(f"Processing payment of {amount} using wallet")
        return True