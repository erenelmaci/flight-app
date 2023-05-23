from rest_framework import serializers
from .models import (
    Passenger,
    Flight,
    Reservation
)


# -----------------------------------------------------------
# --------------------- FixSerializer -----------------------
# -----------------------------------------------------------
class FixSerializer(serializers.ModelSerializer):
    pass


# -----------------------------------------------------------
# --------------------- PassengerSerializer -----------------
# -----------------------------------------------------------
class PassengerSerializer(FixSerializer):

    class Meta:
        model = Passenger
        exclude = []


# -----------------------------------------------------------
# --------------------- FlightSerializer --------------------
# -----------------------------------------------------------
class FlightSerializer(FixSerializer):

    class Meta:
        model = Flight
        exclude = []


# -----------------------------------------------------------
# --------------------- ReservationSerializer ---------------
# -----------------------------------------------------------
class ReservationSerializer(FixSerializer):

    class Meta:
        model = Reservation
        exclude = []