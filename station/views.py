# Create your views here.
from django.shortcuts import render
from django.views.generic.base import View


class Dashboard(View):
    def get(self, request):
        return render(request, 'dashboard.html')
