from django.shortcuts import render
from django.views.generic import TemplateView

class SignupPage(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'signupPage.html', context=None)
