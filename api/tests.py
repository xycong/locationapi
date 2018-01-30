from django.test import TestCase
from .models import Location

# Create your tests here.


class ModelTestCase(TestCase):
    def setUp(self):
        self.location_name = "Loblaws"
        self.location = Location(name=self.location_name)

    def test_model_can_create_a_location(self):
        old_count = Location.objects.count()
        self.location.save()
        new_count = Location.objects.count()
        self.assertNotEqual(old_count, new_count)
