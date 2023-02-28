from django import forms
from .models import DataVegetables

class MyForm(forms.ModelForm):
    class Meta:
        model = DataVegetables
        fields = ['title','price','description']