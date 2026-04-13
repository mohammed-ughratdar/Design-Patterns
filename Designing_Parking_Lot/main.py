import time
from parking_lot import ParkingLot
from floor import ParkingFloor
from spot import ParkingSpot
from vehicles import VehicleFactory, VehicleSize


def main():

    parking_lot = ParkingLot.get_instance()

    floor1 = ParkingFloor(1)
    floor2 = ParkingFloor(2)

    floor1.add_spot(ParkingSpot("1-A", VehicleSize.SMALL))
    floor1.add_spot(ParkingSpot("1-B", VehicleSize.MEDIUM))
    floor1.add_spot(ParkingSpot("1-C", VehicleSize.LARGE))
    floor2.add_spot(ParkingSpot("2-A", VehicleSize.SMALL))
    floor2.add_spot(ParkingSpot("2-B", VehicleSize.MEDIUM))
    floor2.add_spot(ParkingSpot("2-C", VehicleSize.LARGE))

    parking_lot.add_floor(floor1)
    parking_lot.add_floor(floor2)

    car_1 = VehicleFactory.create_vehicle("1234567890", VehicleSize.MEDIUM)
    car_2 = VehicleFactory.create_vehicle("1234567891", VehicleSize.MEDIUM)
    bike_1 = VehicleFactory.create_vehicle("1234567892", VehicleSize.SMALL)
    truck_1 = VehicleFactory.create_vehicle("1234567893", VehicleSize.LARGE)

    ticket_car_1 = parking_lot.park_vehicle(car_1)
    parking_lot.park_vehicle(car_2)
    parking_lot.park_vehicle(bike_1)
    ticket_truck_1 = parking_lot.park_vehicle(truck_1)

    time.sleep(5)

    print(f"Active tickets: {len(parking_lot.get_active_tickets())}")
    print(f"Spots on floor 1: {floor1.get_spots()}")
    print(f"Spots on floor 2: {floor2.get_spots()}")
    parking_lot.unpark_vehicle(ticket_car_1)
    parking_lot.unpark_vehicle(ticket_truck_1)
    print(f"Active tickets: {len(parking_lot.get_active_tickets())}")
    print(f"Spots on floor 1: {floor1.get_spots()}")
    print(f"Spots on floor 2: {floor2.get_spots()}")

if __name__ == "__main__":
    main()