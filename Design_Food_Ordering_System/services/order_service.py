import uuid
from threading import Lock
from typing import Dict, List

from models.customer import Customer
from models.delivery_agent import DeliveryAgent
from models.enums import OrderStatus, PaymentMethod
from models.location import Location
from models.order import Order
from models.order_item import OrderItem
from models.payment import Payment
from models.promotion import Promotion
from models.restaurant import Restaurant
from patterns.delivery_assignment_strategy import DeliveryAssignmentStrategy
from strategies.card_payment_strategy import CardPaymentStrategy
from strategies.cod_payment_strategy import CODPaymentStrategy
from strategies.least_busy_strategy import LeastBusyStrategy
from strategies.wallet_payment_strategy import WalletPaymentStrategy


class OrderService:
    def __init__(self):
        self.orders: Dict[str, Order] = {}
        self.delivery_agent_strategy: DeliveryAssignmentStrategy = LeastBusyStrategy()
        self.lock = Lock()

    def create_order(self, customer: Customer, restaurant: Restaurant, items: List[OrderItem], delivery_location: Location) -> Order:

        for item in items:
            menu_item = restaurant.get_menu_item(item.get_menu_item().get_id())
            if not menu_item or not menu_item.is_item_available():
                raise ValueError(f"Menu item {item.get_menu_item().get_id()} is not available")

        order_id = str(uuid.uuid4())
        order = Order(order_id, customer, restaurant, items, delivery_location)
        with self.lock:
            self.orders[order_id] = order

        customer.add_order(order)
        return order

    def apply_promotion(self, order: Order, promotion: Promotion):
        if promotion.is_valid(order.calculate_subtotal()):
            order.set_promotion(promotion)
            return True
        return False

    def process_payment(self, order: Order, payment_method: PaymentMethod, payment_details: Dict):
        amount = order.calculate_total()

        if payment_method == PaymentMethod.CREDIT_CARD:
            strategy = CardPaymentStrategy()
        elif payment_method == PaymentMethod.DEBIT_CARD:
            strategy = CardPaymentStrategy()
        elif payment_method == PaymentMethod.DIGITAL_WALLET:
            strategy = WalletPaymentStrategy()
        elif payment_method == PaymentMethod.CASH_ON_DELIVERY:
            strategy = CODPaymentStrategy()
        else:
            raise ValueError(f"Invalid payment method: {payment_method}")

        payment = Payment(str(uuid.uuid4()), amount, payment_method, strategy)
        payment.set_payment_details(payment_details)

        if payment.process():
            order.set_payment(payment)
            return payment
        else:
            return None

    def assign_delivery_agent(self, order: Order, agents: List[DeliveryAgent]):
        agent = self.delivery_agent_strategy.assign_agent(order, agents)
        if agent and agent.assign_order(order):
            order.set_delivery_agent(agent)
            return True
        return False

    def update_order_status(self, order: Order, status: OrderStatus):
        stored_order = self.orders.get(order.get_id())
        if not stored_order:
            raise ValueError(f"Order {order.get_id()} not found")

        order = stored_order

        if status == OrderStatus.CONFIRMED:
            order.confirm()
        elif status == OrderStatus.PREPARING:
            order.start_preparing()
        elif status == OrderStatus.OUT_FOR_DELIVERY:
            order.out_for_delivery()
        elif status == OrderStatus.DELIVERED:
            order.deliver()
            if order.get_delivery_agent():
                order.get_delivery_agent().complete_order()
        elif status == OrderStatus.CANCELLED:
            order.cancel()
        else:
            raise ValueError(f"Invalid status: {status}")

    def get_order(self, order_id: str) -> Order:
        return self.orders.get(order_id)

    def set_delivery_agent_strategy(self, strategy: DeliveryAssignmentStrategy):
        self.delivery_agent_strategy = strategy
        