from typing import List

from models.enums import SeatType
from models.seat import Seat


class Screen:
    def __init__(self, id: str, screen_number: int, rows: int, seats_per_row: int):
        self.id = id
        self.screen_number = screen_number
        self.rows = rows
        self.seats: List[List[Seat]] = []
        self.initialize_seats(rows, seats_per_row)

    def initialize_seats(self, rows: int, seats_per_row: int):
        row_char = ord("A")
        for i in range(rows):
            row_seats = []
            for j in range(seats_per_row):
                seat_type = self.determine_seat_type(i, rows)
                seat_id = chr(row_char) + str(j + 1)
                row_seats.append(Seat(seat_id, chr(row_char), j + 1, seat_type))
            self.seats.append(row_seats)
            row_char += 1

    def determine_seat_type(self, row: int, total_rows: int):
        ratio = row / total_rows
        if ratio < 0.2:
            return SeatType.VIP
        elif ratio < 0.5:
            return SeatType.PREMIUM
        else:
            return SeatType.REGULAR

    def get_id(self):
        return self.id

    def get_screen_number(self):
        return self.screen_number

    def get_seats(self):
        return self.seats

    def get_seat(self, row: str, seat_number: int):
        row_index = ord(row) - ord("A")
        if 0 <= row_index < len(self.seats) and 1 <= seat_number <= len(self.seats[row_index]):
            return self.seats[row_index][seat_number - 1]
        return None
