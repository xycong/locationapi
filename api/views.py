from django.shortcuts import render
from rest_framework import generics
from .serializers import LocationSerializer
from .models import Location
from .utils import getDistance
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger('django')


class LocationList(generics.ListAPIView):
    serializer_class = LocationSerializer

    def get_queryset(self):
        queryset = Location.objects.all()
        # Get the query parameters
        query_params = self.request.query_params
        category = query_params.get('category', None)
        coords = query_params.get('coords', None)
        radius = query_params.get('radius', None)
        count = query_params.get('count', None)

        coordsData = []
        if coords and radius is not None:
            for coord in coords.split(','):
                coordsData.append(float(coord))
            logger.info("The current location is %s", coordsData)
        
            # Optional filters
            if category is not None:
                queryset = queryset.filter(category=category)
            
            # Calculate distance for each remaining object
            excluded = []
            for curr in queryset:
                dist = getDistance(coordsData, curr.lat, curr.lon)
                logger.info("The distance from here is %sm", round(dist, 2))
                if dist > int(radius):
                    excluded.append(curr)
            # Exclude objects with distance greater than radius
            queryset = queryset.exclude(name__in=excluded)

            if count is not None:
                queryset = queryset[0:int(count)]
        return queryset