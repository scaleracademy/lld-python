from parking_lot.models import ParkingLot


class ParkingLotRepository:
    def __init__(self):
        self.parking_lots = []

    def create_parking_lot(self, parking_lot: ParkingLot) -> ParkingLot:
        parking_lot.id = len(self.parking_lots) + 1
        self.parking_lots.append(parking_lot)
        return parking_lot

    def get_parking_lot(self, id: int) -> ParkingLot:
        for parking_lot in self.parking_lots:
            if parking_lot.id == id:
                return parking_lot
        return None
