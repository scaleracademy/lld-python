from typing import List
from parking_lot.models import Vehicle


class VehicleRepository:
    def __init__(self):
        self.vehicles: List[Vehicle] = []

    def get_vehicle(self, vehicle_number: str) -> Vehicle:
        for vehicle in self.vehicles:
            if vehicle.license_number == vehicle_number:
                return vehicle
        return None

    def create_vehicle(self, vehicle: Vehicle) -> Vehicle:
        self.vehicles.append(vehicle)
        return vehicle
