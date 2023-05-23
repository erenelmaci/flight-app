from rest_framework.viewsets import ModelViewSet
from .serializers import (
    Passenger, PassengerSerializer,
    Flight, FlightSerializer,
    Reservation, ReservationSerializer
)


# -----------------------------------------------------------
# --------------------- FixView -----------------------------
# -----------------------------------------------------------
class FixView(ModelViewSet):
    pass


# -----------------------------------------------------------
# --------------------- PassengerView -----------------------
# -----------------------------------------------------------
class PassengerView(FixView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


# -----------------------------------------------------------
# --------------------- FlightView --------------------------
# -----------------------------------------------------------
class FlightView(FixView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


# -----------------------------------------------------------
# --------------------- ReservationView ---------------------
# -----------------------------------------------------------
class ReservationView(FixView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
