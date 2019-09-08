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

        user = User(first_name="kjdf", last_name="kdjfkejfdsfef", interests = ["first thing", "jokes"])
        user2 = User(first_name="Jane", last_name="Phillip", interests = ["basketball","singing"])
        user3 = User(first_name="Jim", last_name="Rogers", interests = ["art","reading"])
        user4 = User(first_name="Yeon", last_name="Smith", interests = ["pokemon go","basketball"])
        user5 = User(first_name="Anushree", last_name="Sang", interests = ["animals","reading"])
        user6 = User(first_name="Vahmin", last_name="James", interests = ["animals","art"])
        user7 = User(first_name="Paul", last_name="Holden", interests = ["movies","basketball"])
        user8 = User(first_name="Jessica", last_name="ksdkg", interests = ["basketball","movies"])
        user9 = User(first_name="Joseph", last_name="Yeatts", interests = ["basketball","pokemon go"])
        user10 = User(first_name="Angel", last_name="Mcmichael", interests = ["art","fashion"])
        user11 = User(first_name="Peter", last_name="Donald", interests = ["sofas","driving"])
        user12 = User(first_name="Kim", last_name="Robin", interests = ["sofas","rugs"])

        context = {
            'user1' : user
            'user2' : user2,
            'user3' : user3,
            'user4' : user4,
            'user5' : user5,
            'user6' : user6,
            'user7' : user7,
            'user8' : user8,
            'user9' : user9,
            'user10' : user10,
            'user11' : user11,
            'user12' : user12,
        }
        return render(request, 'profile.html', context)

class EditProfilePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'editProfile.html', context=None)
