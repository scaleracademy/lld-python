from parking_lot.models import ParkingSpot
from parking_lot.enums import ParkingSpotType
from parking_lot.repositories.spot_repository import ParkingSpotRepository
from parking_lot.strategies.allocation_strategy import SpotAllocationStrategy


class ParkingSpotService:
    def __init__(self, spot_allocation_strategy: SpotAllocationStrategy):
        self.spot_repository = ParkingSpotRepository()
        self.spot_allocation_strategy = spot_allocation_strategy

    def allocate_spot(self, lot_id: int, spot_type: ParkingSpotType) -> ParkingSpot:
        parking_spots = self.spot_repository.get_parking_spots(lot_id)
        return self.spot_allocation_strategy.get_spot(parking_spots, spot_type)

    def save_parking_spot(self, spot: ParkingSpot) -> ParkingSpot:
        return self.spot_repository.create_parking_spot(spot)
