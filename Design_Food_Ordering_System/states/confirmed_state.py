from models.enums import OrderStatus
from patterns.order_state import OrderState
from states.cancelled import CancelledState
from states.preparing_state import PreparingState


class ConfirmedState(OrderState):
    def confirm(self, order: 'Order'):
        print("Order is already confirmed")

    def start_preparing(self, order: 'Order'):
        order.set_state(PreparingState())
        order.notify_observers(f"Order {order.get_id()} started preparing")

    def out_for_delivery(self, order: 'Order'):
        print("Order must be prepared before being out for delivery")

    def deliver(self, order: 'Order'):
        print("Order must be prepared before being delivered")

    def cancel(self, order: 'Order'):
        order.set_state(CancelledState())
        order.notify_observers(f"Order {order.get_id()} cancelled")

    def get_status(self) -> 'OrderStatus':
        return OrderStatus.CONFIRMED