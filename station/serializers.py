from rest_framework import serializers

from station.models import Station, Sensor, SensorData


class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ('value', 'date')


class SensorsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('id', 'name')


class SensorsSerializer(serializers.ModelSerializer):
    sensor = SensorDataSerializer(many=True, read_only=True)

    class Meta:
        model = Sensor
        fields = ('id', 'name', 'sensor')


class StationsSerializer(serializers.ModelSerializer):
    sensors = SensorsListSerializer(many=True, read_only=True)

    class Meta:
        model = Station
        fields = ('id', 'name', 'city', 'sensors')
