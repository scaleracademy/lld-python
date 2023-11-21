from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password
from django.utils import timezone

from book_my_show.models import User, Show, ShowSeat, SeatStatus, BookingStatus
from book_my_show.serialisers import (
    AllUserFieldsSerialiser,
    UserNoPasswordSerialiser,
    BookingSerialiser,
)
from book_my_show.strategies.pricing_strategies import SeatBasedPricingStrategy


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return AllUserFieldsSerialiser
        return UserNoPasswordSerialiser

    def perform_create(self, serializer):
        serializer.save(password=make_password(serializer.validated_data["password"]))


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserNoPasswordSerialiser


class BookingCreateView(generics.CreateAPIView):
    serializer_class = BookingSerialiser
    pricing_strategy = SeatBasedPricingStrategy()

    def create(self, request, *args, **kwargs):
        # Step 1 - Get the user through ID
        # Step 1b) - If user is not present, throw error
        user_id = request.data.get("user_id")
        user = get_object_or_404(User, id=user_id)

        # Step 2 - Get the show using show ID
        # Step 2b) - If show is not present, throw error
        show_id = request.data.get("show_id")
        show = get_object_or_404(Show, id=show_id)

        # Step 3 - Get the show seats using showSeat IDs
        # Step 4 - Check if all the seats are available
        show_seat_ids = request.data.get("seat_ids", [])
        show_seats = ShowSeat.objects.filter(id__in=show_seat_ids)

        for seat in show_seats:
            if seat.status != SeatStatus.AVAILABLE:
                raise ValueError("Seat is not available")

        # Step 5 - Mark all the seats as locked
        for seat in show_seats:
            seat.status = SeatStatus.LOCKED
            seat.save()

        # Step 7 - Create and save the booking
        booking_data = {
            "user": user.id,
            "show": show.id,
            "seats": show_seats,
            "status": BookingStatus.PENDING,
            "booked_at": timezone.now(),
        }

        serializer = BookingSerialiser(data=booking_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # Step 8 - Calculate and update the booking amount
        amount = self.pricing_strategy.calculate_price(serializer.instance)
        serializer.instance.amount = amount
        serializer.instance.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
