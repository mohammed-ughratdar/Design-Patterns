class CardInsertedState(ATMState):
    def insert_card(self, atm: ATM, card: Card):
        print("Card already inserted")

    def eject_card(self, atm: ATM):
        atm.set_current_card(None)
        atm.set_state(IdleState())
        print("Card ejected successfully")

    def enter_pin(self, atm: ATM, pin: int):
        if atm.authenticate_card(pin):
            atm.set_state(AutheticatedState())
            print("Authentication successful. Please select an operation.")
        else:
            print("Invalid PIN")

    def select_operation(self, atm: ATM, operation: OperationType, amount: float = None):
        print("Please enter PIN first")