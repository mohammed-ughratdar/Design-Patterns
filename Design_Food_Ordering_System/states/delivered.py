from models.enums import OrderStatus
from patterns.order_state import OrderState


class DeliveredState(OrderState):
    def confirm(self, order: 'Order'):
        print("Order is already delivered.")

    def start_preparing(self, order: 'Order'):
        print("Order is already delivered.")

    def out_for_delivery(self, order: 'Order'):
        print("Order is already delivered.")
        
    def deliver(self, order: 'Order'):
        print("Order is already delivered.")

    def cancel(self, order: 'Order'):
        print("Order is already delivered and cannot be cancelled.")

    def get_status(self) -> 'OrderStatus':
        return OrderStatus.DELIVERED