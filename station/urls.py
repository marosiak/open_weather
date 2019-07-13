from django.urls import path

from station.views import Dashboard, StationsList, StationDetails, SensorsList, SensorDetails

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('stations/', StationsList.as_view()),
    path('stations/<int:pk>/', StationDetails.as_view()),
    path('stations/<int:pk>/sensors', SensorsList.as_view()),
    path('stations/<int:pk>/sensors/<int:pk_sensor>', SensorDetails.as_view()),
]



