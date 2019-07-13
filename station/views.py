# Create your views here.
from django.shortcuts import render
from django.views.generic.base import View
from rest_framework import generics

from station.models import Station, Sensor, SensorData
from station.serializers import StationsSerializer, SensorsSerializer, SensorsListSerializer


class Dashboard(View):
    def get(self, request):
        return render(request, 'dashboard.html')


class StationsList(generics.ListCreateAPIView):
    queryset = Station.objects.all()
    serializer_class = StationsSerializer


class StationDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Station.objects.all()
    serializer_class = StationsSerializer


class SensorsList(generics.ListCreateAPIView):
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Sensor.objects.all().filter(station=pk)

    serializer_class = SensorsListSerializer


# TODO: FIX
class SensorDetails(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        pk = self.kwargs['pk_sensor']
        return Sensor.objects.all().filter(pk=pk)

    serializer_class = SensorsSerializer
