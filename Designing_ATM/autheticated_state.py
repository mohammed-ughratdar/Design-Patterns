class AutheticatedState(ATMState):
    def insert_card(self, atm: ATM, card: Card):
        print("Card already inserted")

    def eject_card(self, atm: ATM):
        atm.set_current_card(None)
        atm.set_state(IdleState())
        print("Card ejected successfully. Thank you for using the ATM.")

    def enter_pin(self, atm: ATM, pin: int):
        print("Pin already entered")

    def select_operation(self, atm: ATM, operation: OperationType, amount: float = None):
        if operation == OperationType.CHECK_BALANCE:
            atm.check_balance()
        elif op == OperationType.WITHDRAW_CASH:
            atm.withdraw_cash(amount)
        elif op == OperationType.DEPOSIT_CASH:
            atm.deposit_cash(amount)
        else:
            print("Invalid operation")