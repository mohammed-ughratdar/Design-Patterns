from threading import Lock
from typing import List, Optional

from models.location import Location


class DeliveryAgent:
    def __init__(self, id: str, name: str, phone: str, location: Location):
        self.id = id
        self.name = name
        self.phone = phone
        self.location = location
        self.orders: List['Order'] = []
        self.current_order: Optional['Order'] = None
        self.is_available = True
        self.ratings: List['Rating'] = []
        self.lock = Lock()

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_phone(self):
        return self.phone

    def get_location(self):
        return self.location

    def get_orders(self):
        return self.orders

    def get_current_order(self):
        return self.current_order

    def get_ratings(self):
        return self.ratings

    def set_location(self, location: Location):
        with self.lock:
            self.location = location

    def set_current_order(self, order: 'Order'):
        with self.lock:
            self.current_order = order

    def assign_order(self, order: 'Order'):
        with self.lock:
            if self.is_available and self.current_order is None:
                self.current_order = order
                self.is_available = False
                return True
            return False

    def complete_order(self):
        with self.lock:
            if self.current_order is not None:
                self.current_order = None
                self.is_available = True
           
    def add_rating(self, rating: 'Rating'):
        with self.lock:
            self.ratings.append(rating)

    def get_average_rating(self):
        with self.lock:
            return sum(rating.get_rating() for rating in self.ratings) / len(self.ratings) if self.ratings else 0

  