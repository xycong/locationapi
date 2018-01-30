from rest_framework import serializers
from .models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'lat', 'lon', 'category', 'date_created',
                  'date_modified')
        read_only_fields = ('date_created', 'date_modified')
