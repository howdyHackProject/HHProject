from django.shortcuts import render
from django.views.generic import TemplateView

from .models import User

class LoginPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'loginPage.html', context=None)
