from book_my_show.strategies.pricing_strategy import PricingStrategy
from book_my_show.models import Booking
from book_my_show.enums import SeatType


class SeatBasedPricingStrategy(PricingStrategy):
    def calculate_price(self, booking: Booking) -> float:
        price = 0
        for seat in booking.seats.all():
            price += self.decide_price(seat.type)
        return price

    @staticmethod
    def decide_price(type: SeatType) -> float:
        return {
            SeatType.GOLD: 100,
            SeatType.PREMIUM: 200,
            SeatType.EXECUTIVE: 300,
        }[type]
