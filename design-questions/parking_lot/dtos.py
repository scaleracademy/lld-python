from datetime import datetime
from dataclasses import dataclass
from parking_lot.enums import VehicleType

@dataclass
class CreateParkingLotRequest:
    name: str
    address: str

@dataclass
class IssueTicketRequest:
    parking_lot_id: int
    vehicle_number: str
    vehicle_type: VehicleType
    entry_gate_id: int
    entry_time: datetime
