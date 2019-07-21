from django.urls import path

from station.views import DashboardView, StationsList, StationDetail

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('stations/', StationsList.as_view(), name='stations'),
    path('stations/<int:pk>', StationDetail.as_view(), name='station-detail'),
]
