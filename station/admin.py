from django.contrib import admin

# Register your models here.
from station.models import Station, Sensor, SensorData

admin.site.register(Station)
admin.site.register(Sensor)
admin.site.register(SensorData)

