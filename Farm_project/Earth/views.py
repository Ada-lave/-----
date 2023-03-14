from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ProfileUser, ProductCard, Post
from django.views.generic.edit import FormView
from django.views.generic import ListView, CreateView


def MainPage(request):
    return render(request, 'Earth/main/index.html')

@login_required
def show_profile(request):
    '''Тестовое отображение профиля'''
    return render(request,'Earth/main/home.html')
    
def test(request):
    print(request.user)
    profile = ProfileUser.objects.filter(user =  request.user)
    Veg = ProductCard.objects.filter(user = request.user)
    
    return render(request,'Earth/main/index.html', {'veg':Veg})

class UserCreated(FormView):
    '''Форма регистрации'''
    form_class = SigUpForm
    template_name = 'Earth/registration/RegForm.html'
    success_url = ''

    def form_valid(self, form):
        user = form.save()
        profile = user.profileuser
        profile.first_name = form.cleaned_data.get('first_name')
        profile.last_name = form.cleaned_data.get('last_name')
        profile.address = form.cleaned_data.get('adress')
        profile.number_phone = form.cleaned_data.get('number_phone')
        profile.age = form.cleaned_data.get('age')
        profile.email = form.cleaned_data.get('email')
        profile.save()
        
        return super(UserCreated, self).form_valid(form)


class AddProduct(CreateView):
    model = ProductCard
    form_class = AddProductsForm
    template_name = 'Earth/form/getVeg.html'
    def form_valid(self,form):
        form.instance.user = self.request.user

def AddProducts(request):
    form = AddProductsForm(request.POST,request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.photo = form.cleaned_data.get('photo')
            product.name = form.cleaned_data.get('name')
            product.description = form.cleaned_data.get('description')
            product.price = form.cleaned_data.get('price')
            product.category =  form.cleaned_data.get('category')
            product.save()
    else:
        form = AddProductsForm()    
    
    return render(request, 'Earth/form/getVeg.html', {"form":form})
            