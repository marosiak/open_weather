from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from api.views import StationViewSet, SensorViewSet, SensorDataViewSet

router = DefaultRouter()
router.register(r'stations', StationViewSet, base_name='stations')

stations_router = routers.NestedSimpleRouter(router, r'stations', lookup='station')
stations_router.register(r'sensors', SensorViewSet, base_name='sensors')

sensors_router = routers.NestedSimpleRouter(stations_router, r'sensors', lookup='sensor')
sensors_router.register(r'data', SensorDataViewSet, base_name='datas')

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api/', include(stations_router.urls)),
    url(r'^api/', include(sensors_router.urls)),
]