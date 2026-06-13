from dispensers import NoteDispenser

class NoteDispenser50(NoteDispenser):
    def __init__(self, num_of_notes: int):
        super().__init__(50, num_of_notes)

