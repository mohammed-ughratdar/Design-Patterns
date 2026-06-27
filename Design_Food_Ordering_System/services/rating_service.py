import uuid
from threading import Lock
from typing import Dict, Optional

from models.customer import Customer
from models.delivery_agent import DeliveryAgent
from models.rating import Rating
from models.restaurant import Restaurant


class RatingService:
    def __init__(self):
        self.ratings: Dict[str, Rating] = {}
        self.lock = Lock()

    def rate_restaurant(self, customer: Customer, restaurant: Restaurant, rating: int, comment: Optional[str] = None):
        rating_object = Rating(str(uuid.uuid4()), customer, rating, comment)

        with self.lock:
            self.ratings[rating_object.get_id()] = rating_object
        
        restaurant.add_rating(rating_object)
        customer.add_rating(rating_object)
        return rating_object

    def rate_delivery_agent(self, customer: Customer, delivery_agent: DeliveryAgent, rating: int, comment: Optional[str] = None):
        rating_object = Rating(str(uuid.uuid4()), customer, rating, comment)

        with self.lock:
            self.ratings[rating_object.get_id()] = rating_object
        
        delivery_agent.add_rating(rating_object)
        customer.add_rating(rating_object)
        return rating_object
       