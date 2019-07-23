import django_filters
from django.db.models.functions import datetime
from django_filters import CharFilter

from .models import SensorData

from django.template.defaulttags import register


@register.filter
def get_arg(dictionary, key):
    return dictionary[key].capitalize()


class SensorDataFilter(django_filters.FilterSet):
    range = CharFilter(method='range_filter')

    class Meta:
        model = SensorData
        fields = ['date', 'value', 'sensor']

    def range_filter(self, queryset, range, value):
        count = 10
        long_date_filter = "%A %H:%M"
        date_filter = "%m/%d"
        now = datetime.datetime.now()

        if value == "daily":
            count = 10
            long_date_filter = "%A %H:%M"
            date_filter = "%H:%M"
            queryset = queryset.filter(date__range=(datetime.datetime(now.year, now.month, now.day), now))

        if value == "weekly":
            count = 7
            long_date_filter = "%A %H:%M"
            date_filter = "%m/%d"
            queryset = queryset.filter(date__range=(datetime.datetime(now.year, now.month, now.day - 7), now))

        if value == "monthly":
            count = 30
            long_date_filter = "%d/%m"
            date_filter = "%d"
            queryset = queryset.filter(date__range=(datetime.datetime(now.year, now.month, 1), now))

        queryset = queryset.order_by('date')[:count]
        for data in queryset:
            data.long_date = data.date.strftime(long_date_filter)
            data.date = data.date.strftime(date_filter)
        return queryset