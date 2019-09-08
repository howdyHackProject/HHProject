from django.conf.urls import url

from ..views.launch import LaunchPage
from ..views.login import LoginPage
from ..views.home import HomePage
from ..views.profile import ProfilePage
from ..views.editProfile import EditProfilePage
from ..views.signup import SignupPage
#, login, home, profile, editProfile


urlpatterns = [
    url(r'^$', LaunchPage.as_view()),
    url(r'^signUp/', SignupPage.as_view()),
    url(r'^signIn/$', LoginPage.as_view()),
    url(r'^home/$', HomePage.as_view()),
    url(r'^profile/$', ProfilePage.as_view()),
    url(r'^editProfile/$', EditProfilePage.as_view()),
]