from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class SigUpForm(UserCreationForm):
    '''Форма для регистрации юзера'''
    username = forms.CharField(max_length=128)
    email = forms.EmailField(max_length=200)
    age = forms.CharField(max_length=100)
    number_phone = forms.CharField(max_length=100)
    adress = forms.CharField(max_length=1000)
    first_name = forms.CharField(max_length=120)
    last_name = forms.CharField(max_length=200)
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','age','number_phone','adress','email','password1','password2']

class OpenAddProductsForm(forms.ModelForm):
    '''Форма для добавления овощей'''
    class Meta:
        model = OpenProductCard
        fields = ['name','description','category','price']



