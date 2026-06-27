from datetime import datetime
from threading import Lock
from typing import Dict, List, Optional

from models.customer import Customer
from models.delivery_agent import DeliveryAgent
from models.enums import OrderStatus, PromotionType
from models.order_item import OrderItem
from models.payment import Payment
from models.promotion import Promotion
from models.restaurant import Restaurant
from patterns.order_observer import OrderObserver
from patterns.order_state import OrderState
from states.placed_state import PlacedState


from models.location import Location


class Order:
    def __init__(self, id: str, customer: Customer, restaurant: Restaurant, items: List[OrderItem], delivery_address: Location):
        self.id = id
        self.customer = customer
        self.restaurant = restaurant
        self.items = items
        self.delivery_address = delivery_address
        self.current_state: OrderState = PlacedState()
        self.created_at = datetime.now()
        self.observers: List['OrderObserver'] = []
        self.payment: Optional['Payment'] = None
        self.promotion: Optional['Promotion'] = None
        self.delivery_agent: Optional[DeliveryAgent] = None
        self.lock = Lock()

    def get_id(self):
        return self.id

    def get_customer(self):
        return self.customer

    def get_restaurant(self):
        return self.restaurant

    def get_items(self):
        return self.items

    def get_delivery_address(self):
        return self.delivery_address
        
    def get_status(self):
        return self.current_state.get_status()

    def get_observers(self):
        return self.observers

    def get_payment(self):
        return self.payment

    def get_promotion(self):
        return self.promotion

    def get_delivery_agent(self):
        return self.delivery_agent

    def set_payment(self, payment: Payment):
        with self.lock:
            self.payment = payment

    def set_promotion(self, promotion: Promotion):
        with self.lock:
            self.promotion = promotion

    def set_delivery_agent(self, delivery_agent: DeliveryAgent):
        with self.lock:
            self.delivery_agent = delivery_agent

    def calculate_subtotal(self):
        return sum(item.get_subtotal() for item in self.items)

    def calculate_delivery_charge(self)-> float:
        if self.promotion and self.promotion.get_promotion_type() == PromotionType.FREE_DELIVERY:
            return 0.0
        
        distance = self.restaurant.get_location().distance_to(self.delivery_address)

        return max(20.0, distance * 0.5)

    
    def calculate_discount(self)-> float:
        if self.promotion:
            return self.promotion.apply_discount(self.calculate_subtotal())
        return 0.0

    def calculate_total(self)-> float:
        subtotal = self.calculate_subtotal()
        delivery_charge = self.calculate_delivery_charge()
        discount = self.calculate_discount()
        return subtotal + delivery_charge - discount

    def add_observer(self, observer: 'OrderObserver'):
        with self.lock:
            self.observers.append(observer)

    def remove_observer(self, observer: 'OrderObserver'):
        with self.lock:
            if observer in self.observers:
                self.observers.remove(observer)
    
    def notify_observers(self, message: str):
        with self.lock:
            for observer in self.observers:
                observer.update(self, message)

    def set_state(self, state: OrderState):
        with self.lock:
            self.current_state = state
            
    def confirm(self):
        self.current_state.confirm(self)

    def start_preparing(self):
        self.current_state.start_preparing(self)

    def out_for_delivery(self):
        self.current_state.out_for_delivery(self)

    def deliver(self):
        self.current_state.deliver(self)

    def cancel(self):
        self.current_state.cancel(self)

        