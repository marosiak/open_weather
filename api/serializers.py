from rest_framework import serializers

from station.models import Station, Sensor, SensorData


class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ('value', 'date')


class SensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('id', 'name', 'station')


class StationsSerializer(serializers.ModelSerializer):
    sensors = SensorsSerializer(many=True)

    class Meta:
        model = Station
        fields = ('id', 'name', 'city', 'sensors')
