from rest_framework import permissions

from station.models import Station


class IsSensorOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        station_pk = view.kwargs['station_pk']
        station = Station.objects.all().get(pk=station_pk)

        if station.owner == request.user:
            return True

        return False
