from parking_lot.models import ParkingLot
from parking_lot.repositories.lot_repository import ParkingLotRepository


class ParkingLotService:
    def __init__(self):
        self.parking_lot_repository = ParkingLotRepository()

    def create_parking_lot(self, parking_lot: ParkingLot) -> ParkingLot:
        return self.parking_lot_repository.create_parking_lot(parking_lot)

    def get_parking_lot(self, id: int) -> ParkingLot:
        return self.parking_lot_repository.get_parking_lot(id)
