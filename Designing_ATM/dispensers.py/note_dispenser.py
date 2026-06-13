from patterns.chain_of_responsibility import DispenseChain
from typing import Optional


class NoteDispenser50(DispenseChain):

    def __init__(self, note_value: int, num_of_notes: int):
        self.note_value = note_value
        self.num_of_notes = num_of_notes
        self.next_chain: Optional[DispenseChain] = None

    def set_next_chain(self, next_chain: DispenseChain):
        self.next_chain = next_chain
    
    def dispense(self, amount: int):
        if amount >= self.note_value and self.num_notes > 0:
            notes_needed = min(amount // self.note_value, self.num_notes)
            dispensed_amount = notes_needed * self.note_value
            self.num_notes -= notes_needed
            print(f"Dispensing {notes_needed} notes of ${self.note_value}")
            
            remaining = amount - dispensed_amount
            if remaining > 0 and self.next_chain:
                self.next_chain.dispense(remaining)
        elif self.next_chain:
            self.next_chain.dispense(amount)
        elif amount > 0:
            print(f"Cannot dispense remaining amount: ${amount}")
    
    def can_dispense(self, amount: int) -> bool:
        if amount >= self.note_value and self.num_notes > 0:
            notes_needed = min(amount // self.note_value, self.num_notes)
            remaining = amount - (notes_needed * self.note_value)
            if remaining == 0:
                return True