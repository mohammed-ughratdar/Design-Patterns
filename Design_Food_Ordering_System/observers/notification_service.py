from typing import List

from models.order import Order


class NotificationService:
    def __init__(self):
        self.notifications: List[str] = []

    def update(self, order: Order, message: str):
        notification = f"Order {order.get_id()} status changed to {message}"
        self.notifications.append(notification)
        print(notification)

    def get_notifications(self):
        return self.notifications
    