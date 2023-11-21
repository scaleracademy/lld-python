from enum import Enum

class ParkingSpotType(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class ParkingSpotStatus(Enum):
    OCCUPIED = 1
    FREE = 2
    OUT_OF_ORDER = 3

class PaymentType(Enum):
    CASH = 1
    CREDIT_CARD = 2
    UPI = 3

class PaymentStatus(Enum):
    DONE = 1
    PENDING = 2

class VehicleType(Enum):
    CAR = 1
    TRUCK = 2
    BUS = 3
    BIKE = 4
    SCOOTER = 5