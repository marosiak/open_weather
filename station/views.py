# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from station.models import Station, Sensor, SensorData
from station.serializers import StationsSerializer, SensorsSerializer, SensorsListSerializer, SensorDataSerializer


class Dashboard(View):
    def get(self, request):
        return render(request, 'dashboard.html')


# class StationsList(generics.ListCreateAPIView):
#     queryset = Station.objects.all()
#     serializer_class = StationsSerializer
#
#
# class StationDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Station.objects.all()
#     serializer_class = StationsSerializer


class StationViewSet(viewsets.ViewSet):
    queryset = Station.objects.all()

    def list(self, request):
        serializer = StationsSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        station = get_object_or_404(self.queryset, pk=pk)
        serializer = StationsSerializer(station)
        return Response(serializer.data)


class SensorViewSet(viewsets.ViewSet):
    queryset = Sensor.objects.all()

    def list(self, request):
        serializer = SensorsListSerializer(self.queryset, many=True, read_only=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        sensor = get_object_or_404(self.queryset, pk=pk)
        serializer = SensorsSerializer(sensor)
        return Response(serializer.data)

    @action(detail=True, methods=['post', 'get'])
    def data(self, request, pk=None):
        datas = SensorData.objects.all().filter(sensor=pk)
        serializer = SensorDataSerializer(datas, many=True)

        return Response(serializer.data)

