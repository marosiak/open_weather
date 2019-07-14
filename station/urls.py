from django.urls import path

from station.views import Dashboard, StationsList, StationDetails, SensorsList, SensorDetails, SensorDataList

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),

    path('stations/', StationsList.as_view()),
    path('stations/<int:pk>/', StationDetails.as_view()),

    path('stations/<int:pk>/sensors', SensorsList.as_view()),
    path('stations/<int:pk_station>/sensors/<int:pk>', SensorDetails.as_view()),

    path('stations/<int:pk_station>/sensors/<int:pk>/data', SensorDataList.as_view()),
]



