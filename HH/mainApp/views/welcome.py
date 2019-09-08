from django.shortcuts import render
from django.views.generic import TemplateView

from .models import User

class WelcomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'welcomePage.html', context=None)