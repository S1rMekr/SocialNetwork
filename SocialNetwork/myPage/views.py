from typing import Any
from django.db import models
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from myPage.models import CustomUser, PostModel
from django.shortcuts import render
from .forms import *


from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.


class IndexView(generic.ListView):
    template_name="myPage/index.html"
    context_object_name="users"

    def get_queryset(self):
        return User.objects.all()
    
class ProfileView(generic.DetailView):
    model = User
    template_name="myPage/profile.html"
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['post'] = PostModel.objects.filter(author=user)
        return context

        

class AddPost(generic.CreateView):
    model = PostModel
    fields = ['title', 'content', 'picture']
    template_name='myPage/add_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return redirect('myPage:profile', self.request.user.id)
    

class UserSettings(generic.edit.UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email', 'country', 'profile_image']
    template_name = 'myPage/user_settings.html'

    def get_object(self):
        return self.request.user
    
    def get_success_url(self):
        return reverse_lazy('myPage:profile', kwargs={'pk': self.object.pk})