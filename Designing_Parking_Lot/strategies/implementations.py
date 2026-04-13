from strategies.interfaces import PaymentStrategy, ParkingStrategy
from ticket import ParkingTicket
from floor import ParkingFloor
from spot import ParkingSpot
from vehicles import Vehicle
from typing import List, Optional

class FlatRateStrategy(PaymentStrategy):
    RATE_PER_HOUR = 10

    def caculate_fee(self, ticket: ParkingTicket) -> float:
        return self.RATE_PER_HOUR * ticket.get_duration_in_hours()

class NearestSpotStrategy(ParkingStrategy):
    def find_spot(self, floors: List[ParkingFloor], vehicle: Vehicle) -> Optional[ParkingSpot]:
        for floor in floors:
            for spot in floor.get_spots():
                if spot.can_park_vehicle(vehicle):
                    return spot
        return None