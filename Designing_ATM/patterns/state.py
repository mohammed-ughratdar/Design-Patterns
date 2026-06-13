from abc import ABC, abstractmethod
from models.enums import OperationType
from models.atm import ATM

class ATMState(ABC):
    @abstractmethod
    def insert_card(self, atm: ATM, card: Card):
        pass

    @abstractmethod
    def eject_card(self, atm: ATM):
        pass

    @abstractmethod
    def enter_pin(self, atm: ATM, pin: int):
        pass

    @abstractmethod
    def select_operation(self, atm: ATM, operation: OperationType, amount: float = None):
        pass
