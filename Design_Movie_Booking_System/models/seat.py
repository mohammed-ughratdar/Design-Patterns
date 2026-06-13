from datetime import datetime, timedelta
from threading import RLock
from typing import List, Optional, TYPE_CHECKING

from models.enums import SeatStatus, SeatType
from patterns.state import SeatState
from states.available_state import AvailableState

if TYPE_CHECKING:
    from models.show import Show
    from patterns.observer import SeatAvailabilityObserver


class Seat:
    RESERVATION_TIME_MINUTES = 15

    def __init__(self, id: str, row: str, seat_number: int, seat_type: SeatType):
        self.id = id
        self.row = row
        self.seat_number = seat_number
        self.seat_type = seat_type
        self.is_reserved = False
        self.current_state: SeatState = AvailableState()
        self.reservation_time: Optional[datetime] = None
        self.observers: List["SeatAvailabilityObserver"] = []
        self.lock = RLock()

    def get_id(self):
        return self.id

    def get_row(self):
        return self.row

    def get_seat_number(self):
        return self.seat_number

    def get_seat_type(self):
        return self.seat_type

    def reserve(self):
        with self.lock:
            return self.current_state.reserve(self)

    def book(self):
        with self.lock:
            return self.current_state.book(self)

    def release(self):
        with self.lock:
            return self.current_state.release(self)

    def get_status(self):
        with self.lock:
            return self.current_state.get_status()

    def add_observer(self, observer: "SeatAvailabilityObserver"):
        self.observers.append(observer)

    def remove_observer(self, observer: "SeatAvailabilityObserver"):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self, show: "Show"):
        for observer in self.observers:
            observer.on_seat_availability_change(self, show)

    def set_state(self, state: SeatState):
        self.current_state = state

    def set_reservation_time(self, reservation_time: Optional[datetime]):
        self.reservation_time = reservation_time

    def get_reservation_time(self):
        return self.reservation_time

    def get_observers(self):
        return self.observers

    def get_lock(self):
        return self.lock

    def get_current_state(self):
        return self.current_state

    def is_reservation_expired(self):
        if self.reservation_time is None:
            return False
        return datetime.now() - self.reservation_time > timedelta(minutes=self.RESERVATION_TIME_MINUTES)
