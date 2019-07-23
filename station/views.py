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
        query = SensorData.objects.all()
        context['datas'] = query.filter(sensor=self.kwargs['pk'])

        chart_datas = context['datas']
        chart_datas = chart_datas.order_by('-id')[:5]
        for chart__data in chart_datas:
            chart__data.date = chart__data.date.strftime("%d/%m %H:%M")
        context['chart_datas'] = reversed(chart_datas)
        return context
