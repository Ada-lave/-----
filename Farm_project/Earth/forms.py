from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SigUpForm(UserCreationForm):
    username = forms.CharField(max_length=128)
    email = forms.EmailField(max_length=200)
    
    first_name = forms.CharField(max_length=120)
    last_name = forms.CharField(max_length=200)
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
