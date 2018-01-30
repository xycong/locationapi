from django.shortcuts import render
from rest_framework import generics
from .serializers import LocationSerializer

# Create your views here.
class CreateView(generics.ListCreateAPIView):
  queryset = List.objects.all()
  serializer_class = LocationSerializer

  def perform_create(self, serializer):
    serializer.save()