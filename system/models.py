from django.db import models

# Create your models here.
class address_info(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
    data = models.CharField(max_length=200)
