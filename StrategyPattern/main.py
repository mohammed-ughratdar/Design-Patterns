from PassengerVehicle import PassengerVehicle
from OffRoadVehicle import OffRoadVehicle

def main():
    passenger_vehicle = PassengerVehicle()
    off_road_vehicle = OffRoadVehicle()
    passenger_vehicle.drive()
    off_road_vehicle.drive()

if __name__ == "__main__":
    main()