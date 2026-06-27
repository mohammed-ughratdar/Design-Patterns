from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.enums import OrderStatus
    from models.order import Order


class OrderState(ABC):
    @abstractmethod
    def confirm(self, order: 'Order'):
        pass

    @abstractmethod
    def start_preparing(self, order: 'Order'):
        pass

    @abstractmethod
    def out_for_delivery(self, order: 'Order'):
        pass

    @abstractmethod
    def deliver(self, order: 'Order'):
        pass

    @abstractmethod
    def cancel(self, order: 'Order'):
        pass

    @abstractmethod
    def get_status(self) -> 'OrderStatus':
        pass