class Movie:

    def __init__(self, id: str, title: str, duration: int):
        self.id = id
        self.title = title
        self.duration = duration

    def get_id(self) -> str:
        return self.id

    def get_title(self) -> str:
        return self.title

    def get_duration(self) -> int:
        return self.duration
