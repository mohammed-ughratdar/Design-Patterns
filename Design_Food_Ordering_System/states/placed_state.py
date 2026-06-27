from models.enums import OrderStatus
from patterns.order_state import OrderState
from states.cancelled import CancelledState
from states.confirmed_state import ConfirmedState


class PlacedState(OrderState):
    def confirm(self, order: 'Order'):
        order.set_state(ConfirmedState())
        order.notify_observers(f"Order {order.get_id()} confirmed")

    def start_preparing(self, order: 'Order'):
        print("Order must be confirme before starting preparation")

    def out_for_delivery(self, order: 'Order'):
        print("Order must be prepared before being out for delivery")

    def deliver(self, order: 'Order'):
        print("Order must be prepared before being delivered")

    def cancel(self, order: 'Order'):
        order.set_state(CancelledState())
        order.notify_observers(f"Order {order.get_id()} cancelled")

    def get_status(self) -> 'OrderStatus':
        return OrderStatus.PLACED