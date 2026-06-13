from typing import Optional, TYPE_CHECKING

from patterns.observer import SeatAvailabilityObserver

if TYPE_CHECKING:
    from models.seat import Seat
    from models.show import Show


class EmailNotificationService(SeatAvailabilityObserver):

    def on_seat_availability_change(self, seat: "Seat", show: Optional["Show"] = None):
        show_id = show.get_id() if show else "unknown"
        print(f"Email notification sent for seat {seat.get_id()} in show {show_id}. Seat is available now.")
