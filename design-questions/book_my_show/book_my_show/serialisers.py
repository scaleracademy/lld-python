from rest_framework import serializers
from book_my_show.models import User, Booking


class AllUserFieldsSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserNoPasswordSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email']

class BookingSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
