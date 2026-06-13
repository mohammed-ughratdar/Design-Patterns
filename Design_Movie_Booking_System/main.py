from datetime import datetime, timedelta

from models.customer import Customer
from models.movie import Movie
from models.screen import Screen
from models.theatre import Theatre
from observers.email_notification_service import EmailNotificationService
from services.booking_service import BookingService


if __name__ == "__main__":

    booking_service = BookingService()

    movie = Movie("1", "Inception", 148)

    theatre = Theatre("1", "Theatre 1", "123 Main St, Anytown, USA")
    screen = Screen("1", 1, 10, 10)
    theatre.add_screen(screen)

    show_time = datetime.now().replace(hour=18, minute=0, second=0, microsecond=0) + timedelta(days=1)

    show = booking_service.create_show(movie, screen, show_time)

    customer = Customer("1", "John Doe", "john.doe@example.com")

    email_service = EmailNotificationService()
    seat_a1 = screen.get_seat("A", 1)
    if seat_a1:
        seat_a1.add_observer(email_service)

    booking_1 = booking_service.create_booking(customer, show, ["A1"])
    if booking_1:
        print(f"Booking 1 created: {booking_1.get_id()}")
    else:
        print("Failed to create booking 1")

    payment = booking_service.process_payment(booking_1)
    print(f"Payment: {payment.get_id()}")
    print(f"Payment status: {payment.get_status()}")
    print(f"Booking status: {booking_1.get_status()}")
