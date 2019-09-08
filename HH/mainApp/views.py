 # mainApp/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class WelcomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class LoginPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'login.html', context=None)

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'home.html', context=None)

class ProfilePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'profile.html', context=None)

class EditProfilePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'editProfile.html', context=None)
