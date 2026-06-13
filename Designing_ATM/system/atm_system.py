class ATMSystem:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        
        return cls._instance


    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self.atm_state: ATMState = IdleState()
        self.bank_service: BankService = BankService()
        self.current_card: Optional[Card] = None
        self.cash_dispenser: CashDispenser = CashDispenser()
        self.trasaction_counter: int = 0

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls()
        return cls._instance

    def insert_card(self, card: Card):
        self.atm_state.insert_card(self, card)

    def eject_card(self):
        self.atm_state.eject_card(self)

    def enter_pin(self, pin: int):
        self.atm_state.enter_pin(self, pin)

    def select_operation(self, operation: OperationType, amount: float = None):
        self.atm_state.select_operation(self, operation, amount)

    def set_current_card(self, card: Card):
        self.current_card = card

    def check_balance(self):
        if self.current_card:
            balance = self.bank_service.get_balance(self.current_card)
            print(f"Balance: {balance}")
            self.trasaction_counter += 1
        else:
            print("No card inserted")

    def deposit(self, amount: float):
        if self.current_card:
            self.bank_service.deposit(self.current_card, amount)
            print(f"Deposited {amount} successfully")
            self.trasaction_counter += 1
        else:
            print("No card inserted")

    def withdraw(self, amount: float):
        if not self.current_card:
            print("No card inserted")
            return

            if not self.cash_dispenser.can_dispense_cash(amount):
                print("Cannot dispense cash. Insufficient cash in the dispenser.")
                return
            
            if self.bank_service.withdraw(self.current_card, amount):
                self.cash_dispenser.dispense_cash(amount)
                print(f"Withdrawn {amount} successfully")
                self.trasaction_counter += 1
            else:
                print("Insufficient balance")
        else:
            print("No card inserted")

    def get_bank_service(self):
        return self.bank_service

    def get_transaction_count(self):
        return self.trasaction_counter