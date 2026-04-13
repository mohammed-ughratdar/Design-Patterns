from datetime import datetime
from typing import Optional

from vehicles import Vehicle
from spot import ParkingSpot

class ParkingTicket:
    def __init__(self, ticket_id: str, vehicle: Vehicle, spot: ParkingSpot):
        self.ticket_id = ticket_id
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = datetime.now()
        self.exit_time: Optional[datetime] = None

    def get_ticket_id(self):
        return self.ticket_id

    def get_vehicle(self):
        return self.vehicle

    def get_spot(self):
        return self.spot

    def set_exit_time(self, exit_time: datetime):
        self.exit_time = exit_time

    def get_duration_in_hours(self) -> float:
        if self.exit_time is None:
            return 0.0
        delta = self.exit_time - self.entry_time
        return delta.total_seconds() / 3600.0
    