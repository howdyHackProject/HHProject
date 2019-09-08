from django.shortcuts import render
from django.views.generic import TemplateView

from .models import User

class ProfilePageView(TemplateView):
    def get(self, request, **kwargs):

        u = User(
            first_name="kjdf", 
            last_name="kdjfkejfdsfef", 
            interests = ["first thing", "jkdjke"]
        )
        context = {'user' : u}
        return render(request, 'profilePage.html', context)