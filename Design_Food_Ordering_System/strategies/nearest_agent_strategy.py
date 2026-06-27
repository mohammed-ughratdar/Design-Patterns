from typing import List, Optional

from models.delivery_agent import DeliveryAgent
from models.order import Order
from patterns.delivery_assignment_strategy import DeliveryAssignmentStrategy


class NearestAgentStrategy(DeliveryAssignmentStrategy):
    def assign_agent(self, order: Order, agents: List[DeliveryAgent]) -> Optional[DeliveryAgent]:
        available_agents = [agent for agent in agents if agent.is_available]
        if not available_agents:
            return None
        
        restaurant_location = order.get_restaurant().get_location()
        nearest_agent = min(available_agents, key= lambda agent: restaurant_location.distance_to(agent.get_location()))
        return nearest_agent