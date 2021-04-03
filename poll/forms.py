from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Poll


class PollForm(forms.ModelForm):
    
    class Meta:
        model = Poll
        fields = ("question", "option1", "option2")




