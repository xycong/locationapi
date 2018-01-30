from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(
        r'^locations/$',
        views.LocationList.as_view(),
        name="index"),
]

urlpatterns = format_suffix_patterns(urlpatterns)