from typing import List

from parking_lot.models import ParkingSpot, ParkingSpotStatus, ParkingSpotType
from parking_lot.strategies.allocation_strategy import SpotAllocationStrategy


class FirstAvailableSpotAllocationStrategy(SpotAllocationStrategy):
    def get_spot(
        self, parking_spots: List[ParkingSpot], spot_type: ParkingSpotType
    ) -> ParkingSpot:
        for spot in parking_spots:
            if spot.spot_type == spot_type and spot.status == ParkingSpotStatus.FREE:
                return spot
        return None
