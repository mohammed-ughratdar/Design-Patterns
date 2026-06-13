class IdleState(ATMState):
    def insert_card(self, atm: ATM, card: Card):
        card = atm.bank_service.get_card(card.get_card_number())
        if card:
            atm.set_current_card(card)
            atm.set_state(CardInsertedState())
            print("Card inserted successfully. Please enter your PIN.")
        else:
            print("Invalid card")

    def enter_pin(self, atm: ATM, pin: int):
        print("Please insert card first")

    def eject_card(self, atm: ATM):
        print("Please insert card first")

    def select_operation(self, atm: ATM, operation: OperationType, amount: int = None):
        print("Please insert card and authenticate first")