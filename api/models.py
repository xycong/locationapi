from django.db import models


# # Create your models here.
# class Category(models.Model):
#     category = models.CharField(max_length=150, unique=True)
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_modified = models.DateTimeField(auto_now=True)


class Location(models.Model):
    name = models.CharField(db_index=True, max_length=255)
    lat = models.FloatField()
    lon = models.FloatField()
    category = models.CharField(max_length=150)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)