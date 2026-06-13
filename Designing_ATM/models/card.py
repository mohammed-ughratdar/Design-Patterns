

class Card:
    def __init__(self, card_number: int, pin: int):
        self.card_number = card_number
        self.pin = pin

    def get_card_number(self) -> int:
        return self.card_number

    def get_pin(self) -> int:
        return self.pin