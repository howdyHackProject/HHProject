 # mainApp/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import User

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
        user = User(first_name="kjdf", last_name="kdjfkejfdsfef", interests = ["first thing", "jkdjke"])
        context = {'user1' : user}
        return render(request, 'profile.html', context)

class EditProfilePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'editProfile.html', context=None)
