from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.screen import Screen


class Theatre:

    def __init__(self, id: str, name: str, location: str):
        self.id = id
        self.name = name
        self.location = location
        self.screens: list["Screen"] = []

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_location(self):
        return self.location

    def add_screen(self, screen: "Screen"):
        self.screens.append(screen)

    def get_screens(self):
        return self.screens
