from django.shortcuts import render
from django.views.generic import TemplateView

# from ..models import Login

class LoginPage(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'loginPage.html', context=None)
