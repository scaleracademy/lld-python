from abc import ABC, abstractmethod
from typing import List
from parking_lot.models import ParkingSpot
from parking_lot.enums import ParkingSpotType


class SpotAllocationStrategy(ABC):
    @abstractmethod
    def get_spot(
        self, parking_spots: List[ParkingSpot], spot_type: ParkingSpotType
    ) -> ParkingSpot:
        pass
