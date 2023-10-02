from string import Template
from django.conf import settings
from django.utils.safestring import mark_safe
from django import forms
from django.forms import ImageField
from django.views.generic.edit import UpdateView
from .models import *
from django.contrib.auth.forms import UserCreationForm, User, AuthenticationForm

from django.contrib.auth import get_user_model
User = get_user_model()



class PictureWidget(forms.widgets.Widget):
    def render(self, name, value, attrs=None, **kwargs):
        html = Template("""<img src="$media$link"/>""")
        return mark_safe(html.substitute(media=settings.MEDIA_URL, link=value))

# A form to create a post
class AddPostForm(forms.ModelForm):
    # picture = ImageField(widget=PictureWidget)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = PostModel
        fields = ['title',  'content', 'picture']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.TextInput(attrs={'class': 'content-input'}),
            'picture': forms.FileInput(attrs={'class': 'input-image-control'}),
        }

# A form to create a custom user
class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(
        label='Имя', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': "Имя"}))
    last_name = forms.CharField(
        label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': "Фамилия"}))
    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(
        attrs={'class': 'form-input', 'placeholder': "Электронная почта"}))
    password1 = forms.CharField(
        label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': "Пароль"}))
    password2 = forms.CharField(
        label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': "Подтверждение пароля"}))


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'country', 'profile_image', 'birth_date']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
            'country' : forms.Select(attrs={'class': 'select-input'})
        }


# A form to login the user
class LoginUserForm(AuthenticationForm):
    password = forms.CharField(
        label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))