from django.shortcuts import render
from django.views.generic import TemplateView

# from ..models import User

class EditProfilePage(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'editProfilePage.html', context=None)