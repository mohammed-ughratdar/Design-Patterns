import threading
import time
import uuid
from typing import Dict, List, Optional

from models.booking import Booking
from models.customer import Customer
from models.enums import SeatStatus
from models.payment import Payment
from models.show import Show
from strategies.pricing_manager import PricingManager


class BookingService:

    def __init__(self):
        self.bookings: Dict[str, Booking] = {}
        self.shows: Dict[str, Show] = {}
        self.pricing_manager = PricingManager()
        self.start_reservation_expiration_check()

    def start_reservation_expiration_check(self):
        def check_expiration():
            while True:
                time.sleep(60)
                self.check_and_expire_reservations()

        thread = threading.Thread(target=check_expiration, daemon=True)
        thread.start()

    def check_and_expire_reservations(self):
        for show in self.shows.values():
            for seat in show.get_seats_map().values():
                if seat.get_status() == SeatStatus.RESERVED and seat.is_reservation_expired():
                    seat.release()
                    seat.notify_observers(show)

    def create_show(self, movie, screen, show_time) -> Show:
        show_id = str(uuid.uuid4())
        show = Show(show_id, movie, screen, show_time)
        self.shows[show_id] = show
        return show

    def create_booking(self, customer: Customer, show: Show, seat_ids: List[str]) -> Optional[Booking]:
        selected_seats = show.select_seats(seat_ids)
        if not selected_seats:
            return None

        book_id = str(uuid.uuid4())
        booking = Booking(book_id, customer, show, selected_seats)
        self.bookings[booking.get_id()] = booking
        customer.add_booking(booking)
        return booking

    def create_booking_with_adjacent_seats(self, customer: Customer, show: Show, seat_count: int) -> Optional[Booking]:
        adjacent_seats = show.find_adjacent_seats(seat_count)
        if not adjacent_seats:
            return None

        seat_ids = [seat.get_id() for seat in adjacent_seats]
        return self.create_booking(customer, show, seat_ids)

    def process_payment(self, booking: Booking) -> Payment:
        total_price = 0.0

        for seat in booking.get_seats():
            total_price += self.pricing_manager.calculate_price(seat.get_seat_type(), booking.get_show())

        payment_id = str(uuid.uuid4())
        payment = Payment(payment_id, total_price)
        booking.set_payment(payment)

        if payment.process():
            booking.confirm()
        else:
            payment.fail()

        return payment

    def cancel_booking(self, booking_id: str):
        booking = self.get_booking(booking_id)
        if booking:
            booking.cancel()
            return True
        return False

    def get_booking(self, booking_id: str) -> Optional[Booking]:
        return self.bookings.get(booking_id)

    def get_show(self, show_id: str) -> Optional[Show]:
        return self.shows.get(show_id)

    def get_shows_by_movie(self, movie_id: str) -> List[Show]:
        return [show for show in self.shows.values() if show.get_movie().get_id() == movie_id]
