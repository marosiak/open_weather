# Create your models here.
from django.db import models as models
from datetime import datetime


class Station(models.Model):
    name = models.CharField(max_length=40)
    city = models.CharField(max_length=85)  # That is the longest city name being owned by city in New Zealand :)
    region = models.CharField(max_length=60)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    last_update = models.DateTimeField(editable=False, null=True)
    last_value = models.FloatField(editable=False, null=True)
    unit = models.CharField(max_length=7)
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='sensors')

    def __str__(self):
        return f'{self.station.name}: {self.name}'


class SensorData(models.Model):
    value = models.FloatField()
    date = models.DateTimeField(auto_now=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='data')

    def save(self, *args, **kwargs):
        # TODO: Timezone now for last_update! (I have no internet at this moment so can't google this shit out)
        output = super(SensorData, self).save(*args, **kwargs)
        self.sensor.last_value = self.value
        self.sensor.save()
        return output

    def __str__(self):
        return f'{self.sensor.name} = {self.value}'
