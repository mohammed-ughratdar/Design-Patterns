from dispensers import NoteDispenser

class NoteDispenser20(NoteDispenser):
    def __init__(self, num_of_notes: int):
        super().__init__(20, num_of_notes)