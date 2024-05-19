from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Trainings
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class TrainingForm(forms.ModelForm):
    class Meta: 
        model = Trainings
        fields = ['title', 'description', 'video_link', 'start_date', 'end_date']