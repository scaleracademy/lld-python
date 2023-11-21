from django.db import models
from book_my_show.enums import (
    PaymentMode,
    PaymentStatus,
    BookingStatus,
    MovieFeature,
    SeatStatus,
)


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)


class City(models.Model):
    name = models.CharField(max_length=255)


class Theater(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class Hall(models.Model):
    name = models.CharField(max_length=255)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)


class Seat(models.Model):
    number = models.CharField(max_length=255)
    seat_type = models.CharField(max_length=255)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)


class Language(models.Model):
    name = models.CharField(max_length=50)


class MovieFeatures(models.Model):
    name = models.CharField(max_length=50)


class Movie(models.Model):
    name = models.CharField(max_length=255)
    rating = models.IntegerField()
    category = models.CharField(max_length=50)
    languages = models.ManyToManyField(Language)
    features = models.ManyToManyField(
        MovieFeatures, limit_choices_to=MovieFeature.choices
    )


class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    duration = models.IntegerField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    features = models.ManyToManyField(
        MovieFeatures, limit_choices_to=MovieFeature.choices
    )


class ShowSeat(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    status = models.CharField(choices=SeatStatus.choices, max_length=50)


class Booking(models.Model):
    amount = models.FloatField()
    seats = models.ManyToManyField(ShowSeat)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(choices=BookingStatus.choices, max_length=50)
    booked_at = models.DateTimeField(auto_now_add=True)


class Payment(models.Model):
    amount = models.FloatField()
    mode = models.CharField(choices=PaymentMode.choices, max_length=50)
    status = models.CharField(choices=PaymentStatus.choices, max_length=50)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
