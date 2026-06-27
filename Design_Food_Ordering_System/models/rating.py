from datetime import datetime
from threading import Lock
from typing import Optional

from models.customer import Customer


class Rating:
    def __init__(self, id: str, customer: Customer, rating: int, comment: Optional[str] = None):
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")
        self.id = id
        self.customer = customer
        self.rating = rating
        self.comment = comment
        self.created_at = datetime.now()

    def get_id(self):
        return self.id

    def get_customer(self):
        return self.customer

    def get_rating(self):
        return self.rating
        
    def get_comment(self):
        return self.comment
