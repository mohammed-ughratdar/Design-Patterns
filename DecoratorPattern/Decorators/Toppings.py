from abc import abstractmethod, ABC
from BasePizza import BasePizza

# Abstract class for toppings
class Toppings(BasePizza, ABC):

    def __init__(self, base_pizza: BasePizza):
        self.base_pizza = base_pizza

    @abstractmethod
    def get_cost(self):
        pass