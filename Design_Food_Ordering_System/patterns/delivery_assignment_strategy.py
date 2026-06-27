from abc import ABC, abstractmethod
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from models.delivery_agent import DeliveryAgent
    from models.order import Order


class DeliveryAssignmentStrategy(ABC):
    @abstractmethod
    def assign_agent(self, order: 'Order', agents: List['DeliveryAgent']) -> Optional['DeliveryAgent']:
        pass