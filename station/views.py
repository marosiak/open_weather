# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import View

from .models import Station


class DashboardView(View):
    def get(self, request):
        return render(request, 'dashboard.html', {'is_dashboard': True})


class StationsView(ListView):

    template_name = 'stations.html'
    model = Station
    context_object_name = 'stations'
    queryset = Station.objects.all()
