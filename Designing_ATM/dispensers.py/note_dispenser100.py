from dispensers import NoteDispenser

class NoteDispenser100(NoteDispenser):
    def __init__(self, num_of_notes: int):
        super().__init__(100, num_of_notes)

