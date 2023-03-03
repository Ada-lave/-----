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
            user = form.save()
            user.refresh_from_db()

            user.ProfileUser.frist_name = form.cleaned_data.get('first_name')
            user.ProfileUser.last_name = form.cleaned_data.get('last_name')
            user.ProfileUser.age = form.cleaned_data.get('age') 
            user.ProfileUser.email = form.cleaned_data.get('email') 
            user.ProfileUser.address = form.cleaned_data('address')
            user.ProfileUser.number_phone = form.cleaned_data('number_phone')
            update_user(user)
            user.save()      

        
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username,password)
            login(request,user)
        
        return redirect('home')
    else:
        form = SigUpForm()
    return render(request, 'Earth/registration/RegForm.html',{'form':form})
