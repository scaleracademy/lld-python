from __future__ import annotations
from datetime import datetime
from dataclasses import dataclass, field
from abc import ABC
from typing import List
from parking_lot.enums import (
    ParkingSpotType,
    ParkingSpotStatus,
    PaymentType,
    PaymentStatus,
    VehicleType,
)
from datetime import datetime


@dataclass
class BaseModel(ABC):
    id: int
    created_at: datetime
    updated_at: datetime


@dataclass
class ParkingLot(BaseModel):
    name: str
    address: str
    parking_floors: List[ParkingFloor] = field(default_factory=list)
    entry_gates: List[ParkingGate] = field(default_factory=list)
    exit_gates: List[ParkingGate] = field(default_factory=list)
    display_board: DisplayBoard


@dataclass
class ParkingFloor(BaseModel):
    floor_number: int
    parking_spots: List[ParkingSpot] = field(default_factory=list)
    payment_counter: PaymentCounter
    display_board: DisplayBoard


@dataclass
class ParkingSpot(BaseModel):
    spot_number: int
    spot_type: ParkingSpotType
    status: ParkingSpotStatus
    lot_id: int


@dataclass
class ParkingGate(BaseModel, ABC):
    attendant: ParkingAttendant


@dataclass
class EntryGate(ParkingGate):
    display_board: DisplayBoard


@dataclass
class ExitGate(ParkingGate):
    payment_counter: PaymentCounter


@dataclass
class ParkingAttendant(BaseModel):
    name: str
    email: str
    mobile: str


@dataclass
class PaymentCounter(BaseModel):
    floor_number: int


@dataclass
class DisplayBoard(BaseModel):
    floor_number: int
    gate_number: int


@dataclass
class ParkingTicket(BaseModel):
    parking_spot: ParkingSpot
    entry_time: datetime
    vehicle: Vehicle
    entry_gate: ParkingGate


@dataclass
class Invoice(BaseModel):
    exit_time: datetime
    exit_gate: ParkingGate
    parking_ticket: ParkingTicket
    amount: float
    payments: List[Payment] = field(default_factory=list)


@dataclass
class Payment(BaseModel):
    amount: float
    payment_type: PaymentType
    status: PaymentStatus
    time: datetime


@dataclass
class Vehicle(BaseModel):
    license_number: str
    type: VehicleType
