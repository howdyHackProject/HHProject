from django.shortcuts import render
from django.views.generic import TemplateView

# from models import User

class HomePage(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'homePage.html', context=None)