from typing import List

from models.location import Location


class Customer:
    def __init__(self, id: str, name: str, email: str, phone: str, location: Location):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.location = location
        self.orders: List['Order'] = []
        self.ratings: List['Rating'] = []

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email

    def add_order(self, order: 'Order'):
        self.orders.append(order)

    def add_rating(self, rating: 'Rating'):
        self.ratings.append(rating)

    def get_orders(self):
        return self.orders

    def get_ratings(self):
        return self.ratings