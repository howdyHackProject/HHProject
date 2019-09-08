#mainApp/urls.py
from django.conf.urls import url
from mainApp import views


urlpatterns = [
    url(r'^$', views.WelcomePageView.as_view()),
    url(r'^signIn/$', views.LoginPageView.as_view()),
    url(r'^home/$', views.HomePageView.as_view()),
    url(r'^profile/$', views.ProfilePageView.as_view()),
    url(r'^editProfile/$', views.EditProfilePageView.as_view()),
]