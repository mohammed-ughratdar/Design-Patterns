from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from models.booking import Booking


class Customer:

    def __init__(self, id: str, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email
        self.bookings: List["Booking"] = []

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_bookings(self):
        return self.bookings

    def add_booking(self, booking: "Booking"):
        self.bookings.append(booking)
