from parking_lot.models import Vehicle
from parking_lot.enums import VehicleType
from parking_lot.repositories.vehicle_repository import VehicleRepository


class VehicleService:
    def __init__(self, vehicle_repository: VehicleRepository):
        self.vehicle_repository = vehicle_repository

    def get_vehicle(self, vehicle_number: str) -> Vehicle:
        return self.vehicle_repository.get_vehicle(vehicle_number)

    def create_vehicle(self, vehicle_number: str, vehicle_type: VehicleType) -> Vehicle:
        vehicle = Vehicle(vehicle_number, vehicle_type)
        return self.vehicle_repository.create_vehicle(vehicle)

    def find_or_create_vehicle(
        self, vehicle_number: str, vehicle_type: VehicleType
    ) -> Vehicle:
        existing_vehicle = self.get_vehicle(vehicle_number)
        if existing_vehicle is not None:
            return existing_vehicle

        return self.create_vehicle(vehicle_number, vehicle_type)
