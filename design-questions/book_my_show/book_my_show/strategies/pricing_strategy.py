from abc import ABC, abstractmethod
from book_my_show.models import Booking


class PricingStrategy(ABC):
    @abstractmethod
    def calculate_price(self, booking: Booking) -> float:
        pass
