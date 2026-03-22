from abc import abstractmethod, ABC

# Abstract class for base pizza
class BasePizza(ABC):

    @abstractmethod
    def get_cost(self):
        pass