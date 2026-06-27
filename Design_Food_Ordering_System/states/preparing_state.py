from models.enums import OrderStatus
from patterns.order_state import OrderState
from states.cancelled import CancelledState
from states.out_for_delivery import OutForDeliveryState


class PreparingState(OrderState):
    def confirm(self, order: 'Order'):
        print("Order must be confirmed before starting preparation")

    def start_preparing(self, order: 'Order'):
        print("Order is already preparing")

    def out_for_delivery(self, order: 'Order'):
        order.set_state(OutForDeliveryState())
        order.notify_observers(f"Order {order.get_id()} is out for delivery")

    def deliver(self, order: 'Order'):
        print("Order must be out for delivery before being delivered")

    def cancel(self, order: 'Order'):
        order.set_state(CancelledState())
        order.notify_observers(f"Order {order.get_id()} cancelled")

    def get_status(self) -> 'OrderStatus':
        return OrderStatus.PREPARING