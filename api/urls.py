from django.conf.urls import url
from django.urls import include
from rest_framework_nested import routers

from api.views import StationViewSet, SensorViewSet

router = routers.SimpleRouter()
router.register(r'stations', StationViewSet)

stations_router = routers.NestedSimpleRouter(router, r'stations', lookup='station')
stations_router.register(r'sensors', SensorViewSet, base_name='station-sensors')


urlpatterns = [
    url(r'^api/', include((router.urls, 'Open Weather'))),
    url(r'^api/', include((stations_router.urls, 'Open Weather'))),
]
