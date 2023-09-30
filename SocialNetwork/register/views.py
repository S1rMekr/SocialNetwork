from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import *
from django.views.generic import *
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout, login
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
class Register(CreateView):
    form_class = RegisterUserForm
    template_name = 'register/register.html'
    

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('myPage:home')


class Login(LoginView):
    form_class = LoginUserForm
    template_name = 'register/login.html'


    def get_success_url(self):
        return reverse_lazy('myPage:home')
    
