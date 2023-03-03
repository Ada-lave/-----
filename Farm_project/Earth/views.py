from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SigUpForm
from .models import ProfileUser

def update_user(user):
    ProfileUser.objects.update_or_create(user=user)


def RegForm(request):
    if request.method == 'POST':
        form = SigUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            form.save_m2m()

            age = request.POST.get('age')
            profile = user.profileuser
            profile.first_name = form.cleaned_data.get('first_name')
            profile.last_name = form.cleaned_data.get('last_name')
            profile.address = form.cleaned_data.get('adress')
            profile.number_phone = form.cleaned_data.get('number_phone')
            profile.age = form.cleaned_data.get('age')
            profile.email = form.cleaned_data.get('email')
            profile.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request,user)
        
        return redirect('home')
    else:
        form = SigUpForm()
    return render(request, 'Earth/registration/RegForm.html',{'form':form})
