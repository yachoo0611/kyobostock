from django.db import models

class Store(models.Model):
    place_name = models.CharField(max_length=50)
    road_address_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    in_seoul = models.BooleanField()
    x = models.CharField(max_length=20)
    y = models.CharField(max_length=20)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.place_name