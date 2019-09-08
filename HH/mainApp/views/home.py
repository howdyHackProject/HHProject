from django.shortcuts import render
from django.views.generic import TemplateView

from .models import User

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'homePage.html', context=None)