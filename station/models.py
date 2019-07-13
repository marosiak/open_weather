# Create your models here.
from django.db import models as models


class Station(models.Model):
    name = models.CharField(max_length=40)
    city = models.CharField(max_length=85)  # That is the longest city name being owned by city in New Zealand :)

    def __str__(self):
        return self.name


class Sensor(models.Model):
    name = models.CharField(max_length=255)
    last_update = models.DateTimeField(editable=False, null=True)
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='station')

    def __str__(self):
        return f'{self.station.name}: {self.name}'


class SensorData(models.Model):
    value = models.FloatField()
    date = models.DateTimeField(auto_now=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='sensor')

    def __str__(self):
        return f'{self.name} = {self.value}'
