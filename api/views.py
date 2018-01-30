from django.shortcuts import render
from rest_framework import generics
from .serializers import LocationSerializer
from .models import Location
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger('django')


# Create your views here.
class LocationList(generics.ListCreateAPIView):
    serializer_class = LocationSerializer

    def get_queryset(self):
        query_params = self.request.query_params

        # coords = query_params.get('coords', None)
        # radius = query_params.get('radius', None)
        category = query_params.get('category', None)
        logger.info("The value of category is %s", category)
        # count = query_params.get('count', None)

        queryset = Location.objects.all()
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset