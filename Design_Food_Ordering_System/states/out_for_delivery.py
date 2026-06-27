from models.enums import OrderStatus
from patterns.order_state import OrderState
from states.delivered import DeliveredState


class OutForDeliveryState(OrderState):
    def confirm(self, order: 'Order'):
        print("Order is already confirmed and out for delivery.")

    def start_preparing(self, order: 'Order'):
        print("Order is already preparing and out for delivery.")

    def out_for_delivery(self, order: 'Order'):
        print("Order is already out for delivery.")

    def deliver(self, order: 'Order'):
        order.set_state(DeliveredState())
        order.notify_observers(f"Order {order.get_id()} delivered")

    def cancel(self, order: 'Order'):
        print("Order is already out for delivery and cannot be cancelled.")

    def get_status(self) -> 'OrderStatus':
        return OrderStatus.OUT_FOR_DELIVERY
        
        