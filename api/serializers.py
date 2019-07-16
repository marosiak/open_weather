from rest_framework import serializers

from station.models import Station, Sensor, SensorData


class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ('value', 'date')


class SensorsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('id', 'name', 'station')


class SensorsSerializer(serializers.ModelSerializer):
    data = SensorDataSerializer(many=True)

    class Meta:
        model = Sensor
        fields = ('id', 'name', 'data')


class StationsSerializer(serializers.ModelSerializer):
    sensors = SensorsListSerializer(many=True)

    class Meta:
        model = Station
        fields = ('id', 'name', 'city', 'sensors')
