import datetime
import uuid
from typing import List, Dict
from floor import ParkingFloor
from spot import ParkingSpot
from ticket import ParkingTicket
from strategies.interfaces import PaymentStrategy, ParkingStrategy
from strategies.implementations import FlatRateStrategy, NearestSpotStrategy
from vehicles import Vehicle
from threading import Lock
class ParkingLot:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        
        return cls._instance


    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self.floors: List[ParkingFloor] = []
        self.active_tickets: Dict[str, ParkingTicket] = {}
        self.payment_strategy: PaymentStrategy = FlatRateStrategy()
        self.parking_strategy: ParkingStrategy = NearestSpotStrategy()
        self._lock = Lock()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls()
        return cls._instance

    def add_floor(self, floor: ParkingFloor):
        self.floors.append(floor)

    def remove_floor(self, floor: ParkingFloor):
        self.floors.remove(floor)

    def get_floors(self):
        return self.floors

    def park_vehicle(self, vehicle: Vehicle):
        with self._lock:
            spot = self.parking_strategy.find_spot(self.floors, vehicle)

            if spot:
                spot.park_vehicle(vehicle)
        ticket = ParkingTicket(str(uuid.uuid4()), vehicle, spot)
        self.active_tickets[ticket.get_ticket_id()] = ticket

        print(f"Vehicle {vehicle.get_license_number()} parked successfully at spot {spot.get_spot_id()}")
        return ticket
    

    def unpark_vehicle(self, ticket: ParkingTicket):
        if ticket.get_ticket_id() in self.active_tickets:
            spot = ticket.get_spot()
            ticket.set_exit_time(datetime.datetime.now())
            fee = self.payment_strategy.caculate_fee(ticket)
            spot.unpark_vehicle()

            print(f"Vehicle {ticket.get_vehicle().get_license_number()} unparked successfully with fee {fee}")
            self.active_tickets.pop(ticket.get_ticket_id())
            return True
        
        print(f"Ticket {ticket.get_ticket_id()} not found or already unparked")
        return False

    def get_active_tickets(self):
        return self.active_tickets

    def set_payment_strategy(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy

    def set_parking_strategy(self, parking_strategy: ParkingStrategy):
        self.parking_strategy = parking_strategy