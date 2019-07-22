# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView

from .models import Station, Sensor, SensorData


class DashboardView(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_dashboard'] = True
        return context


class StationsList(ListView):
    template_name = 'stations.html'
    model = Station
    context_object_name = 'stations'


class StationDetail(DetailView):
    template_name = 'station_detail.html'
    model = Station

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sensors'] = Sensor.objects.all().filter(station=self.kwargs['pk'])
        return context


class SensorDetail(DetailView):
    template_name = 'sensor_detail.html'
    model = Sensor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['datas'] = SensorData.objects.all().filter(sensor=self.kwargs['pk'])
        return context
