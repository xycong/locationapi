from rest_framework import serializers
from .models import Location, Category


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'lat', 'lon', 'category', 'date_created',
                  'date_modified')
        read_only_fields = ('date_created', 'date_modified')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
