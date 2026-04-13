from typing import Optional
from vehicles import Vehicle
from enums import VehicleSize

class ParkingSpot:

    def __init__(self, spot_id: str, spot_size: VehicleSize):
        self.spot_id = spot_id
        self.spot_size = spot_size
        self._occupied = False
        self.vehicle: Optional[Vehicle] = None

    def get_spot_id(self):
        return self.spot_id

    def get_spot_size(self):
        return self.spot_size

    def park_vehicle(self, vehicle: Vehicle):
        self._occupied = True
        self.vehicle = vehicle

    def can_park_vehicle(self, vehicle: Vehicle) -> bool:
        size_order = {
            VehicleSize.SMALL: 0,
            VehicleSize.MEDIUM: 1,
            VehicleSize.LARGE: 2
        }
        return not self._occupied and size_order[self.spot_size] >= size_order[vehicle.get_size()]

    def unpark_vehicle(self):
        self._occupied = False
        self.vehicle = None

    def is_occupied(self) -> bool:
        return self._occupied

    def get_vehicle(self):
        return self.vehicle
