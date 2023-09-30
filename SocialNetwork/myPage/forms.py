from django import forms
from django.views.generic.edit import UpdateView
from .models import *

from django.contrib.auth import get_user_model
User = get_user_model()

# A form to create a post
class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = PostModel
        fields = ['title',  'content', 'picture']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.TextInput(attrs={'class': 'content-input'}),
        }



