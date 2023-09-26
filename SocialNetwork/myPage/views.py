from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from myPage.models import CustomUser, PostModel
from django.shortcuts import render

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.


class IndexView(generic.ListView):
    template_name="myPage/index.html"
    context_object_name="users"

    def get_queryset(self):
        return User.objects.all()
    
class ProfileView(generic.DetailView):
    template_name="myPage/profile.html"
    context_object_name='profile'
    model=User

    def get_queryset(self):
        return User.objects.all()