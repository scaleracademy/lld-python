from django.db import models


class PaymentMode(models.TextChoices):
    UPI = "UPI"
    CREDIT_CARD = "CREDIT_CARD"
    NET_BANKING = "NET_BANKING"


class PaymentStatus(models.TextChoices):
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


class BookingStatus(models.TextChoices):
    BOOKED = "BOOKED"
    CANCELLED = "CANCELLED"
    PENDING = "PENDING"


class MovieFeature(models.TextChoices):
    THREE_D = "3D"
    FOUR_D = "4D"
    IMAX = "IMAX"
    DOLBY = "DOLBY_ATMOS"


class SeatStatus(models.TextChoices):
    BOOKED = "BOOKED"
    AVAILABLE = "AVAILABLE"
    LOCKED = "LOCKED"
    RESERVED = "RESERVED"


class SeatType(models.TextChoices):
    GOLD = "GOLD"
    PREMIUM = "PREMIUM"
    EXECUTIVE = "EXECUTIVE"
