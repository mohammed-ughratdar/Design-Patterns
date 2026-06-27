from threading import Lock
from typing import Dict, List

from models.location import Location
from models.menu_item import MenuItem
from models.rating import Rating


class Restaurant:
    def __init__(self, id: str, name: str, cuisine: str, location: Location):
        self.id = id
        self.name = name
        self.cuisine = cuisine
        self.location = location
        self.menu_items: Dict[str, MenuItem] = {}
        self.ratings: List[Rating] = []
        self.is_open = True
        self.lock = Lock()

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_cuisine(self):
        return self.cuisine

    def get_location(self):
        return self.location

    def add_menu_item(self, menu_item: MenuItem):
        with self.lock:
            self.menu_items[menu_item.get_id()] = menu_item

    def get_menu_item(self, item_id: str):
        with self.lock:
            return self.menu_items.get(item_id)

    def get_menu_items(self):
        with self.lock:
            return list(self.menu_items.values())

    def add_rating(self, rating: Rating):
        with self.lock:
            self.ratings.append(rating)

    def get_average_rating(self):
        with self.lock:
            return sum(rating.get_rating() for rating in self.ratings) / len(self.ratings) if self.ratings else 0

    def is_available(self):
        return self.is_open

    def set_availability(self, is_open: bool):
        with self.lock:
            self.is_open = is_open
