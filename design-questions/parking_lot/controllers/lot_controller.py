from parking_lot.models import ParkingLot
from parking_lot.services.lot_service import ParkingLotService
from parking_lot.dtos import CreateParkingLotRequest


class ParkingLotController:
    def __init__(self):
        self.parking_lot_service = ParkingLotService()

    def create_parking_lot(self, request: CreateParkingLotRequest) -> ParkingLot:
        self.validate_create_request(request)
        parking_lot = self.to_parking_lot(request)
        return self.parking_lot_service.create_parking_lot(parking_lot)

    def validate_create_request(self, request: CreateParkingLotRequest) -> None:
        if not request.name:
            raise ValueError("Name cannot be empty")

        if not request.address:
            raise ValueError("Address cannot be empty")

    def to_parking_lot(self, request: CreateParkingLotRequest) -> ParkingLot:
        return ParkingLot(
            name=request.name,
            address=request.address,
        )
