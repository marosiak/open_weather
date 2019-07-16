from django.urls import path

from station.views import Dashboard

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
]
