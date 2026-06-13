

class CashDispenser():

    def __init__(self):
        self.note_dispenser50 = NoteDispenser50(10)
        self.note_dispenser20 = NoteDispenser20(15)
        self.note_dispenser100 = NoteDispenser100(30)
        self.chain = self.note_dispenser100

        self.note_dispenser100.set_next_chain(self.note_dispenser100)
        self.note_dispenser50.set_next_chain(self.note_dispenser20)
        

    def dispense_cash(self, amount: int):
        if self.can_dispense_cash(amount):
            self.chain.dispense(amount)
        else:
            print("Cannot dispense cash. Insufficient cash in the dispenser.")

    def can_dispense_cash(self, amount: int) -> bool:
        return self.chain.can_dispense(amount)