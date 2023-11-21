from typing import List
from parking_lot.models import ParkingSpot


class ParkingSpotRepository:
    def __init__(self):
        self.parking_spots: List[ParkingSpot] = []

    def get_parking_spots(self, lot_id: int) -> List[ParkingSpot]:
        return [spot for spot in self.parking_spots if spot.lot_id == lot_id]

    def create_parking_spot(self, spot: ParkingSpot) -> ParkingSpot:
        if spot not in self.parking_spots:
            self.parking_spots.append(spot)
            return spot
        
        for index, existing_spot in enumerate(self.parking_spots):
            if existing_spot == spot:
                self.parking_spots[index] = spot
                break
        return spot
