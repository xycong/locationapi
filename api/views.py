from django.shortcuts import render
from rest_framework import generics
from .serializers import LocationSerializer
from .models import Location
from django.db.models import F
from math import radians, sin, cos, acos
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger('django')


# Create your views here.
class LocationList(generics.ListAPIView):
    serializer_class = LocationSerializer

    def get_queryset(self):
        queryset = Location.objects.all()
        query_params = self.request.query_params
        category = query_params.get('category', None)
        coords = query_params.get('coords', None)
        radius = query_params.get('radius', None)
        count = query_params.get('count', None)
        logger.info("The value of category is %s", category)
        logger.info("The value of radius is %s", radius)

        coordsData = []
        if coords is not None:
            for coord in coords.split(','):
                coordsData.append(float(coord))
            logger.info("The value of coords is %s", coordsData)
            if radius is not None:
                if category is not None:
                    queryset = queryset.filter(category=category)
                for loc in queryset:
                    slat = radians(coordsData[0])
                    slon = radians(coordsData[1])
                    elat = radians(loc.lat)
                    elon = radians(loc.lon)
                    dist = 6371.01 * 1000 * acos(
                        sin(slat) * sin(elat) +
                        cos(slat) * cos(elat) * cos(slon - elon))
                    logger.info("The value of distance is %s", round(dist, 2))
                    if (dist > int(radius)):
                        queryset = queryset.exclude(name=loc.name)
                if count is not None:
                    queryset = queryset[0:int(count)]
        return queryset