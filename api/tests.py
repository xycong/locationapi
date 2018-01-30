from rest_framework.test import APITestCase
from rest_framework import status
from .models import Location
from .serializers import LocationSerializer

# Create your tests here.


class LocationListViewTestCase(APITestCase):
    def test_location_get(self):
        response = self.client.get(
            '/locations?category=restaurant&coords=43.895776,-79.464448&count=2&radius=10000'
        )
        self.assertTrue(status.is_success(response.status_code))
