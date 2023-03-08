from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SigUpForm
from .models import ProfileUser, VegetableCard
from django.views.generic.edit import FormView
from django.views.generic import ListView

@login_required
def show_profile(request):
    return render(request,'Earth/main/home.html')
    
def test(request):
    print(request.user)
    profile = ProfileUser.objects.filter(user =  request.user)
    Veg = VegetableCard.objects.filter(user = request.user)
    
    return render(request,'Earth/main/index.html', {'veg':Veg})

class UserCreated(FormView):
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

        