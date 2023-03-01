from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SigUpForm
# from django.contrib.auth.


def RegForm(request):
    form = SigUpForm(request.POST)
    if form.is_valid():
        
        user = form.save()
        user.refresh_from_db()
        user.ProfileUser.first_name = form.cleaned_data.get('first_name')
        user.ProfileUser.last_name = form.cleaned_data.get('last_name')
        user.ProfileUser.email = form.cleaned_data.get('email')
        user.save()
        
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username,password)
        login(request,user)
        
        return redirect('home')
    else:
        form = SigUpForm()
    return render(request, 'Earth/registration/RegForm.html',{'form':form})
