from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ProfileUser, ProductCard
from django.views.generic.edit import FormView
from django.views.generic import ListView, CreateView


class MainPage(ListView):
    '''Отображение товаров на главной странице'''
    model = ProductCard
    template_name = 'Earth/main/index.html'
    context_object_name = 'products'

@login_required
def show_profile(request):
    '''Тестовое отображение профиля'''
    return render(request,'Earth/main/home.html')
    

def test_show_product(request, prod_id):
    prod = get_object_or_404(ProductCard ,pk=prod_id)

    return render(request, 'Earth/main/show_prod.html',{'product':prod})


class UserCreated(FormView):
    '''Форма регистрации'''
    form_class = SigUpForm
    template_name = 'Earth/registration/RegForm.html'
    success_url = ''
# ПЕРЕПИСАТЬ ЧАСТЬ. СЛИШКОМ МНОГО КОДА
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
    ''' Новая версия добовления продукта '''
    model = OpenProductCard
    form_class = OpenAddProductsForm
    template_name = 'Earth/form/getVeg.html'
    

