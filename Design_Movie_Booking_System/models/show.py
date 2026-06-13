from datetime import datetime
from threading import Lock
from typing import Dict, List, TYPE_CHECKING

from models.enums import SeatStatus
from models.seat import Seat

if TYPE_CHECKING:
    from models.movie import Movie
    from models.screen import Screen


class Show:

    def __init__(self, id: str, movie: "Movie", screen: "Screen", show_time: datetime):
        self.id = id
        self.movie = movie
        self.screen = screen
        self.show_time = show_time
        self.seats_map: Dict[str, Seat] = {}
        self.initialize_seats_map()
        self.lock = Lock()

    def initialize_seats_map(self):
        for row in self.screen.get_seats():
            for seat in row:
                self.seats_map[seat.get_id()] = seat

    def select_seats(self, seat_ids: List[str]):
        with self.lock:
            selected_seats = []
            for seat_id in seat_ids:
                seat = self.seats_map.get(seat_id)
                if seat and seat.reserve():
                    seat.set_reservation_time(datetime.now())
                    selected_seats.append(seat)
                else:
                    for reserved_seat in selected_seats:
                        reserved_seat.release()
                    return []
            return selected_seats

    def find_adjacent_seats(self, seat_count: int):
        seats = self.screen.get_seats()
        for row in seats:
            for i in range(len(row) - seat_count + 1):
                adjacent = []
                all_adjacent = True
                for j in range(seat_count):
                    if row[i + j].get_status() == SeatStatus.AVAILABLE:
                        adjacent.append(row[i + j])
                    else:
                        all_adjacent = False
                        break
                if all_adjacent and len(adjacent) == seat_count:
                    return adjacent
        return []

    def get_id(self):
        return self.id

    def get_movie(self):
        return self.movie

    def get_screen(self):
        return self.screen

    def get_seats_map(self):
        return self.seats_map
