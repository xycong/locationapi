from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import re_path
from . import views

app_name = 'locations'
urlpatterns = [
    re_path(r'^locations/(?P<category>\w+)/', views.LocationList.as_view(), name="index"),
]

urlpatterns = format_suffix_patterns(urlpatterns)