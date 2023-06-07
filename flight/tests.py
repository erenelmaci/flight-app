# from django.test import TestCase
from rest_framework.test import APIRequestFactory, APITestCase
from django.contrib.auth.models import AnonymousUser, User
from .views import FlightView
from rest_framework.test import force_authenticate


class FlightTestCase(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            username='eren',
            email='meren1623@hotmail.com',
            password="elmacimeren1623"
        )

    def test_flight_list_as_guest_user(self):
        request = self.factory.get('/flight/flights/')
        request.user = AnonymousUser()
        response = FlightView.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, 200)

    def test_flight_create_as_guest_user(self):
        request = self.factory.post('/flight/flights/')
        request.user = AnonymousUser()
        response = FlightView.as_view({'post': 'create'})(request)
        self.assertEqual(response.status_code, 401)

    def test_flight_create_as_login_user(self):
        request = self.factory.post('/flight/flights/')
        force_authenticate(request, user=self.user)
        response = FlightView.as_view({'post': 'create'})(request)
        self.assertEqual(response.status_code, 400),

    def test_flight_create_as_admin_user(self):
        data = {
            "flight_number": "TK100",
            "airlines": "THY",
            "departure_city": "Antalya",
            "arrival_city": "Amsterdam",
            "date_of_departure": "2022-12-03",
            "etd": "15:27:22"
        }
        request = self.factory.post('/flight/flights/', data, format='json')
        force_authenticate(request, user=self.user)
        self.user.is_staff = True
        self.user.save()
        response = FlightView.as_view({'post': 'create'})(request)
        self.assertEqual(response.status_code, 400)
