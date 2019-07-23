from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from .models import Station, Sensor, SensorData


class StationTest(TestCase):
    def setUp(self):
        test_guy = User.objects.create(username="test_guy")
        Station.objects.create(name="test", city="city", region="region", owner=test_guy)

    def test_station_exists(self):
        station = Station.objects.get(name="test", city="city", region="region")
        self.assertTrue(station)

    def test_station_owned(self):
        station = Station.objects.get(name="test", city="city", region="region")
        self.assertEqual(station.owner.username, "test_guy")


class SensorTest(TestCase):
    def setUp(self):
        test_guy = User.objects.create(username="test_guy")
        station = Station.objects.create(name="test", city="city", region="region", owner=test_guy)
        sensor = Sensor.objects.create(station=station, name="test_sensor", unit="t")

        SensorData.objects.create(value=1.0, sensor=sensor)
        SensorData.objects.create(value=2.1, sensor=sensor)
        SensorData.objects.create(value=5.12, sensor=sensor)

    def test_sensor_exists(self):
        sensor = Sensor.objects.get(name="test_sensor", unit="t")
        self.assertTrue(sensor)

    def test_sensor_station(self):
        sensor = Sensor.objects.get(name="test_sensor", unit="t")
        self.assertEqual(sensor.station.name, "test")

    def test_sensor_data_count(self):
        sensor = Sensor.objects.get(name="test_sensor", unit="t")
        data = SensorData.objects.filter(sensor=sensor)
        self.assertEqual(data.count(), 3)

    def test_sensor_data_accessibility(self):
        sensor = Sensor.objects.get(name="test_sensor", unit="t")
        data = SensorData.objects.filter(sensor=sensor)
        self.assertEqual(data.first().value, 1.0)

    def test_sensor_last_value(self):
        sensor = Sensor.objects.get(name="test_sensor", unit="t")
        self.assertEqual(sensor.last_value, 5.12)


