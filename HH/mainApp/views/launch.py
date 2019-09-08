from django.shortcuts import render
from django.views.generic import TemplateView

# from ..models import User

class LaunchPage(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'launchPage.html', context=None)