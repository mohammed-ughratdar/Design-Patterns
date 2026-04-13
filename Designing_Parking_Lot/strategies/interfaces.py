from abc import abstractmethod
from ticket import ParkingTicket
from typing import List, Optional
from floor import ParkingFloor
from vehicles import Vehicle
from spot import ParkingSpot

class PaymentStrategy:
    @abstractmethod
    def caculate_fee(self, ticket: ParkingTicket) -> float:
        raise NotImplementedError

class ParkingStrategy:
    @abstractmethod
    def find_spot(self, floors: List[ParkingFloor], vehicle: Vehicle) -> Optional[ParkingSpot]:
        raise NotImplementedError