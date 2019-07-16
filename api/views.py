from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response

from api.serializers import StationsSerializer, SensorsListSerializer, SensorDataSerializer
from station.models import Station, Sensor, SensorData


class StationViewSet(viewsets.ViewSet):
    queryset = Station.objects.all()

    def list(self, request):
        serializer = StationsSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        station = get_object_or_404(self.queryset, pk=pk)
        serializer = StationsSerializer(station)
        return Response(serializer.data)


class SensorViewSet(viewsets.ModelViewSet):

    queryset = Sensor.objects.all()
    serializer_class = SensorsListSerializer

    def list(self, request, **kwargs):
        queryset = Sensor.objects.all()
        serializer = SensorsListSerializer(queryset, many=True, read_only=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, **kwargs):
        sensor_data = SensorData.objects.all().filter(sensor=pk)
        serializer = SensorDataSerializer(sensor_data, many=True)
        return Response(serializer.data)