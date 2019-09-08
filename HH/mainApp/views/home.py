from django.shortcuts import render
from django.views.generic import TemplateView

from ..models import User

from mainApp.database.userDao import UserDao

class HomePage(TemplateView):

    # run when user first signs up
    def get(self, request, **kwargs):
        if (request.method == "POST"):
            user = User()
            user.firstName = request.POST.get("first_name")
            user.lastName = request.POST.get("last_name")
            user.age = request.POST.get("age")
            user.username = request.POST.get("username")
            user.password = request.POST.get("password")
            user.save()
        return render(request, 'homePage.html', context=None)