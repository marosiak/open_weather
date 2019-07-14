# Create your views here.
from django.shortcuts import render
from django.views.generic.base import View
from rest_framework import generics

from station.models import Station, Sensor, SensorData
from station.serializers import StationsSerializer, SensorsSerializer, SensorsListSerializer, SensorDataSerializer


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


class SensorDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SensorsSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Sensor.objects.all().filter(pk=pk)


class SensorDataList(generics.ListCreateAPIView):
    serializer_class = SensorDataSerializer

    def perform_create(self, serializer):
        serializer.save(sensor=Sensor.objects.all().get(pk=self.kwargs['pk']))

    def get_queryset(self):
        pk = self.kwargs['pk']
        return SensorData.objects.all().filter(sensor=pk)
