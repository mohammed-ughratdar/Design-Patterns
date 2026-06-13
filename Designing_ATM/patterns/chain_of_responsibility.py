from abc import ABC, abstractmethod

class DispenseChain(ABC):

    @abstractmethod
    def dispense(self, amount: int):
        pass

    @abstractmethod
    def set_next_chain(self, next_chain: DispenseChain):
        pass

    @abstractmethod
    def can_dispense(self, amount: int):
        pass