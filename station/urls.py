from django.urls import path
from rest_framework import routers

from station.views import Dashboard, StationViewSet, SensorViewSet

router = routers.SimpleRouter()
router.register(r'stations', StationViewSet, basename='station')
router.register(r'sensors', SensorViewSet, basename='sensor')

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
]
urlpatterns += router.urls
