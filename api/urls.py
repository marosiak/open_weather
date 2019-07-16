from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from api.views import StationViewSet, SensorViewSet

router = routers.SimpleRouter()
router.register(r'stations', StationViewSet, basename='station')
router.register(r'sensors', SensorViewSet, basename='sensor')

urlpatterns = [
    url(r'^api/', include((router.urls, 'Open Weather'))),
]
