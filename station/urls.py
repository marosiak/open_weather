from django.urls import path

from station.views import DashboardView, StationsView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('stations/', StationsView.as_view(), name='stations')
]
