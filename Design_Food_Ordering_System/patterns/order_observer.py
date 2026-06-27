from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.order import Order


class OrderObserver(ABC):
    @abstractmethod
    def update(self, order: 'Order', message: str):
        pass