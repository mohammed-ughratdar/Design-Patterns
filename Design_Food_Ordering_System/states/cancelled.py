from models.enums import OrderStatus
from patterns.order_state import OrderState


class CancelledState(OrderState):
    def confirm(self, order: 'Order'):
        print("Order is already cancelled.")

    def start_preparing(self, order: 'Order'):
        print("Order is already cancelled.")

    def out_for_delivery(self, order: 'Order'):
        print("Order is already cancelled.")
        
    def deliver(self, order: 'Order'):
        print("Order is already cancelled.")

    def cancel(self, order: 'Order'):
        print("Order is already cancelled.")

    def get_status(self) -> 'OrderStatus':
        return OrderStatus.CANCELLED