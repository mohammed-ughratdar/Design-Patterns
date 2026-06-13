from threading import Lock

from models.enums import PaymentStatus


class Payment:
    def __init__(self, id: str, amount: float):
        self.id = id
        self.amount = amount
        self.status = PaymentStatus.PENDING
        self.lock = Lock()

    def get_id(self):
        return self.id

    def get_amount(self):
        return self.amount

    def get_status(self):
        return self.status

    def process(self):
        with self.lock:
            self.status = PaymentStatus.PAID
            return True

    def fail(self):
        with self.lock:
            self.status = PaymentStatus.FAILED
