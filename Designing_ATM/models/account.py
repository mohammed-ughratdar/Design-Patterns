from typing import Dict
from models.card import Card

class Account:
    def __init__(self, account_number: int, initial_balance: float):
        self.account_number = account_number
        self.balance = initial_balance
        self.cards: Dict[int, Card] = {}

    def get_balance(self) -> float:
        return self.balance

    def get_account_number(self) -> int:
        return self.account_number

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> bool:
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

    def add_card(self, card_number: int, card: Card) -> None:
        self.cards[card_number] = card

    def remove_card(self, card_number: int) -> None:
        del self.cards[card_number]

