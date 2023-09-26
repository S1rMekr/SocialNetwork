from django import forms
from myPage.models import *
from django.contrib.auth.forms import UserCreationForm, User, AuthenticationForm
from django.contrib.auth import get_user_model
User = get_user_model()

# class AddPostForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#     class Meta:
#         model = PostModel
#         fields = ['title',  'content', 'picture']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-input'}),
#             'content': forms.TextInput(attrs={'class': 'content-input'}),
#         }


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(
        label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(
        label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(
        attrs={'class': 'form-input'}))
    password1 = forms.CharField(
        label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(
        label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'country', 'profile_image', 'birth_date']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
            'country' : forms.Select(attrs={'class': 'select_input'})
        }


class LoginUserForm(AuthenticationForm):
    password = forms.CharField(
        label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

