from django.shortcuts import get_object_or_404
# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response

from api.serializers import StationsSerializer, SensorsSerializer, SensorDataSerializer
from .permissions import IsSensorOwner
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
    serializer_class = SensorsSerializer

    def list(self, request, **kwargs):
        queryset = Sensor.objects.all().filter(station=self.kwargs['station_pk'])
        serializer = SensorsSerializer(queryset, many=True, read_only=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, **kwargs):
        queryset = Sensor.objects.all().filter(pk=pk)
        serializer = SensorsSerializer(queryset, many=True, read_only=True)
        return Response(serializer.data)

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (IsSensorOwner,)
        return super(SensorViewSet, self).get_permissions()


class SensorDataViewSet(viewsets.ModelViewSet):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer
