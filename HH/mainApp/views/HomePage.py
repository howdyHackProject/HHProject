from django.shortcuts import render
from django.views.generic import TemplateView

from ..models import User

from mainApp.database.userDao import UserDao

class HomePage(TemplateView):

    # run when user first signs up
    def get(self, request, **kwargs):
<<<<<<< HEAD:HH/mainApp/views/home.py
        # context = {'temp' : "this function is being run"}
        # if (request.method != "POST"):
        #     return render(request, 'homePage.html', context=None)
        # print("Request method was POST")
        user = User()
        user.firstName = request.GET.get("first_name")
        print(user.firstName)
        user.lastName = request.GET.get("last_name")
        user.age = request.GET.get("age")
        user.username = request.GET.get("username")
        user.password = request.GET.get("password")
        user.save()

        context = {'u' : user}

        return render(request, 'homePage.html', context)
=======
        if (request.method == "POST"):
            user = User()
            user.firstName = request.POST.get("first_name")
            user.lastName = request.POST.get("last_name")
            user.age = request.POST.get("age")
            user.username = request.POST.get("username")
            user.password = request.POST.get("password")
            user.save()
        return render(request, 'homePage.html', context=None)
>>>>>>> 3c8fa29cf4b501a789aaac37c9580e1052169aae:HH/mainApp/views/HomePage.py
