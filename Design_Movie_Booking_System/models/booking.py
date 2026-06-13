from datetime import datetime
from threading import Lock
from typing import List, Optional, TYPE_CHECKING

from models.enums import BookingStatus, PaymentStatus

if TYPE_CHECKING:
    from models.customer import Customer
    from models.payment import Payment
    from models.seat import Seat
    from models.show import Show


class Booking:

    def __init__(self, id: str, customer: "Customer", show: "Show", seats: List["Seat"]):
        self.id = id
        self.customer = customer
        self.show = show
        self.seats = seats
        self.status = BookingStatus.PENDING
        self.payment: Optional["Payment"] = None
        self.created_at = datetime.now()
        self.lock = Lock()

    def get_id(self) -> str:
        return self.id

    def get_seats(self) -> List["Seat"]:
        return self.seats

    def get_status(self) -> BookingStatus:
        return self.status

    def confirm(self) -> bool:
        with self.lock:
            if self.status == BookingStatus.PENDING and self.payment and self.payment.get_status() == PaymentStatus.PAID:
                for seat in self.seats:
                    seat.book()
                self.status = BookingStatus.CONFIRMED
                return True
            return False

    def cancel(self) -> bool:
        with self.lock:
            if self.status in (BookingStatus.PENDING, BookingStatus.CONFIRMED):
                self.status = BookingStatus.CANCELLED
                for seat in self.seats:
                    seat.release()
                    seat.notify_observers(self.show)
                return True
            return False

    def set_payment(self, payment: "Payment"):
        self.payment = payment

    def get_show(self) -> "Show":
        return self.show

    def get_customer(self) -> "Customer":
        return self.customer
