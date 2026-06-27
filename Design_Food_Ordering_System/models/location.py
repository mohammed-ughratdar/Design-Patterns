import math


class Location:
    def __init__(self, latitude: float, longitude: float, address: str):
        self.latitude = latitude
        self.longitude = longitude
        self.address = address

    def get_latitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longitude

    def get_address(self):
        return self.address

    def distance_to(self, other: 'Location') -> float:
        return math.sqrt((self.latitude - other.latitude) ** 2 + (self.longitude - other.longitude) ** 2)